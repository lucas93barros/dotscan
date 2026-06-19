from config import BASE_URL


class SefazNavigator:

    def go_to_reports(self, page):
        page.click("text=Relatórios de IPM")
        page.wait_for_load_state("networkidle")

        return page

    def select_year(self, page, ano_base: int):
        page.select_option(
            'select[name="ano_base"]',
            str(ano_base)
        )

        page.click('input[name="btSelecionar"]')

        page.wait_for_timeout(3000)

        page.wait_for_selector(
            "a[href*='ipm_resultado']"
        )

        return page

    def select_report(
        self,
        page,
        report_type,
        vaf_type,
        ano_base
    ):
        tipo_map = {
            "provisorio": 0,
            "definitivo": 1
        }

        cat_map = {
            "vaf1": 9,
            "vaf2": 10,
            "vaf3": 11,
            "vaf3_sicop": 15,
            "vaf4": 12
        }

        url = (
            f"{BASE_URL}/site-ipm-internet/rel_restritos/"
            f"ipm_resultado?tipo={tipo_map[report_type]}"
            f"&cat={cat_map[vaf_type]}"
            f"&ano_base={ano_base}"
        )

        print("URL GERADA:", url)

        page.goto(url)

        page.wait_for_selector(
            "table.resultado"
        )

        print("URL FINAL:", page.url)

        return page