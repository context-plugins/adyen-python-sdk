from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.type181 import Type181OrStr


class Target(SdkBaseModel):
    id: str
    """The unique identifier of the ``target.type``. This can be the ID of your:

    * balance platform
    * account holder
    * account holder's balance account"""

    type_: Type181OrStr = Field(alias="type")
    """The resource for which you want to receive notifications. Possible values:

    * **balancePlatform**: receive notifications about balance changes in your entire balance platform.

    * **accountHolder**: receive notifications about balance changes of a specific user.

    * **balanceAccount**: receive notifications about balance changes in a specific balance account."""


class TargetDict(TypedDict):
    id: str
    type_: Type181OrStr
