from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class TransactionRuleSource(SdkBaseModel):
    id: Optional[str] = UNSET
    """ID of the resource, when applicable."""

    type_: Optional[str] = Field(default=UNSET, alias="type")
    """Indicates the type of resource for which the transaction rule is defined.

    Possible values:

     * **PaymentInstrumentGroup**

    * **PaymentInstrument**

    * **BalancePlatform**

    * **EntityUsageConfiguration**

    * **PlatformRule**: The transaction rule is a platform-wide rule imposed by Adyen."""


class TransactionRuleSourceDict(TypedDict):
    id: NotRequired[str]
    type_: NotRequired[str]
