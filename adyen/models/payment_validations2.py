from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .name6 import Name6, Name6Dict


class PaymentValidations2(SdkBaseModel):
    """The object that you can use to enable payment validations for a transaction."""

    name: Optional[Name6] = UNSET


class PaymentValidations2Dict(TypedDict):
    name: NotRequired[Name6 | Name6Dict]
