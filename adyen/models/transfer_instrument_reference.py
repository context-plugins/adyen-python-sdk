from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class TransferInstrumentReference(SdkBaseModel):
    account_identifier: str = Field(alias="accountIdentifier")
    """The masked IBAN or bank account number."""

    id: str
    """The unique identifier of the resource."""

    real_last_four: Optional[str] = Field(default=UNSET, alias="realLastFour")
    """Four last digits of the bank account number. If the transfer instrument is created using `instant bank account
    verification
    <https://docs.adyen.com/release-notes/platforms-and-financial-products#releaseNote=2023-05-08-hosted-onboarding>`__,
    and it is a virtual bank account, these digits may be different from the last four digits of the masked account
    number."""

    trusted_source: Optional[bool] = Field(default=UNSET, alias="trustedSource")
    """Identifies if the bank account was created through `instant bank verification
    <https://docs.adyen.com/release-notes/platforms-and-financial-products#releaseNote=2023-05-08-hosted-onboarding>`__."""


class TransferInstrumentReferenceDict(TypedDict):
    account_identifier: str
    id: str
    real_last_four: NotRequired[str]
    trusted_source: NotRequired[bool]
