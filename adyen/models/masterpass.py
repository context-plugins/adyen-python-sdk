from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.funding_source import FundingSourceOrStr
from .enums.type35 import Type35OrStr


class Masterpass(SdkBaseModel):
    checkout_attempt_id: Optional[str] = Field(default=UNSET, alias="checkoutAttemptId")
    """The checkout attempt identifier."""

    funding_source: Optional[FundingSourceOrStr] = Field(default=UNSET, alias="fundingSource")
    """The funding source that should be used when multiple sources are available. For Brazilian combo cards, by default
    the funding source is credit. To use debit, set this value to **debit**."""

    masterpass_transaction_id: str = Field(alias="masterpassTransactionId")
    """The Masterpass transaction ID."""

    sdk_data: Optional[str] = Field(default=UNSET, alias="sdkData")
    """Base64-encoded JSON object containing SDK related parameters required by the SDK"""

    type_: Optional[Type35OrStr] = Field(default=UNSET, alias="type")
    """**masterpass**"""


class MasterpassDict(TypedDict):
    checkout_attempt_id: NotRequired[str]
    funding_source: NotRequired[FundingSourceOrStr]
    masterpass_transaction_id: str
    sdk_data: NotRequired[str]
    type_: NotRequired[Type35OrStr]
