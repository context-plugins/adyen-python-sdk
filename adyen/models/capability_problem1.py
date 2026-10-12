from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .capability_problem_entity1 import CapabilityProblemEntity1, CapabilityProblemEntity1Dict
from .verification_error1 import VerificationError1, VerificationError1Dict


class CapabilityProblem1(SdkBaseModel):
    entity: Optional[CapabilityProblemEntity1] = UNSET
    verification_errors: Optional[list[VerificationError1]] = Field(default=UNSET, alias="verificationErrors")


class CapabilityProblem1Dict(TypedDict):
    entity: NotRequired[CapabilityProblemEntity1Dict]
    verification_errors: NotRequired[list[VerificationError1Dict]]
