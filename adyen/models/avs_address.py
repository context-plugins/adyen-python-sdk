from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class AvsAddress(SdkBaseModel):
    street_address: str = Field(alias="streetAddress")
    """The street and house number of the address.

    Example: 1 Infinite Loop, Cupertino."""

    zip: Optional[str] = UNSET
    """The zip or post code of the address.

    Example: CA 95014"""


class AvsAddressDict(TypedDict):
    street_address: str
    zip: NotRequired[str]
