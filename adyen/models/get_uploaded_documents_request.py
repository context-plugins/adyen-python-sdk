from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class GetUploadedDocumentsRequest(SdkBaseModel):
    account_holder_code: str = Field(alias="accountHolderCode")
    """The code of the Account Holder for which to retrieve the documents."""

    bank_account_uuid: Optional[str] = Field(default=UNSET, alias="bankAccountUUID")
    """The code of the Bank Account for which to retrieve the documents."""

    shareholder_code: Optional[str] = Field(default=UNSET, alias="shareholderCode")
    """The code of the Shareholder for which to retrieve the documents."""


class GetUploadedDocumentsRequestDict(TypedDict):
    account_holder_code: str
    bank_account_uuid: NotRequired[str]
    shareholder_code: NotRequired[str]
