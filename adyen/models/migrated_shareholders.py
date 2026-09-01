from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class MigratedShareholders(SdkBaseModel):
    legal_entity_code: Optional[str] = Field(default=UNSET, alias="legalEntityCode")
    """The unique identifier of the legal entity of that shareholder in the balance platform."""

    shareholder_code: Optional[str] = Field(default=UNSET, alias="shareholderCode")
    """The unique identifier of the account of the migrated shareholder in the classic integration."""


class MigratedShareholdersDict(TypedDict):
    legal_entity_code: NotRequired[str]
    shareholder_code: NotRequired[str]
