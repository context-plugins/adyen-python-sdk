from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class AccountHolderResource(SdkBaseModel):
    """All Of Resource, AccountHolderResource."""

    type_: Optional[str] = Field(default=UNSET, alias="type")
    account_holder_id: str = Field(alias="accountHolderId")
    """The unique identifier of the resource connected to the component. For `Platform Experience components
    <https://docs.adyen.com/platforms/build-user-dashboards>`__, this is the account holder linked to the balance
    account shown in the component."""


class AccountHolderResourceDict(TypedDict):
    type_: NotRequired[str]
    account_holder_id: str
