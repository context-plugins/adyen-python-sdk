from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Passcodes(SdkBaseModel):
    admin_menu_pin: Optional[str] = Field(default=UNSET, alias="adminMenuPin")
    """The passcode for the Admin menu and the Settings menu."""

    refund_pin: Optional[str] = Field(default=UNSET, alias="refundPin")
    """The passcode for referenced and unreferenced refunds on standalone terminals."""

    screen_lock_pin: Optional[str] = Field(default=UNSET, alias="screenLockPin")
    """The passcode to unlock the terminal screen after a timeout."""

    tx_menu_pin: Optional[str] = Field(default=UNSET, alias="txMenuPin")
    """The passcode for the Transactions menu."""


class PasscodesDict(TypedDict):
    admin_menu_pin: NotRequired[str]
    refund_pin: NotRequired[str]
    screen_lock_pin: NotRequired[str]
    tx_menu_pin: NotRequired[str]
