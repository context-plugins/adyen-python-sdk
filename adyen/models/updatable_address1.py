from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class UpdatableAddress1(SdkBaseModel):
    """The address of the store. It is not possible to update the country of the store."""

    city: Optional[str] = UNSET
    """The name of the city."""

    line1: Optional[str] = UNSET
    """The street address."""

    line2: Optional[str] = UNSET
    """Second address line."""

    line3: Optional[str] = UNSET
    """Third address line."""

    postal_code: Optional[str] = Field(default=UNSET, alias="postalCode")
    """The postal code."""

    state_or_province: Optional[str] = Field(default=UNSET, alias="stateOrProvince")
    """The state or province code as defined in `ISO 3166-2 <https://www.iso.org/standard/72483.html>`__. For example,
    **ON** for Ontario, Canada.

    Required for the following countries:
     - Australia
    - Brazil
    - Canada
    - India
    - Mexico
    - New Zealand
    - United States"""


class UpdatableAddress1Dict(TypedDict):
    city: NotRequired[str]
    line1: NotRequired[str]
    line2: NotRequired[str]
    line3: NotRequired[str]
    postal_code: NotRequired[str]
    state_or_province: NotRequired[str]
