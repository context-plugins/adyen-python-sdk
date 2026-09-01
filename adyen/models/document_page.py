from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.type91 import Type91OrStr


class DocumentPage(SdkBaseModel):
    page_name: Optional[str] = Field(default=UNSET, alias="pageName")
    page_number: Optional[int] = Field(default=UNSET, alias="pageNumber")
    type_: Optional[Type91OrStr] = Field(default=UNSET, alias="type")


class DocumentPageDict(TypedDict):
    page_name: NotRequired[str]
    page_number: NotRequired[int]
    type_: NotRequired[Type91OrStr]
