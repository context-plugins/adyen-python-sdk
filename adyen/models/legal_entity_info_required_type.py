from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.type213 import Type213OrStr
from .individual1 import Individual1, Individual1Dict
from .legal_entity_association import LegalEntityAssociation, LegalEntityAssociationDict
from .legal_entity_capability import LegalEntityCapability, LegalEntityCapabilityDict
from .organization1 import Organization1, Organization1Dict
from .sole_proprietorship1 import SoleProprietorship1, SoleProprietorship1Dict
from .trust1 import Trust1, Trust1Dict
from .unincorporated_partnership1 import UnincorporatedPartnership1, UnincorporatedPartnership1Dict


class LegalEntityInfoRequiredType(SdkBaseModel):
    capabilities: Optional[dict[str, LegalEntityCapability]] = UNSET
    """Contains key-value pairs that specify the actions that the legal entity can do in your platform.The key is a
    capability required for your integration. For example, **issueCard** for Issuing. The value is an object containing
    the settings for the capability."""

    entity_associations: Optional[list[LegalEntityAssociation]] = Field(default=UNSET, alias="entityAssociations")
    """List of legal entities associated with the current legal entity. For example, ultimate beneficial owners
    associated with an organization through ownership or control, or as signatories."""

    individual: Optional[Individual1] = UNSET
    """Information about the individual. Required if ``type`` is **individual**."""

    organization: Optional[Organization1] = UNSET
    """Information about the organization. Required if ``type`` is **organization**."""

    reference: Optional[str] = UNSET
    """Your reference for the legal entity, maximum 150 characters."""

    sole_proprietorship: Optional[SoleProprietorship1] = Field(default=UNSET, alias="soleProprietorship")
    """Information about the sole proprietorship. Required if ``type`` is **soleProprietorship**."""

    trust: Optional[Trust1] = UNSET
    """Information about the trust. Required if ``type`` is **trust**."""

    type_: Type213OrStr = Field(alias="type")
    """The type of legal entity.

     Possible values: **individual**, **organization**, **soleProprietorship**, or **trust**."""

    unincorporated_partnership: Optional[UnincorporatedPartnership1] = Field(
        default=UNSET, alias="unincorporatedPartnership"
    )
    """Information about the unincorporated partnership. Required if ``type`` is **unincorporatedPartnership**."""

    verification_plan: Optional[str] = Field(default=UNSET, alias="verificationPlan")
    """A key-value pair that specifies the verification process for a legal entity. Set to **upfront** for upfront
    verification for `marketplaces
    <https://docs.adyen.com/marketplaces/verification-overview/verification-types/#upfront-verification>`__."""


class LegalEntityInfoRequiredTypeDict(TypedDict):
    capabilities: NotRequired[dict[str, LegalEntityCapability | LegalEntityCapabilityDict]]
    entity_associations: NotRequired[list[LegalEntityAssociation | LegalEntityAssociationDict]]
    individual: NotRequired[Individual1 | Individual1Dict]
    organization: NotRequired[Organization1 | Organization1Dict]
    reference: NotRequired[str]
    sole_proprietorship: NotRequired[SoleProprietorship1 | SoleProprietorship1Dict]
    trust: NotRequired[Trust1 | Trust1Dict]
    type_: Type213OrStr
    unincorporated_partnership: NotRequired[UnincorporatedPartnership1 | UnincorporatedPartnership1Dict]
    verification_plan: NotRequired[str]
