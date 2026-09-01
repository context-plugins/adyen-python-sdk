from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.menu_entry_tag1 import MenuEntryTag1OrStr
from .enums.output_format2 import OutputFormat2OrStr
from .output_text import OutputText, OutputTextDict
from .predefined_content import PredefinedContent, PredefinedContentDict


class MenuEntry(SdkBaseModel):
    """An entry of the menu to present to the Cashier. It conveys message text and parameters of the menu entry. This
    output data could be only provided for an input command, in order to choose an entry of the menu."""

    menu_entry_tag: Optional[MenuEntryTag1OrStr] = Field(default=UNSET, alias="MenuEntryTag")
    """Characteristics related to the selection of a menu entry. Possible values:
    * **NonSelectable**
    * **NonSelectableSubMenu**
    * **Selectable**
    * **SubMenu**"""

    default_selected_flag: Optional[bool] = Field(default=UNSET, alias="DefaultSelectedFlag")
    """Selection of a menu entry to be displayed. In Input request message, it allows selection of one or several menu
    entries before any user action."""

    output_format: OutputFormat2OrStr = Field(alias="OutputFormat")
    """Possible values:
    * **BarCode**
    * **MessageRef**
    * **Text**
    * **XHTML**"""

    predefined_content: Optional[PredefinedContent] = Field(default=UNSET, alias="PredefinedContent")
    """Reference of a predefined message to display or print. It conveys information related to the predefined
    message."""

    output_text: Optional[list[OutputText]] = Field(default=UNSET, alias="OutputText")
    """Content of text message to display or print. It conveys Information related to the content of the text message
    and its format. All the data elements related to the format of the text to display or print are parameters valid for
    the whole Text content."""

    output_xhtml: Optional[str] = Field(default=UNSET, alias="OutputXHTML")
    """XHTML document body containing the message to display or print."""


class MenuEntryDict(TypedDict):
    menu_entry_tag: NotRequired[MenuEntryTag1OrStr]
    default_selected_flag: NotRequired[bool]
    output_format: OutputFormat2OrStr
    predefined_content: NotRequired[PredefinedContent | PredefinedContentDict]
    output_text: NotRequired[list[OutputText | OutputTextDict]]
    output_xhtml: NotRequired[str]
