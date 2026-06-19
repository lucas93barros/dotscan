import streamlit as st

from collector.auth import SefazAuth
from collector.navigator import SefazNavigator
from collector.extractor import SefazExtractor

from exporters.csv_exporter import CSVExporter
from exporters.excel_exporter import ExcelExporter


st.set_page_config(
    page_title="DOTScan",
    layout="wide"
)

st.title("DOTScan")
st.subheader("Automação de extração de DOTs - SEFAZ ES")


# =========================
# Inputs
# =========================

cpf = st.text_input("CPF")
senha = st.text_input("Senha", type="password")

ano_base = st.selectbox(
    "Ano Base",
    [2025, 2024, 2023, 2022, 2021]
)

report_type = st.radio(
    "Tipo de Relatório",
    ["provisorio", "definitivo"]
)

vaf_type = st.selectbox(
    "VAF",
    [
        "vaf1",
        "vaf2",
        "vaf3",
        "vaf3_sicop",
        "vaf4"
    ]
)


# =========================
# Execução
# =========================

if st.button("Executar"):

    with st.spinner("Executando extração..."):

        auth = SefazAuth()
        navigator = SefazNavigator()
        extractor = SefazExtractor()
        csv_exporter = CSVExporter()
        excel_exporter = ExcelExporter()

        try:
            # login
            page, browser, playwright = auth.login(
                cpf=cpf,
                senha=senha
            )

            # navegar
            page = navigator.go_to_reports(page)

            # selecionar ano
            page = navigator.select_year(
                page,
                ano_base
            )

            # selecionar relatório
            page = navigator.select_report(
                page,
                report_type,
                vaf_type,
                ano_base
            )

            # extrair tabela
            df = extractor.extract_table(page)

            # feedback
            st.success("Extração concluída")

            # render
            st.dataframe(df)

            # exportações
            csv = csv_exporter.export(df)
            excel_data = excel_exporter.export(df)

            # botões
            col1, col2, col3 = st.columns([6, 1, 1])

            with col2:
                st.download_button(
                    label="Baixar CSV",
                    data=csv,
                    file_name=f"dotscan_{ano_base}_{vaf_type}.csv",
                    mime="text/csv"
                )

            with col3:
                st.download_button(
                    label="Baixar Excel",
                    data=excel_data,
                    file_name=f"dotscan_{ano_base}_{vaf_type}.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                )

        except Exception as e:
            st.error(str(e))

        finally:
            browser.close()
            playwright.stop()
            