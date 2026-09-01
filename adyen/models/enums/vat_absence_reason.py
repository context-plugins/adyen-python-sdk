from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class VatAbsenceReason(str, Enum):
    """The reason the organization has not provided a VAT number.

    Possible values: **industryExemption**, **belowTaxThreshold**."""

    INDUSTRY_EXEMPTION = "industryExemption"
    BELOW_TAX_THRESHOLD = "belowTaxThreshold"

    __str__ = str.__str__


VatAbsenceReasonOrStr: TypeAlias = Annotated[VatAbsenceReason | str, open_enum_validator(VatAbsenceReason)]
