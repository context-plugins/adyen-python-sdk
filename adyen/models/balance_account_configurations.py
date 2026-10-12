from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .balance_account_configuration import BalanceAccountConfiguration, BalanceAccountConfigurationDict
from .link2 import Link2, Link2Dict


class BalanceAccountConfigurations(SdkBaseModel):
    balance_account_payout_schedules: list[BalanceAccountConfiguration] = Field(alias="balanceAccountPayoutSchedules")
    """Contains a list of the Balance Account payout schedules."""

    link: Link2
    """Contains links to the next and previous page whenever applicable."""


class BalanceAccountConfigurationsDict(TypedDict):
    balance_account_payout_schedules: list[BalanceAccountConfigurationDict]
    link: Link2Dict
