from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class SaleToIssuerData(SdkBaseModel):
    """Sale information intended for the Issuer. The POI System receives this information and sends it to the Acquirer
    for the Issuer without any change."""

    statement_reference: Optional[str] = Field(default=UNSET, alias="StatementReference")
    """Label to print on the bank statement."""


class SaleToIssuerDataDict(TypedDict):
    statement_reference: NotRequired[str]
