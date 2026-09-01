from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.status43 import Status43OrStr
from .platform_payment_configuration1 import PlatformPaymentConfiguration1, PlatformPaymentConfiguration1Dict


class BalanceAccountUpdateRequest(SdkBaseModel):
    account_holder_id: Optional[str] = Field(default=UNSET, alias="accountHolderId")
    """The unique identifier of the `account holder
    <https://docs.adyen.com/api-explorer/balanceplatform/latest/post/accountHolders#responses-200-id>`__ associated with
    the balance account."""

    description: Optional[str] = UNSET
    """A human-readable description of the balance account. You can use this parameter to distinguish between multiple
    balance accounts under an account holder."""

    metadata: Optional[dict[str, str]] = UNSET
    """A set of key and value pairs for general use. The keys do not have specific names and may be used for storing
    miscellaneous data as desired.
    > Note that during an update of metadata, the omission of existing key-value pairs will result in the deletion of
        those key-value pairs."""

    platform_payment_configuration: Optional[PlatformPaymentConfiguration1] = Field(
        default=UNSET, alias="platformPaymentConfiguration"
    )
    """Contains key-value pairs to configure the sales day closing time and settlement delay for a balance account."""

    reference: Optional[str] = UNSET
    """Your reference to the balance account."""

    status: Optional[Status43OrStr] = UNSET
    """The status of the balance account. Payment instruments linked to the balance account can only be used if the
    balance account status is **active**.

    Possible values: **active**, **closed**, **suspended**."""

    time_zone: Optional[str] = Field(default=UNSET, alias="timeZone")
    """The time zone of the balance account. For example, **Europe/Amsterdam**. Defaults to the time zone of the account
    holder if no time zone is set. For possible values, see the `list of time zone codes
    <https://en.wikipedia.org/wiki/List_of_tz_database_time_zones>`__."""


class BalanceAccountUpdateRequestDict(TypedDict):
    account_holder_id: NotRequired[str]
    description: NotRequired[str]
    metadata: NotRequired[dict[str, str]]
    platform_payment_configuration: NotRequired[PlatformPaymentConfiguration1 | PlatformPaymentConfiguration1Dict]
    reference: NotRequired[str]
    status: NotRequired[Status43OrStr]
    time_zone: NotRequired[str]
