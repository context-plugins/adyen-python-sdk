from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type142(str, Enum):
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

    DEFINED_BENEFICIARY = "definedBeneficiary"
    DIRECTOR = "director"
    IMMEDIATE_PARENT_COMPANY = "immediateParentCompany"
    LEGAL_REPRESENTATIVE = "legalRepresentative"
    PCI_SIGNATORY = "pciSignatory"
    PROTECTOR = "protector"
    SECONDARY_PARTNER = "secondaryPartner"
    SECONDARY_TRUSTEE = "secondaryTrustee"
    SETTLOR = "settlor"
    SIGNATORY = "signatory"
    SOLE_PROPRIETORSHIP = "soleProprietorship"
    TRUST = "trust"
    TRUST_OWNERSHIP = "trustOwnership"
    UBO_THROUGH_CONTROL = "uboThroughControl"
    UBO_THROUGH_OWNERSHIP = "uboThroughOwnership"
    ULTIMATE_PARENT_COMPANY = "ultimateParentCompany"
    UNDEFINED_BENEFICIARY = "undefinedBeneficiary"
    UNINCORPORATED_PARTNERSHIP = "unincorporatedPartnership"

    __str__ = str.__str__


Type142OrStr: TypeAlias = Annotated[Type142 | str, open_enum_validator(Type142)]
