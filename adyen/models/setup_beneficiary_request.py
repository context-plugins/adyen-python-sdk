from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class SetupBeneficiaryRequest(SdkBaseModel):
    destination_account_code: str = Field(alias="destinationAccountCode")
    """The destination account code."""

    merchant_reference: Optional[str] = Field(default=UNSET, alias="merchantReference")
    """A value that can be supplied at the discretion of the executing user."""

    source_account_code: str = Field(alias="sourceAccountCode")
    """The benefactor account."""


class SetupBeneficiaryRequestDict(TypedDict):
    destination_account_code: str
    merchant_reference: NotRequired[str]
    source_account_code: str
