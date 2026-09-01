from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .attachment import Attachment, AttachmentDict
from .attachment1 import Attachment1, Attachment1Dict
from .enums.type84 import Type84OrStr
from .owner_entity2 import OwnerEntity2, OwnerEntity2Dict


class Document(SdkBaseModel):
    attachment: Optional[Attachment1] = UNSET
    """Object that contains the document."""

    attachments: Optional[list[Attachment]] = UNSET
    """Array that contains the document. The array supports multiple attachments for uploading different sides or pages
    of a document."""

    creation_date: Optional[RFC3339DateTime] = Field(default=UNSET, alias="creationDate")
    """The creation date of the document."""

    description: str
    """Your description for the document."""

    expiry_date: Optional[str] = Field(default=UNSET, alias="expiryDate")
    """The expiry date of the document, in YYYY-MM-DD format."""

    file_name: Optional[str] = Field(default=UNSET, alias="fileName")
    """The filename of the document."""

    id: Optional[str] = UNSET
    """The unique identifier of the document."""

    issuer_country: Optional[str] = Field(default=UNSET, alias="issuerCountry")
    """The two-character `ISO 3166-1 alpha-2 <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`__ country code where
    the document was issued. For example, **US**."""

    issuer_state: Optional[str] = Field(default=UNSET, alias="issuerState")
    """The state or province where the document was issued (AU only)."""

    modification_date: Optional[RFC3339DateTime] = Field(default=UNSET, alias="modificationDate")
    """The modification date of the document."""

    number: Optional[str] = UNSET
    """The number in the document."""

    owner: Optional[OwnerEntity2] = UNSET
    """Contains information about the resource that owns the document."""

    type_: Type84OrStr = Field(alias="type")
    """Type of document, used when providing an ID number or uploading a document. The possible values depend on the
    legal entity type.

    * For **organization**, the ``type`` values can be **proofOfAddress**, **registrationDocument**, **vatDocument**,
        **proofOfOrganizationTaxInfo**, **proofOfOwnership**, **proofOfIndustry**, **proofOfSignatory**,
        **proofOfDirector**, or **proofOfFundingOrWealthSource**.

    * For **individual**, the ``type`` values can be **identityCard**, **driversLicense**, **passport**, **liveSelfie**,
        **proofOfNationalIdNumber**, **proofOfResidency**, **proofOfIndustry**, **proofOfIndividualTaxId**,
        **proofOfFundingOrWealthSource** or **proofOfRelationship**.

    * For **soleProprietorship**, the ``type`` values can be **constitutionalDocument**, **proofOfAddress**, or
        **proofOfIndustry**.

    * For **trust**, the ``type`` value is **constitutionalDocument**.

    * For **unincorporatedPartnership**, the ``type`` value is **constitutionalDocument**.

    * Use **bankStatement** to upload documents for a `transfer instrument
        <https://docs.adyen.com/api-explorer/#/legalentity/latest/post/transferInstruments__resParam_id>`__."""


class DocumentDict(TypedDict):
    attachment: NotRequired[Attachment1 | Attachment1Dict]
    attachments: NotRequired[list[Attachment | AttachmentDict]]
    creation_date: NotRequired[RFC3339DateTime]
    description: str
    expiry_date: NotRequired[str]
    file_name: NotRequired[str]
    id: NotRequired[str]
    issuer_country: NotRequired[str]
    issuer_state: NotRequired[str]
    modification_date: NotRequired[RFC3339DateTime]
    number: NotRequired[str]
    owner: NotRequired[OwnerEntity2 | OwnerEntity2Dict]
    type_: Type84OrStr
