from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .patchable_amount_dto import PatchableAmountDto, PatchableAmountDtoDict


class PatchableTopUpAmount(SdkBaseModel):
    fixed: OptionalNullable[PatchableAmountDto] = UNSET
    """The fixed amount with which you want to top up the balance account."""

    target: OptionalNullable[PatchableAmountDto] = UNSET
    """The target balance for the balance account that the top-up must achieve."""


class PatchableTopUpAmountDict(TypedDict):
    fixed: NotRequired[PatchableAmountDtoDict | None]
    target: NotRequired[PatchableAmountDtoDict | None]
