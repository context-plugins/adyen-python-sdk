from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.status32 import Status32OrStr
from .enums.type211 import Type211OrStr
from .kyccheck_summary2 import KyccheckSummary2, KyccheckSummary2Dict


class KyccheckStatusData(SdkBaseModel):
    required_fields: Optional[list[str]] = Field(default=UNSET, alias="requiredFields")
    """A list of the fields required for execution of the check."""

    status: Status32OrStr
    """The status of the check.

    Possible values: **AWAITING_DATA** , **DATA_PROVIDED**, **FAILED**, **INVALID_DATA**, **PASSED**, **PENDING**,
    **RETRY_LIMIT_REACHED**."""

    summary: Optional[KyccheckSummary2] = UNSET
    """A summary of the execution of the check."""

    type_: Type211OrStr = Field(alias="type")
    """The type of check.

    Possible values:

     * **BANK_ACCOUNT_VERIFICATION**: Used in v5 and earlier. Replaced by **PAYOUT_METHOD_VERIFICATION** in v6 and
            later.

     * **COMPANY_VERIFICATION**

      * **CARD_VERIFICATION**

    * **IDENTITY_VERIFICATION**

    * **LEGAL_ARRANGEMENT_VERIFICATION**

    * **NONPROFIT_VERIFICATION**

     * **PASSPORT_VERIFICATION**

    * **PAYOUT_METHOD_VERIFICATION**: Used in v6 and later.

    * **PCI_VERIFICATION**"""


class KyccheckStatusDataDict(TypedDict):
    required_fields: NotRequired[list[str]]
    status: Status32OrStr
    summary: NotRequired[KyccheckSummary2Dict]
    type_: Type211OrStr
