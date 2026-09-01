from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .sale_to_poirequest import SaleToPoirequest, SaleToPoirequestDict


class TerminalApirequest(SdkBaseModel):
    """The request payload of the Adyen Terminal API."""

    sale_to_poi_request: SaleToPoirequest = Field(alias="SaleToPOIRequest")
    """The SaleToPOIRequest message pair is a container for the request message content. It contains a MessageHeader and
    a message body."""


class TerminalApirequestDict(TypedDict):
    sale_to_poi_request: SaleToPoirequest | SaleToPoirequestDict
