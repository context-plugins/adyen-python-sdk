from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.capability import CapabilityOrStr
from .enums.type212 import Type212OrStr
from .remediating_action import RemediatingAction, RemediatingActionDict


class VerificationErrorRecursive(SdkBaseModel):
    capabilities: Optional[list[CapabilityOrStr]] = UNSET
    """Contains the capabilities that the verification error applies to."""

    code: Optional[str] = UNSET
    """The verification error code."""

    message: Optional[str] = UNSET
    """A description of the error."""

    type_: Optional[Type212OrStr] = Field(default=UNSET, alias="type")
    """The type of error.



    Possible values:
    * **invalidInput**
    * **dataMissing**
    * **pendingStatus**
    * **dataReview**"""

    remediating_actions: Optional[list[RemediatingAction]] = Field(default=UNSET, alias="remediatingActions")
    """Contains the actions that you can take to resolve the verification error."""


class VerificationErrorRecursiveDict(TypedDict):
    capabilities: NotRequired[list[CapabilityOrStr]]
    code: NotRequired[str]
    message: NotRequired[str]
    type_: NotRequired[Type212OrStr]
    remediating_actions: NotRequired[list[RemediatingActionDict]]
