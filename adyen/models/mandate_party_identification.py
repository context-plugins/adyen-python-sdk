from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class MandatePartyIdentification(SdkBaseModel):
    full_name: Optional[str] = Field(default=UNSET, alias="fullName")
    r"""The full name of the entity that owns the bank account.

    Supported characters: [a-z] [A-Z] [0-9] , . ; : - — / \ + & ! ? @ ( ) " ' and space."""


class MandatePartyIdentificationDict(TypedDict):
    full_name: NotRequired[str]
