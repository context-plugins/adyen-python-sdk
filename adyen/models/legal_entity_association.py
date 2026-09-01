from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.type142 import Type142OrStr


class LegalEntityAssociation(SdkBaseModel):
    associator_id: Optional[str] = Field(default=UNSET, alias="associatorId")
    """The unique identifier of another legal entity with which the ``legalEntityId`` is associated. When the
    ``legalEntityId`` is associated to legal entities other than the current one, the response returns all the
    associations."""

    entity_type: Optional[str] = Field(default=UNSET, alias="entityType")
    """The legal entity type of associated legal entity.

    For example, **organization**, **soleProprietorship** or **individual**."""

    job_title: Optional[str] = Field(default=UNSET, alias="jobTitle")
    """The individual's job title if the ``type`` is **uboThroughControl** or **signatory**."""

    legal_entity_id: str = Field(alias="legalEntityId")
    """The unique identifier of the associated `legal entity
    <https://docs.adyen.com/api-explorer/legalentity/latest/post/legalEntities#responses-200-id>`__."""

    name: Optional[str] = UNSET
    """The name of the associated `legal entity
    <https://docs.adyen.com/api-explorer/legalentity/latest/post/legalEntities#responses-200-id>`__.

    - For **individual**, ``name.firstName`` and ``name.lastName``.
    - For **organization**, ``legalName``.
    - For **soleProprietorship**, ``name``."""

    nominee: Optional[bool] = UNSET
    """Default value: **false** Set to **true** if the entity association ``type`` **director**, **secondaryPartner** or
    **shareholder** is also a nominee. Only applicable to New Zealand."""

    relationship: Optional[str] = UNSET
    """The individual's relationship to a legal representative if the ``type`` is **legalRepresentative**. Possible
    values: **parent**, **guardian**."""

    settlor_exemption_reason: Optional[list[str]] = Field(default=UNSET, alias="settlorExemptionReason")
    """Defines the KYC exemption reason for a settlor associated with a trust. Only applicable to trusts in Australia.

    For example, **professionalServiceProvider**, **deceased**, or **contributionBelowThreshold**."""

    type_: Type142OrStr = Field(alias="type")
    """Defines the relationship of the legal entity to the current legal entity.

    Possible value for individuals: **legalRepresentative**.

    Possible values for organizations: **director**, **signatory**, **trustOwnership**, **uboThroughOwnership**,
    **uboThroughControl**, **ultimateParentCompany**, or **immediateParentCompany**.

    Possible values for sole proprietorships: **soleProprietorship**.

    Possible value for trusts: **trust**.

    Possible values for trust members: **definedBeneficiary**, **protector**, **secondaryTrustee**, **settlor**,
    **uboThroughControl**, or **uboThroughOwnership**.

    Possible value for unincorporated partnership: **unincorporatedPartnership**.

    Possible values for unincorporated partnership members: **secondaryPartner**, **uboThroughControl**,
    **uboThroughOwnership**"""


class LegalEntityAssociationDict(TypedDict):
    associator_id: NotRequired[str]
    entity_type: NotRequired[str]
    job_title: NotRequired[str]
    legal_entity_id: str
    name: NotRequired[str]
    nominee: NotRequired[bool]
    relationship: NotRequired[str]
    settlor_exemption_reason: NotRequired[list[str]]
    type_: Type142OrStr
