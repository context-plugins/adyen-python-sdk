from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .capability_problem1 import CapabilityProblem1, CapabilityProblem1Dict
from .document_reference import DocumentReference, DocumentReferenceDict
from .enums.type182 import Type182OrStr
from .individual1 import Individual1, Individual1Dict
from .legal_entity_association import LegalEntityAssociation, LegalEntityAssociationDict
from .legal_entity_capability import LegalEntityCapability, LegalEntityCapabilityDict
from .organization1 import Organization1, Organization1Dict
from .sole_proprietorship1 import SoleProprietorship1, SoleProprietorship1Dict
from .transfer_instrument_reference import TransferInstrumentReference, TransferInstrumentReferenceDict
from .trust1 import Trust1, Trust1Dict
from .unincorporated_partnership1 import UnincorporatedPartnership1, UnincorporatedPartnership1Dict
from .upload_android_app_response import UploadAndroidAppResponse, UploadAndroidAppResponseDict
from .verification_deadline import VerificationDeadline, VerificationDeadlineDict


class LegalEntity3(SdkBaseModel):
    capabilities: Optional[dict[str, LegalEntityCapability]] = UNSET
    """Contains key-value pairs that specify the actions that the legal entity can do in your platform.The key is a
    capability required for your integration. For example, **issueCard** for Issuing. The value is an object containing
    the settings for the capability."""

    document_details: Optional[list[DocumentReference]] = Field(default=UNSET, alias="documentDetails")
    """List of documents uploaded for the legal entity."""

    documents: Optional[list[UploadAndroidAppResponse]] = UNSET
    """List of documents uploaded for the legal entity."""

    entity_associations: Optional[list[LegalEntityAssociation]] = Field(default=UNSET, alias="entityAssociations")
    """List of legal entities associated with the current legal entity. For example, ultimate beneficial owners
    associated with an organization through ownership or control, or as signatories."""

    id: str
    """The unique identifier of the legal entity."""

    individual: Optional[Individual1] = UNSET
    """Information about the individual. Required if ``type`` is **individual**."""

    organization: Optional[Organization1] = UNSET
    """Information about the organization. Required if ``type`` is **organization**."""

    problems: Optional[list[CapabilityProblem1]] = UNSET
    """List of verification errors related to capabilities for the legal entity."""

    reference: Optional[str] = UNSET
    """Your reference for the legal entity, maximum 150 characters."""

    sole_proprietorship: Optional[SoleProprietorship1] = Field(default=UNSET, alias="soleProprietorship")
    """Information about the sole proprietorship. Required if ``type`` is **soleProprietorship**."""

    transfer_instruments: Optional[list[TransferInstrumentReference]] = Field(
        default=UNSET, alias="transferInstruments"
    )
    """List of transfer instruments that the legal entity owns."""

    trust: Optional[Trust1] = UNSET
    """Information about the trust. Required if ``type`` is **trust**."""

    type_: Optional[Type182OrStr] = Field(default=UNSET, alias="type")
    """The type of legal entity.

    Possible values: **individual**, **organization**, **soleProprietorship**, or **trust**."""

    unincorporated_partnership: Optional[UnincorporatedPartnership1] = Field(
        default=UNSET, alias="unincorporatedPartnership"
    )
    """Information about the unincorporated partnership. Required if ``type`` is **unincorporatedPartnership**."""

    verification_deadlines: Optional[list[VerificationDeadline]] = Field(default=UNSET, alias="verificationDeadlines")
    """List of verification deadlines and the capabilities that will be disallowed if verification errors are not
    resolved."""

    verification_plan: Optional[str] = Field(default=UNSET, alias="verificationPlan")
    """A key-value pair that specifies the verification process for a legal entity. Set to **upfront** for upfront
    verification for `marketplaces
    <https://docs.adyen.com/marketplaces/verification-overview/verification-types/#upfront-verification>`__."""


class LegalEntity3Dict(TypedDict):
    capabilities: NotRequired[dict[str, LegalEntityCapabilityDict]]
    document_details: NotRequired[list[DocumentReferenceDict]]
    documents: NotRequired[list[UploadAndroidAppResponseDict]]
    entity_associations: NotRequired[list[LegalEntityAssociationDict]]
    id: str
    individual: NotRequired[Individual1Dict]
    organization: NotRequired[Organization1Dict]
    problems: NotRequired[list[CapabilityProblem1Dict]]
    reference: NotRequired[str]
    sole_proprietorship: NotRequired[SoleProprietorship1Dict]
    transfer_instruments: NotRequired[list[TransferInstrumentReferenceDict]]
    trust: NotRequired[Trust1Dict]
    type_: NotRequired[Type182OrStr]
    unincorporated_partnership: NotRequired[UnincorporatedPartnership1Dict]
    verification_deadlines: NotRequired[list[VerificationDeadlineDict]]
    verification_plan: NotRequired[str]
