from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class MigratedStores(SdkBaseModel):
    business_line_id: Optional[str] = Field(default=UNSET, alias="businessLineId")
    """The unique identifier of the business line associated with the migrated account holder in the balance
    platform."""

    store_code: Optional[str] = Field(default=UNSET, alias="storeCode")
    """The unique identifier of the store associated with the migrated account holder in the classic integration."""

    store_id: Optional[str] = Field(default=UNSET, alias="storeId")
    """The unique identifier of the store associated with the migrated account holder in the balance platform."""

    store_reference: Optional[str] = Field(default=UNSET, alias="storeReference")
    """Your reference for the store in the classic integration. The `Customer Area <https://ca-test.adyen.com/>`__ uses
    this value for the store description."""


class MigratedStoresDict(TypedDict):
    business_line_id: NotRequired[str]
    store_code: NotRequired[str]
    store_id: NotRequired[str]
    store_reference: NotRequired[str]
