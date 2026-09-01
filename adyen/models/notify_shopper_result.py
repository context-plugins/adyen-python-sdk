from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class NotifyShopperResult(SdkBaseModel):
    displayed_reference: Optional[str] = Field(default=UNSET, alias="displayedReference")
    """Reference of Pre-debit notification that is displayed to the shopper"""

    message: Optional[str] = UNSET
    """A simple description of the ``resultCode``."""

    psp_reference: Optional[str] = Field(default=UNSET, alias="pspReference")
    """The unique reference that is associated with the request."""

    reference: Optional[str] = UNSET
    """Reference of Pre-debit notification sent in my the merchant"""

    result_code: Optional[str] = Field(default=UNSET, alias="resultCode")
    """The code indicating the status of notification."""

    shopper_notification_reference: Optional[str] = Field(default=UNSET, alias="shopperNotificationReference")
    """The unique reference for the request sent downstream."""

    stored_payment_method_id: Optional[str] = Field(default=UNSET, alias="storedPaymentMethodId")
    """This is the recurringDetailReference returned in the response when token was created"""


class NotifyShopperResultDict(TypedDict):
    displayed_reference: NotRequired[str]
    message: NotRequired[str]
    psp_reference: NotRequired[str]
    reference: NotRequired[str]
    result_code: NotRequired[str]
    shopper_notification_reference: NotRequired[str]
    stored_payment_method_id: NotRequired[str]
