from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class GetAccountHolderRequest(SdkBaseModel):
    account_code: Optional[str] = Field(default=UNSET, alias="accountCode")
    """The code of the account of which to retrieve the details.
    > Required if no ``accountHolderCode`` is provided."""

    account_holder_code: Optional[str] = Field(default=UNSET, alias="accountHolderCode")
    """The code of the account holder of which to retrieve the details.
    > Required if no ``accountCode`` is provided."""

    show_details: Optional[bool] = Field(default=UNSET, alias="showDetails")
    """True if the request should return the account holder details"""


class GetAccountHolderRequestDict(TypedDict):
    account_code: NotRequired[str]
    account_holder_code: NotRequired[str]
    show_details: NotRequired[bool]
