from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.field_name import FieldNameOrStr


class FieldType(SdkBaseModel):
    """The type of error field."""

    field: Optional[str] = UNSET
    """The full name of the property."""

    field_name: Optional[FieldNameOrStr] = Field(default=UNSET, alias="fieldName")
    """The type of the field."""

    shareholder_code: Optional[str] = Field(default=UNSET, alias="shareholderCode")
    """The code of the shareholder that the field belongs to. If empty, the field belongs to an account holder."""


class FieldTypeDict(TypedDict):
    field: NotRequired[str]
    field_name: NotRequired[FieldNameOrStr]
    shareholder_code: NotRequired[str]
