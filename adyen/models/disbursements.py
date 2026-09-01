from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .disbursement import Disbursement, DisbursementDict


class Disbursements(SdkBaseModel):
    disbursements: list[Disbursement]
    """Contains a list of all disbursements related to the specified grant."""


class DisbursementsDict(TypedDict):
    disbursements: list[Disbursement | DisbursementDict]
