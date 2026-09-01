from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .patchable_amount_dto import PatchableAmountDto, PatchableAmountDtoDict


class PatchableTopUpAmount2(SdkBaseModel):
    """The currency and value to be added to the balance account, specified in minor units. This can be a fixed amount
    or a target amount."""

    fixed: OptionalNullable[PatchableAmountDto] = UNSET
    """The fixed amount with which you want to top up the balance account."""

    target: OptionalNullable[PatchableAmountDto] = UNSET
    """The target balance for the balance account that the top-up must achieve."""


class PatchableTopUpAmount2Dict(TypedDict):
    fixed: NotRequired[PatchableAmountDto | PatchableAmountDtoDict | None]
    target: NotRequired[PatchableAmountDto | PatchableAmountDtoDict | None]
