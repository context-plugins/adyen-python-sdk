from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Folio(SdkBaseModel):
    cash_advances: Optional[int] = Field(default=UNSET, alias="cashAdvances")
    """The folio cash advances, in `minor units <https://docs.adyen.com/development-resources/currency-codes>`__.
    * For example, 2000 means USD 20.00.
    * Encoding: Numeric
    * Max value: 10000000000
    * **additionalData key:** ``lodging.folioCashAdvances``"""

    number: Optional[str] = UNSET
    """The card acceptor's internal invoice or billing ID reference number.
    * Format: Alphanumeric
    * Must not start with a space
    * Must not contain any special characters
    * Must not be all zeros.
    * **additionalData key:** ``lodging.folioNumber``"""


class FolioDict(TypedDict):
    cash_advances: NotRequired[int]
    number: NotRequired[str]
