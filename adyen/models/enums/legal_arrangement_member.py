from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class LegalArrangementMember(str, Enum):
    BENEFICIARY = "Beneficiary"
    CONTROLLING_PERSON = "ControllingPerson"
    PARTNER = "Partner"
    PROTECTOR = "Protector"
    SETTLOR = "Settlor"
    SHAREHOLDER = "Shareholder"
    TRUSTEE = "Trustee"

    __str__ = str.__str__


LegalArrangementMemberOrStr: TypeAlias = Annotated[
    LegalArrangementMember | str, open_enum_validator(LegalArrangementMember)
]
