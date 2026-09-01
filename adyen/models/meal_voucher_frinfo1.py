from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class MealVoucherFrinfo1(SdkBaseModel):
    """Details to provide if ``type`` is **mealVoucher_FR**."""

    conecs_id: str = Field(alias="conecsId")
    """Meal Voucher conecsId. Format: digits only"""

    siret: str
    """Meal Voucher siret. Format: 14 digits."""

    sub_types: list[str] = Field(alias="subTypes")
    """The list of additional payment methods. Allowed values: **mealVoucher_FR_endenred**, **mealVoucher_FR_groupeup**,
    **mealVoucher_FR_natixis**, **mealVoucher_FR_sodexo**."""


class MealVoucherFrinfo1Dict(TypedDict):
    conecs_id: str
    siret: str
    sub_types: list[str]
