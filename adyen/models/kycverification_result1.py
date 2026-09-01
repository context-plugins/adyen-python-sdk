from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .kyccheck_result2 import KyccheckResult2, KyccheckResult2Dict
from .kyclegal_arrangement_check_result import KyclegalArrangementCheckResult, KyclegalArrangementCheckResultDict
from .kyclegal_arrangement_entity_check_result import (
    KyclegalArrangementEntityCheckResult,
    KyclegalArrangementEntityCheckResultDict,
)
from .kycpayout_method_check_result import KycpayoutMethodCheckResult, KycpayoutMethodCheckResultDict
from .kycshareholder_check_result import KycshareholderCheckResult, KycshareholderCheckResultDict
from .kycsignatory_check_result import KycsignatoryCheckResult, KycsignatoryCheckResultDict
from .kycultimate_parent_company_check_result import (
    KycultimateParentCompanyCheckResult,
    KycultimateParentCompanyCheckResultDict,
)


class KycverificationResult1(SdkBaseModel):
    """The details of KYC Verification of the account holder."""

    account_holder: Optional[KyccheckResult2] = Field(default=UNSET, alias="accountHolder")
    """The results of the checks on the account holder."""

    legal_arrangements: Optional[list[KyclegalArrangementCheckResult]] = Field(default=UNSET, alias="legalArrangements")
    """The results of the checks on the legal arrangements."""

    legal_arrangements_entities: Optional[list[KyclegalArrangementEntityCheckResult]] = Field(
        default=UNSET, alias="legalArrangementsEntities"
    )
    """The results of the checks on the legal arrangement entities."""

    payout_methods: Optional[list[KycpayoutMethodCheckResult]] = Field(default=UNSET, alias="payoutMethods")
    """The results of the checks on the payout methods."""

    shareholders: Optional[list[KycshareholderCheckResult]] = UNSET
    """The results of the checks on the shareholders."""

    signatories: Optional[list[KycsignatoryCheckResult]] = UNSET
    """The results of the checks on the signatories."""

    ultimate_parent_company: Optional[list[KycultimateParentCompanyCheckResult]] = Field(
        default=UNSET, alias="ultimateParentCompany"
    )
    """The result of the check on the Ultimate Parent Company."""


class KycverificationResult1Dict(TypedDict):
    account_holder: NotRequired[KyccheckResult2 | KyccheckResult2Dict]
    legal_arrangements: NotRequired[list[KyclegalArrangementCheckResult | KyclegalArrangementCheckResultDict]]
    legal_arrangements_entities: NotRequired[
        list[KyclegalArrangementEntityCheckResult | KyclegalArrangementEntityCheckResultDict]
    ]
    payout_methods: NotRequired[list[KycpayoutMethodCheckResult | KycpayoutMethodCheckResultDict]]
    shareholders: NotRequired[list[KycshareholderCheckResult | KycshareholderCheckResultDict]]
    signatories: NotRequired[list[KycsignatoryCheckResult | KycsignatoryCheckResultDict]]
    ultimate_parent_company: NotRequired[
        list[KycultimateParentCompanyCheckResult | KycultimateParentCompanyCheckResultDict]
    ]
