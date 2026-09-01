from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .amount17 import Amount17, Amount17Dict
from .cash_out_info_counterparty1 import CashOutInfoCounterparty1, CashOutInfoCounterparty1Dict
from .cash_out_transfer import CashOutTransfer, CashOutTransferDict
from .fee21 import Fee21, Fee21Dict


class CashOut(SdkBaseModel):
    amount: Amount17
    """Contains the amount of the cashout, in `minor units
    <https://docs.adyen.com/development-resources/currency-codes>`__."""

    counterparty: Optional[CashOutInfoCounterparty1] = UNSET
    """Contains information about the counterparty of the cashout transfer."""

    description: Optional[str] = UNSET
    """Allowed and returned only when you provide the ``counterparty.transferInstrumentId`` field.

    Your description of the cashout transfer. This description is used by most banks as the transfer description. We
    recommend sending a maximum of 140 characters, otherwise the description may be truncated.

    If you do not provide a description, Adyen generates a description automatically. This generated description is not
    returned in the response.

    Supported characters: **[a-z] [A-Z] [0-9] / - ? : ( ) . , ' + Space**."""

    fee: Optional[Fee21] = UNSET
    """Contains the currency and value of the cashout fee, in `minor units
    <https://docs.adyen.com/development-resources/currency-codes>`__."""

    id: str
    """The unique identifier of the cashout reference."""

    instructing_balance_account_id: str = Field(alias="instructingBalanceAccountId")
    """The unique identifier of the balance account that initiates the cashout request."""

    reference_for_beneficiary: Optional[str] = Field(default=UNSET, alias="referenceForBeneficiary")
    """Allowed and returned only when you provide the ``counterparty.transferInstrumentId`` field.

    The reference that is sent to the recipient of a cashout transfer. This reference is also sent in all webhooks
    related to the cashout transfer, so you can use it to track the status of the transfer.

    If you do not provide a reference for the beneficiary, Adyen generates one automatically. This generated reference
    for the beneficiary is not returned in the response.

    Supported characters: **a-z**, **A-Z**, **0-9**."""

    transfer_instrument_id: Optional[str] = Field(default=UNSET, alias="transferInstrumentId")
    """**Use ``counterparty.transferInstrumentId`` instead.**

    The unique identifier of the counterparty transfer instrument."""

    transfers: list[CashOutTransfer]
    """The list of transfers related to cashout."""


class CashOutDict(TypedDict):
    amount: Amount17 | Amount17Dict
    counterparty: NotRequired[CashOutInfoCounterparty1 | CashOutInfoCounterparty1Dict]
    description: NotRequired[str]
    fee: NotRequired[Fee21 | Fee21Dict]
    id: str
    instructing_balance_account_id: str
    reference_for_beneficiary: NotRequired[str]
    transfer_instrument_id: NotRequired[str]
    transfers: list[CashOutTransfer | CashOutTransferDict]
