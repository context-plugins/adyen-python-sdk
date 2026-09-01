from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.type181 import Type181OrStr


class TargetUpdate2(SdkBaseModel):
    """The type and ID of the resource about whose balance changes you want to be notified."""

    id: Optional[str] = UNSET
    """The unique identifier of the ``target.type``. This can be the ID of your:

    * balance platform
    * account holder
    * account holder's balance account"""

    type_: Optional[Type181OrStr] = Field(default=UNSET, alias="type")
    """The resource for which you want to receive notifications. Possible values:

    * **balancePlatform**: receive notifications about balance changes in your entire balance platform.

    * **accountHolder**: receive notifications about balance changes of a specific user.

    * **balanceAccount**: receive notifications about balance changes in a specific balance account."""


class TargetUpdate2Dict(TypedDict):
    id: NotRequired[str]
    type_: NotRequired[Type181OrStr]
