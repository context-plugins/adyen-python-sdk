from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class OutputBarcode(SdkBaseModel):
    barcode_value: str = Field(alias="BarcodeValue")
    """Value with a Barcode coding. The barcode value to display or print."""


class OutputBarcodeDict(TypedDict):
    barcode_value: str
