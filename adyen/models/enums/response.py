from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Response(str, Enum):
    """Indicates if the modification request has been received for processing."""

    CAPTURE_RECEIVED = "[capture-received]"
    CANCEL_RECEIVED = "[cancel-received]"
    REFUND_RECEIVED = "[refund-received]"
    CANCEL_OR_REFUND_RECEIVED = "[cancelOrRefund-received]"
    ADJUST_AUTHORISATION_RECEIVED = "[adjustAuthorisation-received]"
    DONATION_RECEIVED = "[donation-received]"
    TECHNICAL_CANCEL_RECEIVED = "[technical-cancel-received]"
    VOID_PENDING_REFUND_RECEIVED = "[voidPendingRefund-received]"
    AUTHORISED = "Authorised"
    REFUSED = "Refused"
    ERROR = "Error"

    __str__ = str.__str__


ResponseOrStr: TypeAlias = Annotated[Response | str, open_enum_validator(Response)]
