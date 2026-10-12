from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .recurring import Recurring, RecurringDict


class RecurringDetailsRequest(SdkBaseModel):
    merchant_account: str = Field(alias="merchantAccount")
    """The merchant account identifier you want to process the (transaction) request with."""

    recurring: Optional[Recurring] = UNSET
    """A container for the type of a recurring contract to be retrieved.

    The contract value needs to match the contract value submitted in the payment transaction used to create a recurring
    contract. However, if ``ONECLICK,RECURRING`` is the original contract definition in the initial payment, then
    ``contract`` should take either ``ONECLICK`` or ``RECURRING``, depending on whether or not you want the shopper to
    enter their card's security code when they finalize their purchase."""

    shopper_reference: str = Field(alias="shopperReference")
    """The reference you use to uniquely identify the shopper (e.g. user ID or account ID)."""


class RecurringDetailsRequestDict(TypedDict):
    merchant_account: str
    recurring: NotRequired[RecurringDict]
    shopper_reference: str
