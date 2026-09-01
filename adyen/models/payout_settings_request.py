from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class PayoutSettingsRequest(SdkBaseModel):
    enabled: Optional[bool] = UNSET
    """Indicates if payouts to this bank account are enabled. Default: **true**.

    To receive payouts into this bank account, both ``enabled`` and ``allowed`` must be **true**."""

    enabled_from_date: Optional[str] = Field(default=UNSET, alias="enabledFromDate")
    """The date when Adyen starts paying out to this bank account.

    Format: `ISO 8601 <https://www.w3.org/TR/NOTE-datetime>`__, for example, **2019-11-23T12:25:28Z** or
    **2020-05-27T20:25:28+08:00**.

    If not specified, the ``enabled`` field indicates if payouts are enabled for this bank account.

    If a date is specified and:

    * ``enabled``: **true**, payouts are enabled starting the specified date.
    * ``enabled``: **false**, payouts are disabled until the specified date. On the specified date, ``enabled`` changes
        to **true** and this field is reset to **null**."""

    transfer_instrument_id: str = Field(alias="transferInstrumentId")
    """The unique identifier of the `transfer instrument
    <https://docs.adyen.com/api-explorer/#/legalentity/latest/post/transferInstruments>`__ that contains the details of
    the bank account."""


class PayoutSettingsRequestDict(TypedDict):
    enabled: NotRequired[bool]
    enabled_from_date: NotRequired[str]
    transfer_instrument_id: str
