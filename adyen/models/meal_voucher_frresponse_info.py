from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class MealVoucherFrresponseInfo(SdkBaseModel):
    conecs_id: Optional[str] = Field(default=UNSET, alias="conecsId")
    """Meal Voucher conecsId."""

    siret: Optional[str] = UNSET
    """Meal Voucher siret."""

    sub_types: Optional[list[str]] = Field(default=UNSET, alias="subTypes")
    """The list of additional payment methods."""


class MealVoucherFrresponseInfoDict(TypedDict):
    conecs_id: NotRequired[str]
    siret: NotRequired[str]
    sub_types: NotRequired[list[str]]
