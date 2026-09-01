from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class UndefinedBeneficiary(SdkBaseModel):
    description: Optional[str] = UNSET
    """The details of the undefined beneficiary."""

    reference: Optional[str] = UNSET
    """The reference of the undefined beneficiary."""


class UndefinedBeneficiaryDict(TypedDict):
    description: NotRequired[str]
    reference: NotRequired[str]
