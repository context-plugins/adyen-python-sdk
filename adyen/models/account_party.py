from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.party_role2 import PartyRole2OrStr
from .identity2 import Identity2, Identity2Dict


class AccountParty(SdkBaseModel):
    identity: Identity2
    """Contains the identity details of the party."""

    role: PartyRole2OrStr
    """Specifies a role or capacity of the party in relation to the bank account."""


class AccountPartyDict(TypedDict):
    identity: Identity2Dict
    role: PartyRole2OrStr
