from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .item import Item, ItemDict
from .sub_input_detail import SubInputDetail, SubInputDetailDict


class InputDetail(SdkBaseModel):
    configuration: Optional[dict[str, str]] = UNSET
    """Configuration parameters for the required input."""

    details: Optional[list[SubInputDetail]] = UNSET
    """Input details can also be provided recursively."""

    input_details: Optional[list[SubInputDetail]] = Field(default=UNSET, alias="inputDetails")
    """Input details can also be provided recursively (deprecated)."""

    item_search_url: Optional[str] = Field(default=UNSET, alias="itemSearchUrl")
    """In case of a select, the URL from which to query the items."""

    items: Optional[list[Item]] = UNSET
    """In case of a select, the items to choose from."""

    key: Optional[str] = UNSET
    """The value to provide in the result."""

    optional: Optional[bool] = UNSET
    """True if this input value is optional."""

    type_: Optional[str] = Field(default=UNSET, alias="type")
    """The type of the required input."""

    value: Optional[str] = UNSET
    """The value can be pre-filled, if available."""


class InputDetailDict(TypedDict):
    configuration: NotRequired[dict[str, str]]
    details: NotRequired[list[SubInputDetailDict]]
    input_details: NotRequired[list[SubInputDetailDict]]
    item_search_url: NotRequired[str]
    items: NotRequired[list[ItemDict]]
    key: NotRequired[str]
    optional: NotRequired[bool]
    type_: NotRequired[str]
    value: NotRequired[str]
