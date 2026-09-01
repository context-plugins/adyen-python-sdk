from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.status21 import Status21OrStr
from .terminal_reassignment_target2 import TerminalReassignmentTarget2, TerminalReassignmentTarget2Dict


class TerminalAssignment2(SdkBaseModel):
    """Indicates the account level to which the terminal is assigned, the `assignment status
    <https://docs.adyen.com/point-of-sale/automating-terminal-management/assign-terminals-api>`__, and where the
    terminals is in the process of being reassigned to."""

    company_id: str = Field(alias="companyId")
    """The unique identifier of the company account to which terminal is assigned."""

    merchant_id: Optional[str] = Field(default=UNSET, alias="merchantId")
    """The unique identifier of the merchant account to which terminal is assigned."""

    reassignment_target: Optional[TerminalReassignmentTarget2] = Field(default=UNSET, alias="reassignmentTarget")
    """Indicates where the terminal is in the process of being reassigned to."""

    status: Status21OrStr
    """The status of the reassignment. Possible values:
     * ``reassignmentInProgress``: the terminal was boarded and is now scheduled to remove the configuration. Wait for
            the terminal to synchronize with the Adyen platform.
     * ``deployed``: the terminal is deployed and reassigned.
     * ``inventory``: the terminal is in inventory and cannot process transactions.
     * ``boarded``: the terminal is boarded to a store, or a merchant account representing a store, and can process
            transactions."""

    store_id: Optional[str] = Field(default=UNSET, alias="storeId")
    """The unique identifier of the store to which terminal is assigned."""


class TerminalAssignment2Dict(TypedDict):
    company_id: str
    merchant_id: NotRequired[str]
    reassignment_target: NotRequired[TerminalReassignmentTarget2 | TerminalReassignmentTarget2Dict]
    status: Status21OrStr
    store_id: NotRequired[str]
