from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.shareholder_type import ShareholderTypeOrStr
from .vias_address2 import ViasAddress2, ViasAddress2Dict
from .vias_name1 import ViasName1, ViasName1Dict
from .vias_personal_data1 import ViasPersonalData1, ViasPersonalData1Dict
from .vias_phone_number1 import ViasPhoneNumber1, ViasPhoneNumber1Dict


class ShareholderContact(SdkBaseModel):
    address: Optional[ViasAddress2] = UNSET
    """The address of the person."""

    email: Optional[str] = UNSET
    """The e-mail address of the person."""

    full_phone_number: Optional[str] = Field(default=UNSET, alias="fullPhoneNumber")
    """The phone number of the person provided as a single string. It will be handled as a landline phone. Examples:
    "0031 6 11 22 33 44", "+316/1122-3344", "(0031) 611223344"
    """

    job_title: Optional[str] = Field(default=UNSET, alias="jobTitle")
    """Job title of the person. Required when the ``shareholderType`` is **Controller**.

    Example values: **Chief Executive Officer**, **Chief Financial Officer**, **Chief Operating Officer**,
    **President**, **Vice President**, **Executive President**, **Managing Member**, **Partner**, **Treasurer**,
    **Director**, or **Other**."""

    name: Optional[ViasName1] = UNSET
    """The name of the person."""

    personal_data: Optional[ViasPersonalData1] = Field(default=UNSET, alias="personalData")
    """Contains information about the person."""

    phone_number: Optional[ViasPhoneNumber1] = Field(default=UNSET, alias="phoneNumber")
    """The phone number of the person."""

    shareholder_code: Optional[str] = Field(default=UNSET, alias="shareholderCode")
    """The unique identifier (UUID) of the shareholder entry. >**If, during an Account Holder create or update request,
    this field is left blank (but other fields provided), a new Shareholder will be created with a
    procedurally-generated UUID.**

    >**If, during an Account Holder create request, a UUID is provided, the creation of Account Holder will fail with a
    validation Error..**

    >**If, during an Account Holder update request, a UUID that is not correlated with an existing Shareholder is
    provided, the update of the Shareholder will fail.**

    >**If, during an Account Holder update request, a UUID that is correlated with an existing Shareholder is provided,
    the existing Shareholder will be updated.**"""

    shareholder_reference: Optional[str] = Field(default=UNSET, alias="shareholderReference")
    """Your reference for the shareholder entry."""

    shareholder_type: Optional[ShareholderTypeOrStr] = Field(default=UNSET, alias="shareholderType")
    """Specifies how the person is associated with the account holder.

    Possible values:

    * **Owner**: Individuals who directly or indirectly own 25% or more of a company.

    * **Controller**: Individuals who are members of senior management staff responsible for managing a company or
        organization."""

    web_address: Optional[str] = Field(default=UNSET, alias="webAddress")
    """The URL of the person's website."""


class ShareholderContactDict(TypedDict):
    address: NotRequired[ViasAddress2 | ViasAddress2Dict]
    email: NotRequired[str]
    full_phone_number: NotRequired[str]
    job_title: NotRequired[str]
    name: NotRequired[ViasName1 | ViasName1Dict]
    personal_data: NotRequired[ViasPersonalData1 | ViasPersonalData1Dict]
    phone_number: NotRequired[ViasPhoneNumber1 | ViasPhoneNumber1Dict]
    shareholder_code: NotRequired[str]
    shareholder_reference: NotRequired[str]
    shareholder_type: NotRequired[ShareholderTypeOrStr]
    web_address: NotRequired[str]
