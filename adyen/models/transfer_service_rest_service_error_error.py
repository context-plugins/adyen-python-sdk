from __future__ import annotations

from typing import Any

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .invalid_field import InvalidField, InvalidFieldDict
from .routing_details import RoutingDetails, RoutingDetailsDict


class TransferServiceRestServiceErrorError(SdkBaseModel):
    detail: str
    """A human-readable explanation specific to this occurrence of the problem."""

    error_code: str = Field(alias="errorCode")
    """A code that identifies the problem type."""

    instance: Optional[str] = UNSET
    """A unique URI that identifies the specific occurrence of the problem."""

    invalid_fields: Optional[list[InvalidField]] = Field(default=UNSET, alias="invalidFields")
    """Detailed explanation of each validation error, when applicable."""

    request_id: Optional[str] = Field(default=UNSET, alias="requestId")
    """A unique reference for the request, essentially the same as ``pspReference``."""

    response: Optional[Any] = UNSET
    """JSON response payload."""

    routing_details: Optional[list[RoutingDetails]] = Field(default=UNSET, alias="routingDetails")
    """Detailed explanation of each attempt to route the transfer with the priorities from the request."""

    status: int
    """The HTTP status code."""

    title: str
    """A short, human-readable summary of the problem type."""

    type_: str = Field(alias="type")
    """A URI that identifies the problem type, pointing to human-readable documentation on this problem type."""


class TransferServiceRestServiceErrorErrorDict(TypedDict):
    detail: str
    error_code: str
    instance: NotRequired[str]
    invalid_fields: NotRequired[list[InvalidFieldDict]]
    request_id: NotRequired[str]
    response: NotRequired[Any]
    routing_details: NotRequired[list[RoutingDetailsDict]]
    status: int
    title: str
    type_: str
