from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .amount import Amount, AmountDict


class CustomNotification1(SdkBaseModel):
    """Custom test notification object. Required when the
    https://docs.adyen.com/api-explorer/#/ManagementService/v1/post/companies/{companyId}/webhooks/{webhookId}/test__reqParam_types
    list contains **CUSTOM**."""

    amount: Optional[Amount] = UNSET
    """The amount of the payment that the notification is about. Set the value in `minor units
    <https://docs.adyen.com/development-resources/currency-codes>`__."""

    event_code: Optional[str] = Field(default=UNSET, alias="eventCode")
    """The event that caused the notification to be sent.Currently supported values:
    * **AUTHORISATION**
    * **CANCELLATION**
    * **REFUND**
    * **CAPTURE**
    * **REPORT_AVAILABLE**
    * **CHARGEBACK**
    * **REQUEST_FOR_INFORMATION**
    * **NOTIFICATION_OF_CHARGEBACK**
    * **NOTIFICATIONTEST**
    * **ORDER_OPENED**
    * **ORDER_CLOSED**
    * **CHARGEBACK_REVERSED**
    * **REFUNDED_REVERSED**
    * **REFUND_WITH_DATA**"""

    event_date: Optional[RFC3339DateTime] = Field(default=UNSET, alias="eventDate")
    """The time of the event. Format: `ISO 8601 <http://www.w3.org/TR/NOTE-datetime>`__, YYYY-MM-DDThh:mm:ssTZD."""

    merchant_reference: Optional[str] = Field(default=UNSET, alias="merchantReference")
    """Your reference for the custom test notification."""

    payment_method: Optional[str] = Field(default=UNSET, alias="paymentMethod")
    """The payment method for the payment that the notification is about. Possible values:
    * **amex**
    * **visa**
    * **mc**
    * **maestro**
    * **bcmc**
    * **paypal**
     * **sms**
     * **bankTransfer_NL**
    * **bankTransfer_DE**
    * **bankTransfer_BE**
    * **ideal**
    * **elv**
    * **sepadirectdebit**"""

    reason: Optional[str] = UNSET
    """A description of what caused the notification."""

    success: Optional[bool] = UNSET
    """The outcome of the event which the notification is about. Set to either **true** or **false**."""


class CustomNotification1Dict(TypedDict):
    amount: NotRequired[AmountDict]
    event_code: NotRequired[str]
    event_date: NotRequired[RFC3339DateTime]
    merchant_reference: NotRequired[str]
    payment_method: NotRequired[str]
    reason: NotRequired[str]
    success: NotRequired[bool]
