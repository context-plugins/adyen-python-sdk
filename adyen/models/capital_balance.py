from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class CapitalBalance(SdkBaseModel):
    """An object containing the details of the existing grant., Contains information about the balances of the
    disbursement., Contains information about the balances of the grant."""

    currency: str
    """The three-character `ISO currency code <https://docs.adyen.com/development-resources/currency-codes>`__."""

    fee: int
    """Fee amount."""

    principal: int
    """Principal amount."""

    total: int
    """Total amount. A sum of principal amount and fee amount."""


class CapitalBalanceDict(TypedDict):
    currency: str
    fee: int
    principal: int
    total: int
