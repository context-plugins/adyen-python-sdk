from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class OutputBarcode1(SdkBaseModel):
    """Barcode content to display or print. Mandatory if ``OutputFormat`` is Barcode, not allowed otherwise."""

    barcode_value: str = Field(alias="BarcodeValue")
    """Value with a Barcode coding. The barcode value to display or print."""


class OutputBarcode1Dict(TypedDict):
    barcode_value: str
