from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, SdkBaseModel
from .address12 import Address12, Address12Dict
from .enums.type112 import Type112, Type112OrStr


class PartyIdentification(SdkBaseModel):
    address: Optional[Address12] = UNSET
    """The address of the bank account or card owner."""

    date_of_birth: Optional[Date] = Field(default=UNSET, alias="dateOfBirth")
    """The date of birth of the individual in `ISO-8601 <https://www.w3.org/TR/NOTE-datetime>`__ format. For example,
    **YYYY-MM-DD**.

    Allowed only when ``type`` is **individual**."""

    email: Optional[str] = UNSET
    """The email address of the organization or individual. Maximum length: 254 characters."""

    first_name: Optional[str] = Field(default=UNSET, alias="firstName")
    """The first name of the individual.

    Supported characters: [a-z] [A-Z] - . / — and space.

    This parameter is:
    - Allowed only when ``type`` is **individual**.
    - Required when ``category`` is **card**."""

    full_name: Optional[str] = Field(default=UNSET, alias="fullName")
    r"""The full name of the entity that owns the bank account or card.

    Supported characters: [a-z] [A-Z] [0-9] , . ; : - — / \ + & ! ? @ ( ) " ' and space.

    Required when ``category`` is **bank**."""

    last_name: Optional[str] = Field(default=UNSET, alias="lastName")
    """The last name of the individual.

    Supported characters: [a-z] [A-Z] - . / — and space.

    This parameter is:
    - Allowed only when ``type`` is **individual**.
    - Required when ``category`` is **card**."""

    reference: Optional[str] = UNSET
    """A unique reference to identify the party or counterparty involved in the transfer. For example, your client's
    unique wallet or payee ID.

    Required when you include ``cardIdentification.storedPaymentMethodId``."""

    type_: Type112OrStr = Field(default=Type112.UNKNOWN, alias="type")
    """The type of entity that owns the bank account or card.

    Possible values: **individual**, **organization**, or **unknown**.

    Required when ``category`` is **card**. In this case, the value must be **individual**."""

    url: Optional[str] = UNSET
    """The URL of the organization or individual. Maximum length: 255 characters."""


class PartyIdentificationDict(TypedDict):
    address: NotRequired[Address12Dict]
    date_of_birth: NotRequired[Date]
    email: NotRequired[str]
    first_name: NotRequired[str]
    full_name: NotRequired[str]
    last_name: NotRequired[str]
    reference: NotRequired[str]
    type_: NotRequired[Type112OrStr]
    url: NotRequired[str]
