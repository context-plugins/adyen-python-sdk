from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class StoreSplitConfiguration1(SdkBaseModel):
    """Rules for Adyen for Platforms merchants to split the transaction amount and fees."""

    balance_account_id: Optional[str] = Field(default=UNSET, alias="balanceAccountId")
    """The `unique identifier of the balance account
    <https://docs.adyen.com/api-explorer/#/balanceplatform/latest/get/balanceAccounts/{id}__queryParam_id>`__ to which
    the split amount must be booked, depending on the defined `split logic
    <https://docs.adyen.com/api-explorer/Management/latest/post/merchants/_merchantId_/splitConfigurations#request-rules-splitLogic>`__."""

    split_configuration_id: Optional[str] = Field(default=UNSET, alias="splitConfigurationId")
    """The unique identifier of the `split configuration profile
    <https://docs.adyen.com/platforms/automatic-split-configuration/create-split-configuration/>`__."""


class StoreSplitConfiguration1Dict(TypedDict):
    balance_account_id: NotRequired[str]
    split_configuration_id: NotRequired[str]
