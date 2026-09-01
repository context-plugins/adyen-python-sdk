from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.legal_form import LegalFormOrStr
from .enums.type110 import Type110OrStr
from .legal_arrangement_entity_detail import LegalArrangementEntityDetail, LegalArrangementEntityDetailDict
from .vias_address4 import ViasAddress4, ViasAddress4Dict


class LegalArrangementDetail(SdkBaseModel):
    address: ViasAddress4
    """The address of the legal arrangement."""

    legal_arrangement_code: Optional[str] = Field(default=UNSET, alias="legalArrangementCode")
    """Adyen-generated unique alphanumeric identifier (UUID) for the entry, returned in the response when you create a
    legal arrangement. Use only when updating an account holder. If you include this field when creating an account
    holder, the request will fail."""

    legal_arrangement_entities: Optional[list[LegalArrangementEntityDetail]] = Field(
        default=UNSET, alias="legalArrangementEntities"
    )
    """An array containing information about other entities that are part of the legal arrangement."""

    legal_arrangement_reference: Optional[str] = Field(default=UNSET, alias="legalArrangementReference")
    """Your reference for the legal arrangement. Must be between 3 to 128 characters."""

    legal_form: Optional[LegalFormOrStr] = Field(default=UNSET, alias="legalForm")
    """The form of legal arrangement. Required if ``type`` is **Trust** or **Partnership**.

    The possible values depend on the ``type``.

    - For ``type`` **Trust**: **CashManagementTrust**, **CorporateUnitTrust**, **DeceasedEstate**,
        **DiscretionaryInvestmentTrust**, **DiscretionaryServicesManagementTrust**, **DiscretionaryTradingTrust**,
        **FirstHomeSaverAccountsTrust**, **FixedTrust**, **FixedUnitTrust**, **HybridTrust**, **ListedPublicUnitTrust**,
        **OtherTrust**, **PooledSuperannuationTrust**, **PublicTradingTrust**, or **UnlistedPublicUnitTrust**.

    - For ``type`` **Partnership**: **LimitedPartnership**, **FamilyPartnership**, or **OtherPartnership**"""

    name: str
    """The legal name of the legal arrangement. Minimum length: 3 characters."""

    registration_number: Optional[str] = Field(default=UNSET, alias="registrationNumber")
    """The registration number of the legal arrangement."""

    tax_number: Optional[str] = Field(default=UNSET, alias="taxNumber")
    """The tax identification number of the legal arrangement."""

    type_: Type110OrStr = Field(alias="type")
    """The `type of legal arrangement
    <https://docs.adyen.com/classic-platforms/verification-process/legal-arrangements#types-of-legal-arrangements>`__.

    Possible values:

    - **Association**

    - **Partnership**

    - **SoleProprietorship**

    - **Trust**"""


class LegalArrangementDetailDict(TypedDict):
    address: ViasAddress4 | ViasAddress4Dict
    legal_arrangement_code: NotRequired[str]
    legal_arrangement_entities: NotRequired[list[LegalArrangementEntityDetail | LegalArrangementEntityDetailDict]]
    legal_arrangement_reference: NotRequired[str]
    legal_form: NotRequired[LegalFormOrStr]
    name: str
    registration_number: NotRequired[str]
    tax_number: NotRequired[str]
    type_: Type110OrStr
