from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.error_condition1 import ErrorCondition1OrStr
from .enums.result11 import Result11OrStr


class Response11(SdkBaseModel):
    """Result of a message request processing."""

    result: Result11OrStr = Field(alias="Result")
    """Result of the processing of the message. Possible values:
    * **Failure**
    * **Partial**
    * **Success**"""

    error_condition: Optional[ErrorCondition1OrStr] = Field(default=UNSET, alias="ErrorCondition")
    """Condition that has produced an error on the processing of a message request. Returned if Result is not Success.
    Possible values:
    * **Aborted**
    * **Busy**
    * **Cancel**
    * **DeviceOut**
    * **InProgress**
    * **InsertedCard**
    * **InvalidCard**
    * **LoggedOut**
    * **MessageFormat**
    * **NotAllowed**
    * **NotFound**
    * **PaymentRestriction**
    * **Refusal**
    * **UnavailableDevice**
    * **UnavailableService**
    * **UnreachableHost**
    * **WrongPIN**"""

    additional_response: Optional[str] = Field(default=UNSET, alias="AdditionalResponse")
    """Additional information related to processing status of a message request. If present, the POI logs it for further
    examination."""


class Response11Dict(TypedDict):
    result: Result11OrStr
    error_condition: NotRequired[ErrorCondition1OrStr]
    additional_response: NotRequired[str]
