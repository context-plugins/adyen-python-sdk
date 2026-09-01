from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.state_type import StateTypeOrStr


class UpdateAccountHolderStateRequest(SdkBaseModel):
    account_holder_code: str = Field(alias="accountHolderCode")
    """The code of the Account Holder on which to update the state."""

    disable: bool
    """If true, disable the requested state. If false, enable the requested state."""

    reason: Optional[str] = UNSET
    """The reason that the state is being updated. >Required if the state is being disabled."""

    state_type: StateTypeOrStr = Field(alias="stateType")
    """The state to be updated. >Permitted values are: ``Processing``, ``Payout``"""


class UpdateAccountHolderStateRequestDict(TypedDict):
    account_holder_code: str
    disable: bool
    reason: NotRequired[str]
    state_type: StateTypeOrStr
