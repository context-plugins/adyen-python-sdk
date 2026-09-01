from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class GetTaxFormRequest(SdkBaseModel):
    account_holder_code: str = Field(alias="accountHolderCode")
    """The account holder code you provided when you created the account holder."""

    form_type: str = Field(alias="formType")
    """Type of the requested tax form. For example, 1099-K."""

    year: int
    """Applicable tax year in the YYYY format."""


class GetTaxFormRequestDict(TypedDict):
    account_holder_code: str
    form_type: str
    year: int
