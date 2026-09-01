from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Opi(SdkBaseModel):
    enable_pay_at_table: Optional[bool] = Field(default=UNSET, alias="enablePayAtTable")
    """Indicates if Pay at table is enabled."""

    pay_at_table_store_number: Optional[str] = Field(default=UNSET, alias="payAtTableStoreNumber")
    """The store number to use for Pay at Table."""

    pay_at_table_url: Optional[str] = Field(default=UNSET, alias="payAtTableURL")
    """The URL and port number used for Pay at Table communication."""


class OpiDict(TypedDict):
    enable_pay_at_table: NotRequired[bool]
    pay_at_table_store_number: NotRequired[str]
    pay_at_table_url: NotRequired[str]
