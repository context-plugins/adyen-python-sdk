from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .item import Item, ItemDict


class SubInputDetail(SdkBaseModel):
    configuration: Optional[dict[str, str]] = UNSET
    """Configuration parameters for the required input."""

    items: Optional[list[Item]] = UNSET
    """In case of a select, the items to choose from."""

    key: Optional[str] = UNSET
    """The value to provide in the result."""

    optional: Optional[bool] = UNSET
    """True if this input is optional to provide."""

    type_: Optional[str] = Field(default=UNSET, alias="type")
    """The type of the required input."""

    value: Optional[str] = UNSET
    """The value can be pre-filled, if available."""


class SubInputDetailDict(TypedDict):
    configuration: NotRequired[dict[str, str]]
    items: NotRequired[list[Item | ItemDict]]
    key: NotRequired[str]
    optional: NotRequired[bool]
    type_: NotRequired[str]
    value: NotRequired[str]
