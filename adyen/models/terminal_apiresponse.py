from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .sale_to_poiresponse import SaleToPoiresponse, SaleToPoiresponseDict


class TerminalApiresponse(SdkBaseModel):
    """The response payload of the Adyen Terminal API."""

    sale_to_poi_response: SaleToPoiresponse = Field(alias="SaleToPOIResponse")
    """The SaleToPOIResponse message pair is a container for the response message content. It contains a MessageHeader
    and a message body."""


class TerminalApiresponseDict(TypedDict):
    sale_to_poi_response: SaleToPoiresponse | SaleToPoiresponseDict
