from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .field_type import FieldType, FieldTypeDict


class ErrorFieldType(SdkBaseModel):
    error_code: Optional[int] = Field(default=UNSET, alias="errorCode")
    """The validation error code."""

    error_description: Optional[str] = Field(default=UNSET, alias="errorDescription")
    """A description of the validation error."""

    field_type: Optional[FieldType] = Field(default=UNSET, alias="fieldType")
    """The type of error field."""


class ErrorFieldTypeDict(TypedDict):
    error_code: NotRequired[int]
    error_description: NotRequired[str]
    field_type: NotRequired[FieldType | FieldTypeDict]
