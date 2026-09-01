from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.creation_result_code import CreationResultCodeOrStr


class TestCardRangeCreationResult(SdkBaseModel):
    card_number_range_end: str = Field(alias="cardNumberRangeEnd")
    """The last test card number in the generated test card range.

    Example: 5432 1234 1234 4321"""

    card_number_range_start: str = Field(alias="cardNumberRangeStart")
    """The first test card number in the generated test card range.

    Example: 5432 1234 1234 1234"""

    creation_result_code: CreationResultCodeOrStr = Field(alias="creationResultCode")
    """Notification message. It informs about the outcome of the operation. Possible values:
    * CREATED
    * ALREADY_EXISTS
    * ERROR"""

    message: Optional[str] = UNSET
    """An optional information message about the result."""


class TestCardRangeCreationResultDict(TypedDict):
    card_number_range_end: str
    card_number_range_start: str
    creation_result_code: CreationResultCodeOrStr
    message: NotRequired[str]
