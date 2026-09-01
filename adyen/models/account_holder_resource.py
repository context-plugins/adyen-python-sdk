from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel


class AccountHolderResource(SdkBaseModel):
    """All Of Resource, AccountHolderResource."""

    type_: Literal["accountHolder"] = Field(default="accountHolder", alias="type")

    account_holder_id: str = Field(alias="accountHolderId")
    """The unique identifier of the resource connected to the component. For `Platform Experience components
    <https://docs.adyen.com/platforms/build-user-dashboards>`__, this is the account holder linked to the balance
    account shown in the component."""


class AccountHolderResourceDict(TypedDict):
    type_: NotRequired[Literal["accountHolder"]]
    account_holder_id: str
