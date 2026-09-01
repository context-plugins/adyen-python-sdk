from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.output_format1 import OutputFormat1OrStr
from .output_barcode1 import OutputBarcode1, OutputBarcode1Dict
from .output_text import OutputText, OutputTextDict
from .predefined_content1 import PredefinedContent1, PredefinedContent1Dict


class OutputContent3(SdkBaseModel):
    """Content to display or print. This is a sequence of elements if they have different formats."""

    output_format: OutputFormat1OrStr = Field(alias="OutputFormat")
    """Format of the content to display or print. Possible values:
    * **BarCode**
    * **MessageRef**
    * **Text**
    * **XHTML**"""

    predefined_content: Optional[PredefinedContent1] = Field(default=UNSET, alias="PredefinedContent")
    """Reference of a predefined message to display or print. Mandatory, if ``OutputFormat`` is MessageRef, not allowed
    otherwise."""

    output_text: Optional[list[OutputText]] = Field(default=UNSET, alias="OutputText")
    """Content of text message to display or print. Mandatory, if ``OutputFormat`` is Text, not allowed otherwise. One
    instance of ``OutputText`` per shared format."""

    output_xhtml: Optional[str] = Field(default=UNSET, alias="OutputXHTML")
    """XHTML document body containing the message to display or print. Mandatory if ``OutputFormat`` is XHTML, not
    allowed otherwise."""

    output_barcode: Optional[OutputBarcode1] = Field(default=UNSET, alias="OutputBarcode")
    """Barcode content to display or print. Mandatory if ``OutputFormat`` is Barcode, not allowed otherwise."""


class OutputContent3Dict(TypedDict):
    output_format: OutputFormat1OrStr
    predefined_content: NotRequired[PredefinedContent1 | PredefinedContent1Dict]
    output_text: NotRequired[list[OutputText | OutputTextDict]]
    output_xhtml: NotRequired[str]
    output_barcode: NotRequired[OutputBarcode1 | OutputBarcode1Dict]
