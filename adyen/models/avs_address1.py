from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class AvsAddress1(SdkBaseModel):
    """Contains the billing address of the card holder. The address details need to be AVS-compliant, which means that
    you need to provide at least street address."""

    street_address: str = Field(alias="streetAddress")
    """The street and house number of the address.

    Example: 1 Infinite Loop, Cupertino."""

    zip: Optional[str] = UNSET
    """The zip or post code of the address.

    Example: CA 95014"""


class AvsAddress1Dict(TypedDict):
    street_address: str
    zip: NotRequired[str]
