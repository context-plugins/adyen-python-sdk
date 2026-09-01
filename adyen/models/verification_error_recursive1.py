from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.capability import CapabilityOrStr
from .enums.type512 import Type512OrStr
from .remediating_action import RemediatingAction, RemediatingActionDict


class VerificationErrorRecursive1(SdkBaseModel):
    capabilities: Optional[list[CapabilityOrStr]] = UNSET
    """Contains key-value pairs that specify the actions that the legal entity can do in your platform. The key is a
    capability required for your integration. For example, **issueCard** for Issuing.The value is an object containing
    the settings for the capability."""

    code: Optional[str] = UNSET
    """The general error code."""

    message: Optional[str] = UNSET
    """The general error message."""

    type_: Optional[Type512OrStr] = Field(default=UNSET, alias="type")
    """The type of error.

    Possible values:
    * **invalidInput**
    * **dataMissing**
    * **pendingStatus**
    * **rejected**
    * **dataReview**"""

    remediating_actions: Optional[list[RemediatingAction]] = Field(default=UNSET, alias="remediatingActions")
    """An object containing possible solutions to fix a verification error."""


class VerificationErrorRecursive1Dict(TypedDict):
    capabilities: NotRequired[list[CapabilityOrStr]]
    code: NotRequired[str]
    message: NotRequired[str]
    type_: NotRequired[Type512OrStr]
    remediating_actions: NotRequired[list[RemediatingAction | RemediatingActionDict]]
