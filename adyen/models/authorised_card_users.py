from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class AuthorisedCardUsers(SdkBaseModel):
    legal_entity_ids: Optional[list[str]] = Field(default=UNSET, alias="legalEntityIds")
    """The legal entity IDs of the authorized card users linked to the specified payment instrument."""


class AuthorisedCardUsersDict(TypedDict):
    legal_entity_ids: NotRequired[list[str]]
