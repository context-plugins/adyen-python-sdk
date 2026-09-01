from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.priority1 import Priority1OrStr


class RoutingDetails(SdkBaseModel):
    detail: Optional[str] = UNSET
    """A human-readable explanation specific to this occurrence of the problem."""

    error_code: Optional[str] = Field(default=UNSET, alias="errorCode")
    """A code that identifies the problem type."""

    priority: Optional[Priority1OrStr] = UNSET
    """The priority for the bank transfer. This sets the speed at which the transfer is sent and the fees that you have
    to pay. Required for transfers with ``category`` **bank**.

    Possible values:

    * **regular**: For normal, low-value transactions.

    * **fast**: A faster way to transfer funds, but the fees are higher. Recommended for high-priority, low-value
        transactions.

    * **wire**: The fastest way to transfer funds, but this has the highest fees. Recommended for high-priority,
        high-value transactions.

    * **instant**: For instant funds transfers within the United States and in `SEPA locations
        <https://www.ecb.europa.eu/paym/integration/retail/sepa/html/index.en.html>`__.

    * **crossBorder**: For high-value transfers to a recipient in a different country.

    * **internal**: For transfers to an Adyen-issued business bank account (by bank account number/IBAN)."""

    title: Optional[str] = UNSET
    """A short, human-readable summary of the problem type."""


class RoutingDetailsDict(TypedDict):
    detail: NotRequired[str]
    error_code: NotRequired[str]
    priority: NotRequired[Priority1OrStr]
    title: NotRequired[str]
