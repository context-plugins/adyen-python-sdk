from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .recurring_detail import RecurringDetail, RecurringDetailDict


class RecurringDetailWrapper(SdkBaseModel):
    recurring_detail: Optional[RecurringDetail] = Field(default=UNSET, alias="RecurringDetail")


class RecurringDetailWrapperDict(TypedDict):
    recurring_detail: NotRequired[RecurringDetail | RecurringDetailDict]
