from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.priority import PriorityOrStr
from .enums.verification_status1 import VerificationStatus1OrStr


class PayoutSettings(SdkBaseModel):
    allowed: Optional[bool] = UNSET
    """Indicates if payouts to the bank account are allowed. This value is set automatically based on the status of the
    verification process. The value is:

    * **true** if ``verificationStatus`` is **valid**.
    * **false** for all other values."""

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

    id: str
    """The unique identifier of the payout setting."""

    priority: Optional[PriorityOrStr] = UNSET
    """Determines how long it takes for the funds to reach the bank account. Adyen pays out based on the `payout
    frequency <https://docs.adyen.com/account/getting-paid#payout-frequency>`__. Depending on the currencies and banks
    involved in transferring the money, it may take up to three days for the payout funds to arrive in the bank account.

     Possible values:
    * **first**: same day.
    * **urgent**: the next day.
    * **normal**: between 1 and 3 days."""

    transfer_instrument_id: str = Field(alias="transferInstrumentId")
    """The unique identifier of the `transfer instrument
    <https://docs.adyen.com/api-explorer/#/legalentity/latest/post/transferInstruments>`__ that contains the details of
    the bank account."""

    verification_status: Optional[VerificationStatus1OrStr] = Field(default=UNSET, alias="verificationStatus")
    """The status of the verification process for the bank account.

    Possible values:
    * **valid**: the verification was successful.
    * **pending**: the verification is in progress.
    * **invalid**: the information provided is not complete.
    * **rejected**: there are reasons to refuse working with this entity."""


class PayoutSettingsDict(TypedDict):
    allowed: NotRequired[bool]
    enabled: NotRequired[bool]
    enabled_from_date: NotRequired[str]
    id: str
    priority: NotRequired[PriorityOrStr]
    transfer_instrument_id: str
    verification_status: NotRequired[VerificationStatus1OrStr]
