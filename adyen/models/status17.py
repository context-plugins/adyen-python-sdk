from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .action1 import Action1, Action1Dict
from .enums.code import CodeOrStr


class Status17(SdkBaseModel):
    actions: Optional[list[Action1]] = UNSET
    """A list of actions that need to be completed to proceed with the grant."""

    code: CodeOrStr
    """The code for the status of the grant. Possible values:
    - **Pending**
    - **Active**
    - **Repaid**
    - **WrittenOff**
    - **Failed**
    - **Revoked**
    - **Requested**
    - **Reviewing**
    - **Approved**
    - **Rejected**
    - **Cancelled**"""


class Status17Dict(TypedDict):
    actions: NotRequired[list[Action1 | Action1Dict]]
    code: CodeOrStr
