from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class SweepCounterparty(SdkBaseModel):
    balance_account_id: Optional[str] = Field(default=UNSET, alias="balanceAccountId")
    """The unique identifier of the destination or source `balance account
    <https://docs.adyen.com/api-explorer/#/balanceplatform/latest/post/balanceAccounts__resParam_id>`__.

     > If you are updating the counterparty from a transfer instrument to a balance account, set
            ``transferInstrumentId`` to **null**."""

    merchant_account: Optional[str] = Field(default=UNSET, alias="merchantAccount")
    """The merchant account that will be the source of funds.

    You can only use this parameter with sweeps of ``type`` **pull** and if you are processing payments with Adyen."""

    transfer_instrument_id: Optional[str] = Field(default=UNSET, alias="transferInstrumentId")
    """The unique identifier of the destination or source `transfer instrument
    <https://docs.adyen.com/api-explorer/legalentity/latest/post/transferInstruments#responses-200-id>`__ depending on
    the sweep ``type``

    . To set up automated top-up sweeps to balance accounts in your `marketplace
    <https://docs.adyen.com/marketplaces/top-up-balance-account/#before-you-begin>`__ or `platform
    <https://docs.adyen.com/platforms/top-up-balance-account/#before-you-begin>`__, use this parameter in combination
    with a ``merchantAccount`` and a sweep ``type`` of **pull**.

    Top-up sweeps start a direct debit request from the source transfer instrument. Contact Adyen Support to enable this
    feature.> If you are updating the counterparty from a balance account to a transfer instrument, set
    ``balanceAccountId`` to **null**."""


class SweepCounterpartyDict(TypedDict):
    balance_account_id: NotRequired[str]
    merchant_account: NotRequired[str]
    transfer_instrument_id: NotRequired[str]
