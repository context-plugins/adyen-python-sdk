from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CollectInformation1(SdkBaseModel):
    """Contains indicators whether the page should only collect information for specific `KYC checks
    <https://docs.adyen.com/classic-platforms/verification-checks>`__. By default, the page collects information for all
    KYC checks that apply to the `legal entity type
    <https://docs.adyen.com/classic-platforms/account-holders-and-accounts#legal-entity-types>`__."""

    bank_details: Optional[bool] = Field(default=UNSET, alias="bankDetails")
    """Indicates whether `bank account details
    <https://docs.adyen.com/classic-platforms/verification-process/accepted-data-format/#bank-accounts>`__ must be
    collected. Default is **true**."""

    business_details: Optional[bool] = Field(default=UNSET, alias="businessDetails")
    """Indicates whether `business details
    <https://docs.adyen.com/classic-platforms/verification-process/accepted-data-format/#organizations>`__ must be
    collected. Default is **true**."""

    individual_details: Optional[bool] = Field(default=UNSET, alias="individualDetails")
    """Indicates whether `individual details
    <https://docs.adyen.com/classic-platforms/verification-process/accepted-data-format/#individuals>`__ must be
    collected. Default is **true**."""

    legal_arrangement_details: Optional[bool] = Field(default=UNSET, alias="legalArrangementDetails")
    """Indicates whether `legal arrangement details
    <https://docs.adyen.com/classic-platforms/verification-checks/legal-arrangements>`__ must be collected. Default is
    **true**."""

    pci_questionnaire: Optional[bool] = Field(default=UNSET, alias="pciQuestionnaire")
    """Indicates whether answers to a `PCI questionnaire
    <https://docs.adyen.com/classic-platforms/platforms-for-partners#onboard-partner-platform>`__ must be collected.
    Applies only to partner platforms. Default is **true**."""

    shareholder_details: Optional[bool] = Field(default=UNSET, alias="shareholderDetails")
    """Indicates whether `shareholder details
    <https://docs.adyen.com/classic-platforms/verification-process/accepted-data-format/#individuals>`__ must be
    collected. Defaults to **true**."""


class CollectInformation1Dict(TypedDict):
    bank_details: NotRequired[bool]
    business_details: NotRequired[bool]
    individual_details: NotRequired[bool]
    legal_arrangement_details: NotRequired[bool]
    pci_questionnaire: NotRequired[bool]
    shareholder_details: NotRequired[bool]
