from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .balance_platform_configuration import BalancePlatformConfiguration, BalancePlatformConfigurationDict


class BalancePlatformConfigurations(SdkBaseModel):
    balance_platform_payout_schedules: list[BalancePlatformConfiguration] = Field(
        alias="balancePlatformPayoutSchedules"
    )
    """Contains a list of the payout schedules configured in your balance platform."""


class BalancePlatformConfigurationsDict(TypedDict):
    balance_platform_payout_schedules: list[BalancePlatformConfiguration | BalancePlatformConfigurationDict]
