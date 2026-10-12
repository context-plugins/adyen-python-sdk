from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .capability_problem1 import CapabilityProblem1, CapabilityProblem1Dict


class VerificationErrors(SdkBaseModel):
    problems: Optional[list[CapabilityProblem1]] = UNSET
    """List of the verification errors."""


class VerificationErrorsDict(TypedDict):
    problems: NotRequired[list[CapabilityProblem1Dict]]
