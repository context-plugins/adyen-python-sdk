from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.type15 import Type15OrStr


class PersonalDocumentData(SdkBaseModel):
    expiration_date: Optional[str] = Field(default=UNSET, alias="expirationDate")
    """The expiry date of the document,
     in ISO-8601 YYYY-MM-DD format. For example, **2000-01-31**."""

    issuer_country: Optional[str] = Field(default=UNSET, alias="issuerCountry")
    """The country where the document was issued, in the two-character `ISO 3166-1 alpha-2
    <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`__ format. For example, **NL**."""

    issuer_state: Optional[str] = Field(default=UNSET, alias="issuerState")
    """The state where the document was issued (if applicable)."""

    number: Optional[str] = UNSET
    """The number in the document."""

    type_: Type15OrStr = Field(alias="type")
    """The type of the document. Possible values: **ID**, **DRIVINGLICENSE**, **PASSPORT**, **SOCIALSECURITY**,
    **VISA**.

    To delete an existing entry for a document ``type``, send only the ``type`` field in your request."""


class PersonalDocumentDataDict(TypedDict):
    expiration_date: NotRequired[str]
    issuer_country: NotRequired[str]
    issuer_state: NotRequired[str]
    number: NotRequired[str]
    type_: Type15OrStr
