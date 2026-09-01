from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class SaleToIssuerData1(SdkBaseModel):
    """Sale information intended for the Issuer. Send to the Acquirer if present."""

    statement_reference: Optional[str] = Field(default=UNSET, alias="StatementReference")
    """Label to print on the bank statement."""


class SaleToIssuerData1Dict(TypedDict):
    statement_reference: NotRequired[str]
