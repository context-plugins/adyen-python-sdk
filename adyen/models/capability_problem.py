from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .capability_problem_entity2 import CapabilityProblemEntity2, CapabilityProblemEntity2Dict
from .verification_error import VerificationError, VerificationErrorDict


class CapabilityProblem(SdkBaseModel):
    entity: Optional[CapabilityProblemEntity2] = UNSET
    """Contains the type of the entity and the corresponding ID."""

    verification_errors: Optional[list[VerificationError]] = Field(default=UNSET, alias="verificationErrors")
    """Contains information about the verification error."""


class CapabilityProblemDict(TypedDict):
    entity: NotRequired[CapabilityProblemEntity2Dict]
    verification_errors: NotRequired[list[VerificationErrorDict]]
