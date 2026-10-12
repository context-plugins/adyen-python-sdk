from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .patchable_amount_dto import PatchableAmountDto, PatchableAmountDtoDict


class Financier(SdkBaseModel):
    amount: PatchableAmountDto
    """The amount of the funds the financier provided."""

    first_name: str = Field(alias="firstName")
    """The financier's first name."""

    last_name: str = Field(alias="lastName")
    """The financier's last name."""

    location: str
    """The city and country/region where the financier is currently located. For example: Chicago, USA"""


class FinancierDict(TypedDict):
    amount: PatchableAmountDtoDict
    first_name: str
    last_name: str
    location: str
