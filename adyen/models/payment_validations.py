from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .name6 import Name6, Name6Dict


class PaymentValidations(SdkBaseModel):
    name: Optional[Name6] = UNSET


class PaymentValidationsDict(TypedDict):
    name: NotRequired[Name6Dict]
