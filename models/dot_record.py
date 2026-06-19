from dataclasses import dataclass
from decimal import Decimal


@dataclass
class DotRecord:
    inscricao_estadual: str
    razao_social: str
    composicao: str
    valor_vaf: Decimal
    percentual_rcx: Decimal