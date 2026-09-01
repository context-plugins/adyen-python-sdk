from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class StatusOfLegalProceeding(str, Enum):
    """The status of any current or past legal action taken against the legal entity.

    Possible values: **noLegalActionsTaken**, **underJudicialAdministration**, **bankruptcyInsolvency**,
    **otherLegalMeasures**

    If the value of this field is **noLegalActionsTaken**, then ``dateOfInitiationOfLegalProceeding`` is not required.
    Otherwise, it is required."""

    NO_LEGAL_ACTIONS_TAKEN = "noLegalActionsTaken"
    UNDER_JUDICIAL_ADMINISTRATION = "underJudicialAdministration"
    BANKRUPTCY_INSOLVENCY = "bankruptcyInsolvency"
    OTHER_LEGAL_MEASURES = "otherLegalMeasures"

    __str__ = str.__str__


StatusOfLegalProceedingOrStr: TypeAlias = Annotated[
    StatusOfLegalProceeding | str, open_enum_validator(StatusOfLegalProceeding)
]
