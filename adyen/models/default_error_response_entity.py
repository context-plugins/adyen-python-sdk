from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .invalid_field import InvalidField, InvalidFieldDict


class DefaultErrorResponseEntity(SdkBaseModel):
    """Standardized error response following RFC-7807 format"""

    detail: Optional[str] = UNSET
    """A human-readable explanation specific to this occurrence of the problem."""

    error_code: Optional[str] = Field(default=UNSET, alias="errorCode")
    """Unique business error code."""

    instance: Optional[str] = UNSET
    """A URI that identifies the specific occurrence of the problem if applicable."""

    invalid_fields: Optional[list[InvalidField]] = Field(default=UNSET, alias="invalidFields")
    """Array of fields with validation errors when applicable."""

    request_id: Optional[str] = Field(default=UNSET, alias="requestId")
    """The unique reference for the request."""

    status: Optional[int] = UNSET
    """The HTTP status code."""

    title: Optional[str] = UNSET
    """A short, human-readable summary of the problem type."""

    type_: Optional[str] = Field(default=UNSET, alias="type")
    """A URI that identifies the validation error type. It points to human-readable documentation for the problem
    type."""


class DefaultErrorResponseEntityDict(TypedDict):
    detail: NotRequired[str]
    error_code: NotRequired[str]
    instance: NotRequired[str]
    invalid_fields: NotRequired[list[InvalidField | InvalidFieldDict]]
    request_id: NotRequired[str]
    status: NotRequired[int]
    title: NotRequired[str]
    type_: NotRequired[str]
