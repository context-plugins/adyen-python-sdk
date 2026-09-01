from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .store1 import Store1, Store1Dict


class GetStoresUnderAccountResponse(SdkBaseModel):
    stores: Optional[list[Store1]] = UNSET
    """Array that returns a list of all stores for the specified merchant account, or for all merchant accounts under
    the company account."""


class GetStoresUnderAccountResponseDict(TypedDict):
    stores: NotRequired[list[Store1 | Store1Dict]]
