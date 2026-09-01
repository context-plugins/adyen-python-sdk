from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .disbursement_repayment_info_update2 import DisbursementRepaymentInfoUpdate2, DisbursementRepaymentInfoUpdate2Dict


class DisbursementInfoUpdate(SdkBaseModel):
    repayment: Optional[DisbursementRepaymentInfoUpdate2] = UNSET
    """Contains information about the basis points configured for repaying the disbursement."""


class DisbursementInfoUpdateDict(TypedDict):
    repayment: NotRequired[DisbursementRepaymentInfoUpdate2 | DisbursementRepaymentInfoUpdate2Dict]
