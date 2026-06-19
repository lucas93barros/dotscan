
import subprocess
from playwright.sync_api import sync_playwright
from config import LOGIN_URL


class SefazAuth:
    def login(self, cpf: str, senha: str):

         # garante instalação do Chromium no Streamlit Cloud
        subprocess.run(
            ["playwright", "install", "chromium"],
            check=True
        )
        playwright = sync_playwright().start()

        browser = playwright.chromium.launch(
            headless=True
        )

        context = browser.new_context()
        page = context.new_page()

        page.goto(
            LOGIN_URL,
            wait_until="domcontentloaded",
            timeout=120000
        )

        page.fill('input[name="cod_cpf"]', cpf)
        page.fill('#dsc_senha', senha)

        page.click('input[type="submit"]')
        page.wait_for_load_state("domcontentloaded")

        if page.locator("text=Lista de Funções").count() == 0:
            raise Exception("Falha na autenticação")

        return page, browser, playwright
