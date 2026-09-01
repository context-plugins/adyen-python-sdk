from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class BankAccountIdentificationType(str, Enum):
    AU_LOCAL = "auLocal"
    BR_LOCAL = "brLocal"
    CA_LOCAL = "caLocal"
    CZ_LOCAL = "czLocal"
    DK_LOCAL = "dkLocal"
    HK_LOCAL = "hkLocal"
    HU_LOCAL = "huLocal"
    IBAN = "iban"
    IN_LOCAL = "inLocal"
    JP_LOCAL = "jpLocal"
    LEGACY = "legacy"
    MX_LOCAL = "mxLocal"
    MY_LOCAL = "myLocal"
    NO_LOCAL = "noLocal"
    NUMBER_AND_BIC = "numberAndBic"
    NZ_LOCAL = "nzLocal"
    PL_LOCAL = "plLocal"
    SE_LOCAL = "seLocal"
    SG_LOCAL = "sgLocal"
    UK_LOCAL = "ukLocal"
    US_LOCAL = "usLocal"

    __str__ = str.__str__


BankAccountIdentificationTypeOrStr: TypeAlias = Annotated[
    BankAccountIdentificationType | str, open_enum_validator(BankAccountIdentificationType)
]
