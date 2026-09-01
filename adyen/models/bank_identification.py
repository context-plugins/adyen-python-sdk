from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.identification_type import IdentificationTypeOrStr


class BankIdentification(SdkBaseModel):
    country: Optional[str] = UNSET
    """Two-character `ISO 3166-1 alpha-2 <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`__ country code."""

    identification: Optional[str] = UNSET
    """The bank identification code."""

    identification_type: Optional[IdentificationTypeOrStr] = Field(default=UNSET, alias="identificationType")
    """The type of the identification.

    Possible values: **iban**, **routingNumber**, **sortCode**, **bic**."""


class BankIdentificationDict(TypedDict):
    country: NotRequired[str]
    identification: NotRequired[str]
    identification_type: NotRequired[IdentificationTypeOrStr]
