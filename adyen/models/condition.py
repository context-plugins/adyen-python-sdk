from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.balance_type import BalanceTypeOrStr
from .enums.condition_type import ConditionTypeOrStr


class Condition(SdkBaseModel):
    balance_type: BalanceTypeOrStr = Field(alias="balanceType")
    """Define the type of balance about which you want to get notified. Possible values:

    * **available**: the balance available for use.

    * **balance**: the sum of transactions that have already been settled.

    * **pending**: the sum of transactions that will be settled in the future.

    * **reserved**: the balance currently held in reserve."""

    condition_type: ConditionTypeOrStr = Field(alias="conditionType")
    """Define when you want to get notified about a balance change. Possible values:

    * **greaterThan**: the balance in the account(s) exceeds the specified ``value``.

    * **greaterThanOrEqual**: the balance in the account(s) reaches or exceeds the specified ``value``.

    * **lessThan**: the balance in the account(s) drops below the specified ``value``.

    * **lessThanOrEqual**: the balance in the account(s) reaches to drops below the specified ``value``."""

    value: int
    """The value limit in the specified balance type and currency, in minor units."""


class ConditionDict(TypedDict):
    balance_type: BalanceTypeOrStr
    condition_type: ConditionTypeOrStr
    value: int
