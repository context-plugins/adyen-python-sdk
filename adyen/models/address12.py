from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Address12(SdkBaseModel):
    """The address of the bank account or card owner."""

    city: Optional[str] = UNSET
    r"""The name of the city.

    Supported characters: **[a-z] [A-Z] [0-9] . - — / # , ’ ° ( ) : ; [ ] & \ |** and Space.

    > Required when the ``category`` is **card**."""

    country: str
    """The two-character ISO 3166-1 alpha-2 country code. For example, **US**, **NL**, or **GB**."""

    line1: Optional[str] = UNSET
    r"""The first line of the street address.

    Supported characters: **[a-z] [A-Z] [0-9] . - — / # , ’ ° ( ) : ; [ ] & \ |** and Space.

    > Required when the ``category`` is **card**."""

    line2: Optional[str] = UNSET
    r"""The second line of the street address.

    Supported characters: **[a-z] [A-Z] [0-9] . - — / # , ’ ° ( ) : ; [ ] & \ |** and Space.

    > Required when the ``category`` is **card**."""

    postal_code: Optional[str] = Field(default=UNSET, alias="postalCode")
    """The postal code. Maximum length:
    * 5 digits for an address in the US.
    * 10 characters for an address in all other countries.

    Supported characters: **[a-z] [A-Z] [0-9]** and Space.

    > Required for addresses in the US."""

    state_or_province: Optional[str] = Field(default=UNSET, alias="stateOrProvince")
    """The two-letter ISO 3166-2 state or province code. For example, **CA** in the US or **ON** in Canada.

       > Required for the US and Canada."""


class Address12Dict(TypedDict):
    city: NotRequired[str]
    country: str
    line1: NotRequired[str]
    line2: NotRequired[str]
    postal_code: NotRequired[str]
    state_or_province: NotRequired[str]
