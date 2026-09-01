from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.status23 import Status23OrStr
from .platform_payment_configuration1 import PlatformPaymentConfiguration1, PlatformPaymentConfiguration1Dict


class BalanceAccountBase(SdkBaseModel):
    account_holder_id: str = Field(alias="accountHolderId")
    """The unique identifier of the `account holder
    <https://docs.adyen.com/api-explorer/balanceplatform/latest/post/accountHolders#responses-200-id>`__ associated with
    the balance account."""

    default_currency_code: Optional[str] = Field(default=UNSET, alias="defaultCurrencyCode")
    """The default three-character `ISO currency code <https://docs.adyen.com/development-resources/currency-codes>`__
    of the balance account. This is the currency displayed on the Balance Account overview page in your Customer Area.
    The default value is **EUR**.
    > After a balance account is created, you cannot change its default currency."""

    description: Optional[str] = UNSET
    """A human-readable description of the balance account, maximum 300 characters. You can use this parameter to
    distinguish between multiple balance accounts under an account holder."""

    id: str
    """The unique identifier of the balance account."""

    metadata: Optional[dict[str, str]] = UNSET
    """A set of key and value pairs for general use. The keys do not have specific names and may be used for storing
    miscellaneous data as desired.
    > Note that during an update of metadata, the omission of existing key-value pairs will result in the deletion of
        those key-value pairs."""

    migrated_account_code: Optional[str] = Field(default=UNSET, alias="migratedAccountCode")
    """The unique identifier of the account of the migrated account holder in the classic integration."""

    platform_payment_configuration: Optional[PlatformPaymentConfiguration1] = Field(
        default=UNSET, alias="platformPaymentConfiguration"
    )
    """Contains key-value pairs to configure the sales day closing time and settlement delay for a balance account."""

    reference: Optional[str] = UNSET
    """Your reference for the balance account, maximum 150 characters."""

    status: Optional[Status23OrStr] = UNSET
    """The status of the balance account, set to **active** by default."""

    time_zone: Optional[str] = Field(default=UNSET, alias="timeZone")
    """The time zone of the balance account. For example, **Europe/Amsterdam**. Defaults to the time zone of the account
    holder if no time zone is set. For possible values, see the `list of time zone codes
    <https://en.wikipedia.org/wiki/List_of_tz_database_time_zones>`__."""


class BalanceAccountBaseDict(TypedDict):
    account_holder_id: str
    default_currency_code: NotRequired[str]
    description: NotRequired[str]
    id: str
    metadata: NotRequired[dict[str, str]]
    migrated_account_code: NotRequired[str]
    platform_payment_configuration: NotRequired[PlatformPaymentConfiguration1 | PlatformPaymentConfiguration1Dict]
    reference: NotRequired[str]
    status: NotRequired[Status23OrStr]
    time_zone: NotRequired[str]
