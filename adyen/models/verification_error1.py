from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.capability import CapabilityOrStr
from .enums.type512 import Type512OrStr
from .remediating_action import RemediatingAction, RemediatingActionDict
from .verification_error_recursive1 import VerificationErrorRecursive1, VerificationErrorRecursive1Dict


class VerificationError1(SdkBaseModel):
    capabilities: Optional[list[CapabilityOrStr]] = UNSET
    """Contains key-value pairs that specify the actions that the legal entity can do in your platform. The key is a
    capability required for your integration. For example, **issueCard** for Issuing.The value is an object containing
    the settings for the capability."""

    code: Optional[str] = UNSET
    """The general error code."""

    message: Optional[str] = UNSET
    """The general error message."""

    remediating_actions: Optional[list[RemediatingAction]] = Field(default=UNSET, alias="remediatingActions")
    """An object containing possible solutions to fix a verification error."""

    sub_errors: Optional[list[VerificationErrorRecursive1]] = Field(default=UNSET, alias="subErrors")
    """An array containing more granular information about the cause of the verification error."""

    type_: Optional[Type512OrStr] = Field(default=UNSET, alias="type")
    """The type of error.

    Possible values:
    * **invalidInput**
    * **dataMissing**
    * **pendingStatus**
    * **rejected**
    * **dataReview**"""


class VerificationError1Dict(TypedDict):
    capabilities: NotRequired[list[CapabilityOrStr]]
    code: NotRequired[str]
    message: NotRequired[str]
    remediating_actions: NotRequired[list[RemediatingAction | RemediatingActionDict]]
    sub_errors: NotRequired[list[VerificationErrorRecursive1 | VerificationErrorRecursive1Dict]]
    type_: NotRequired[Type512OrStr]
