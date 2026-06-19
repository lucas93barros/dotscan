from io import StringIO
import pandas as pd


class SefazExtractor:

    def extract_table(self, page):
        tables = page.locator("table")
        total = tables.count()

        print("TOTAL DE TABELAS:", total)

        if total == 0:
            raise Exception("Nenhuma tabela encontrada.")

        # tenta pegar a tabela de resultado
        for i in range(total):
            html = tables.nth(i).evaluate(
                "el => el.outerHTML"
            )

            if "INSCRIÇÃO" in html and "RAZÃO SOCIAL" in html:
                df = pd.read_html(
                    StringIO(html)
                )[0]

                return df

        raise Exception(
            "Tabela de dados não encontrada."
        )