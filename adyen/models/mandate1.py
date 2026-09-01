from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .enums.mandate_status2 import MandateStatus2OrStr
from .enums.mandate_type2 import MandateType2OrStr
from .mandate_bank_account2 import MandateBankAccount2, MandateBankAccount2Dict


class Mandate1(SdkBaseModel):
    balance_account_id: Optional[str] = Field(default=UNSET, alias="balanceAccountId")
    """The unique identifier of the balance account linked to the payment instrument."""

    counterparty: Optional[MandateBankAccount2] = UNSET
    """Contains information to identify the counterparty."""

    created_at: Optional[RFC3339DateTime] = Field(default=UNSET, alias="createdAt")
    """The date when the mandate was created."""

    id: Optional[str] = UNSET
    """The unique identifier of the mandate."""

    payment_instrument_id: Optional[str] = Field(default=UNSET, alias="paymentInstrumentId")
    """The unique identifier of the payment instrument linked to the mandate."""

    status: Optional[MandateStatus2OrStr] = UNSET
    """The status of the mandate.

    Possible values: **pending**, **approved**, **cancelled**."""

    type_: Optional[MandateType2OrStr] = Field(default=UNSET, alias="type")
    """The type of mandate. Possible value: **bacs**."""

    updated_at: Optional[RFC3339DateTime] = Field(default=UNSET, alias="updatedAt")
    """The date when the mandate was updated."""


class Mandate1Dict(TypedDict):
    balance_account_id: NotRequired[str]
    counterparty: NotRequired[MandateBankAccount2 | MandateBankAccount2Dict]
    created_at: NotRequired[RFC3339DateTime]
    id: NotRequired[str]
    payment_instrument_id: NotRequired[str]
    status: NotRequired[MandateStatus2OrStr]
    type_: NotRequired[MandateType2OrStr]
    updated_at: NotRequired[RFC3339DateTime]
