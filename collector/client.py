import pandas as pd


class SefazCollector:
    def collect(
        self,
        cpf: str,
        senha: str,
        ano_base: int,
        report_type: str,
        vaf_type: str
    ) -> pd.DataFrame:
        raise NotImplementedError