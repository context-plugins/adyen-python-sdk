from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .business_details1 import BusinessDetails1, BusinessDetails1Dict
from .enums.legal_arrangement_member import LegalArrangementMemberOrStr
from .enums.legal_entity_type import LegalEntityTypeOrStr
from .individual_details1 import IndividualDetails1, IndividualDetails1Dict
from .vias_address5 import ViasAddress5, ViasAddress5Dict
from .vias_phone_number2 import ViasPhoneNumber2, ViasPhoneNumber2Dict


class LegalArrangementEntityDetail(SdkBaseModel):
    address: Optional[ViasAddress5] = UNSET
    """The address of the entity."""

    business_details: Optional[BusinessDetails1] = Field(default=UNSET, alias="businessDetails")
    """Required when creating an entity with ``legalEntityType`` **Business**, **NonProfit**, **PublicCompany**, or
    **Partnership**."""

    email: Optional[str] = UNSET
    """The e-mail address of the entity."""

    full_phone_number: Optional[str] = Field(default=UNSET, alias="fullPhoneNumber")
    """The phone number of the contact provided as a single string. It will be handled as a landline phone.
    **Examples:** "0031 6 11 22 33 44", "+316/1122-3344", "(0031) 611223344"
    """

    individual_details: Optional[IndividualDetails1] = Field(default=UNSET, alias="individualDetails")
    """Required when creating an entity with ``legalEntityType`` **Individual**."""

    legal_arrangement_entity_code: Optional[str] = Field(default=UNSET, alias="legalArrangementEntityCode")
    """Adyen-generated unique alphanumeric identifier (UUID) for the entry, returned in the response when you create a
    legal arrangement entity. Use only when updating an account holder. If you include this field when creating an
    account holder, the request will fail."""

    legal_arrangement_entity_reference: Optional[str] = Field(default=UNSET, alias="legalArrangementEntityReference")
    """Your reference for the legal arrangement entity."""

    legal_arrangement_members: Optional[list[LegalArrangementMemberOrStr]] = Field(
        default=UNSET, alias="legalArrangementMembers"
    )
    """An array containing the roles of the entity in the legal arrangement.

    The possible values depend on the legal arrangement ``type``.

    - For ``type`` **Association**: **ControllingPerson** and **Shareholder**.

    - For ``type`` **Partnership**: **Partner** and **Shareholder**.

    - For ``type`` **Trust**: **Trustee**, **Settlor**, **Protector**, **Beneficiary**, and **Shareholder**."""

    legal_entity_type: Optional[LegalEntityTypeOrStr] = Field(default=UNSET, alias="legalEntityType")
    """The legal entity type.

    Possible values: **Business**, **Individual**, **NonProfit**, **PublicCompany**, or **Partnership**."""

    phone_number: Optional[ViasPhoneNumber2] = Field(default=UNSET, alias="phoneNumber")
    """The phone number of the entity."""

    web_address: Optional[str] = Field(default=UNSET, alias="webAddress")
    """The URL of the website of the contact."""


class LegalArrangementEntityDetailDict(TypedDict):
    address: NotRequired[ViasAddress5Dict]
    business_details: NotRequired[BusinessDetails1Dict]
    email: NotRequired[str]
    full_phone_number: NotRequired[str]
    individual_details: NotRequired[IndividualDetails1Dict]
    legal_arrangement_entity_code: NotRequired[str]
    legal_arrangement_entity_reference: NotRequired[str]
    legal_arrangement_members: NotRequired[list[LegalArrangementMemberOrStr]]
    legal_entity_type: NotRequired[LegalEntityTypeOrStr]
    phone_number: NotRequired[ViasPhoneNumber2Dict]
    web_address: NotRequired[str]
