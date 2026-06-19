from playwright.sync_api import sync_playwright
from config import LOGIN_URL


class SefazAuth:
    def login(self, cpf: str, senha: str):
        playwright = sync_playwright().start()

        browser = playwright.chromium.launch(
            headless=False
        )

        context = browser.new_context()
        page = context.new_page()

        page.goto(LOGIN_URL)
        page.fill('input[name="cod_cpf"]', cpf)
        page.fill('#dsc_senha', senha)
        page.click('input[type="submit"]')
        page.wait_for_load_state("networkidle")
        if page.locator("text=Lista de Funções").count() == 0:
            raise Exception("Falha na autenticação")

        return page, browser, playwright