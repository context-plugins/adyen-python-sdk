from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class PaymentsAppDto(SdkBaseModel):
    installation_id: str = Field(alias="installationId")
    """The unique identifier of the Payments App instance."""

    merchant_account_code: str = Field(alias="merchantAccountCode")
    """The account code associated with the Payments App instance."""

    merchant_store_code: Optional[str] = Field(default=UNSET, alias="merchantStoreCode")
    """The store code associated with the Payments App instance."""

    status: str
    """The status of the Payments App instance."""


class PaymentsAppDtoDict(TypedDict):
    installation_id: str
    merchant_account_code: str
    merchant_store_code: NotRequired[str]
    status: str
