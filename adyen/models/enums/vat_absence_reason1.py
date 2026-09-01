from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class VatAbsenceReason1(str, Enum):
    """The reason for not providing a VAT number.

    Possible values: **industryExemption**, **belowTaxThreshold**."""

    INDUSTRY_EXEMPTION = "industryExemption"
    BELOW_TAX_THRESHOLD = "belowTaxThreshold"

    __str__ = str.__str__


VatAbsenceReason1OrStr: TypeAlias = Annotated[VatAbsenceReason1 | str, open_enum_validator(VatAbsenceReason1)]
