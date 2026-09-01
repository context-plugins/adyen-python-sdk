from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type84(str, Enum):
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

    BANK_STATEMENT = "bankStatement"
    DRIVERS_LICENSE = "driversLicense"
    IDENTITY_CARD = "identityCard"
    NATIONAL_ID_NUMBER = "nationalIdNumber"
    PASSPORT = "passport"
    PROOF_OF_ADDRESS = "proofOfAddress"
    PROOF_OF_NATIONAL_ID_NUMBER = "proofOfNationalIdNumber"
    PROOF_OF_RESIDENCY = "proofOfResidency"
    REGISTRATION_DOCUMENT = "registrationDocument"
    VAT_DOCUMENT = "vatDocument"
    PROOF_OF_ORGANIZATION_TAX_INFO = "proofOfOrganizationTaxInfo"
    PROOF_OF_INDIVIDUAL_TAX_ID = "proofOfIndividualTaxId"
    PROOF_OF_OWNERSHIP = "proofOfOwnership"
    PROOF_OF_SIGNATORY = "proofOfSignatory"
    LIVE_SELFIE = "liveSelfie"
    PROOF_OF_INDUSTRY = "proofOfIndustry"
    CONSTITUTIONAL_DOCUMENT = "constitutionalDocument"
    PROOF_OF_FUNDING_OR_WEALTH_SOURCE = "proofOfFundingOrWealthSource"
    PROOF_OF_RELATIONSHIP = "proofOfRelationship"
    PROOF_OF_DIRECTOR = "proofOfDirector"

    __str__ = str.__str__


Type84OrStr: TypeAlias = Annotated[Type84 | str, open_enum_validator(Type84)]
