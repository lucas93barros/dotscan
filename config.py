BASE_URL = "https://s1-internet.sefaz.es.gov.br"
LOGIN_URL = f"{BASE_URL}/site-ipm-internet/rel_restritos/index"

DEFAULT_TIMEOUT = 30000  # ms
TABLE_TIMEOUT = 60000

REPORT_TYPES = {
    "provisorio": "Provisório",
    "definitivo": "Definitivo"
}

VAF_TYPES = {
    "vaf1": "VAF1",
    "vaf2": "VAF2",
    "vaf3": "VAF3",
    "vaf3_sicop": "VAF3_SICOP",
    "vaf4": "VAF4"
}