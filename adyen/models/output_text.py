from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.alignment1 import Alignment1OrStr
from .enums.character_height1 import CharacterHeight1OrStr
from .enums.character_style1 import CharacterStyle1OrStr
from .enums.character_width1 import CharacterWidth1OrStr


class OutputText(SdkBaseModel):
    """Content of text message to display or print. It conveys information related to the content of the text message
    and its format. All the data elements related to the format of the text to display or print are parameters valid for
    the whole text content."""

    text: str = Field(alias="Text")
    """Content of text message to display, print or play."""

    character_set: Optional[int] = Field(default=UNSET, alias="CharacterSet")
    """Character height of the text string to display or print. Absence of this data element means the characters have
    normal height."""

    start_row: Optional[int] = Field(default=UNSET, alias="StartRow")
    """Row where the text string has to be displayed or printed."""

    start_column: Optional[int] = Field(default=UNSET, alias="StartColumn")
    """Column where the text string has to be displayed or printed."""

    character_width: Optional[CharacterWidth1OrStr] = Field(default=UNSET, alias="CharacterWidth")
    """Character width of the text string to display or print. Absence of this data element means the characters have
    normal width. Possible values:
    * **DoubleWidth**
    * **SingleWidth**"""

    character_height: Optional[CharacterHeight1OrStr] = Field(default=UNSET, alias="CharacterHeight")
    """Character height of the text string to display or print. Absence of this data element means the characters have
    normal height. Possible values:
    * **DoubleHeight**
    * **HalfHeight**
    * **SingleHeight**"""

    character_style: Optional[CharacterStyle1OrStr] = Field(default=UNSET, alias="CharacterStyle")
    """Typographic style of the sequence of characters to display or print. Absence of this data element means the
    characters have normal style. Possible values:
    * **Bold**
    * **Italic**
    * **Normal**
    * **Underline**"""

    alignment: Optional[Alignment1OrStr] = Field(default=UNSET, alias="Alignment")
    """Alignment of the text string on the display line or print line. Absence of this data element means the characters
    have normal alignment. Possible values:
    * **Centred**
    * **Justified**
    * **Left**
    * **Right**"""

    end_of_line_flag: bool = Field(default=True, alias="EndOfLineFlag")
    """Indicates if the text is at the end of a line. Allows the display or the print of a new line and a carry-over
    return characters after the formatted text."""


class OutputTextDict(TypedDict):
    text: str
    character_set: NotRequired[int]
    start_row: NotRequired[int]
    start_column: NotRequired[int]
    character_width: NotRequired[CharacterWidth1OrStr]
    character_height: NotRequired[CharacterHeight1OrStr]
    character_style: NotRequired[CharacterStyle1OrStr]
    alignment: NotRequired[Alignment1OrStr]
    end_of_line_flag: NotRequired[bool]
