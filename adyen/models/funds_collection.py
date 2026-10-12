from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .bank_account_identification1 import BankAccountIdentification1, BankAccountIdentification1Dict
from .enums.funds_collection_type2 import FundsCollectionType2OrStr


class FundsCollection(SdkBaseModel):
    account_identification: Optional[BankAccountIdentification1] = Field(default=UNSET, alias="accountIdentification")
    """Contains the identification information of the account to which you can transfer funds related to repayments."""

    funds_collection_type: Optional[FundsCollectionType2OrStr] = Field(default=UNSET, alias="fundsCollectionType")
    """The type of funds collection.

    Possible values: **UnscheduledRepayment**, **Revocation**."""


class FundsCollectionDict(TypedDict):
    account_identification: NotRequired[BankAccountIdentification1Dict]
    funds_collection_type: NotRequired[FundsCollectionType2OrStr]
