from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class BrlocalAccountIdentification(SdkBaseModel):
    account_number: str = Field(alias="accountNumber")
    """The bank account number, without separators or whitespace."""

    bank_code: str = Field(alias="bankCode")
    """The 3-digit bank code, with leading zeros."""

    branch_number: str = Field(alias="branchNumber")
    """The bank account branch number, without separators or whitespace."""

    ispb: Optional[str] = UNSET
    """The 8-digit ISPB, with leading zeros."""

    type_: Literal["brLocal"] = Field(default="brLocal", alias="type")
    """**brLocal**"""


class BrlocalAccountIdentificationDict(TypedDict):
    account_number: str
    bank_code: str
    branch_number: str
    ispb: NotRequired[str]
    type_: Literal["brLocal"]
