from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .custom_notification1 import CustomNotification1, CustomNotification1Dict


class TestCompanyWebhookRequest(SdkBaseModel):
    merchant_ids: Optional[list[str]] = Field(default=UNSET, alias="merchantIds")
    """List of ``merchantId`` values for which test webhooks will be sent. The list can have a maximum of 20
    ``merchantId`` values.

    If not specified, we send sample notifications to all the merchant accounts that the webhook is configured for. If
    this is more than 20 merchant accounts, use this list to specify a subset of the merchant accounts for which to send
    test notifications."""

    notification: Optional[CustomNotification1] = UNSET
    """Custom test notification object. Required when the
    https://docs.adyen.com/api-explorer/#/ManagementService/v1/post/companies/{companyId}/webhooks/{webhookId}/test__reqParam_types
    list contains **CUSTOM**."""

    types: Optional[list[str]] = UNSET
    """List of event codes for which to send test notifications. Only the webhook types below are supported.

    Possible values if webhook ``type``: **standard**:

    * **AUTHORISATION**
    * **CHARGEBACK_REVERSED**
    * **ORDER_CLOSED**
    * **ORDER_OPENED**
    * **PAIDOUT_REVERSED**
    * **PAYOUT_THIRDPARTY**
    * **REFUNDED_REVERSED**
    * **REFUND_WITH_DATA**
    * **REPORT_AVAILABLE**
    * **CUSTOM** - set your custom notification fields in the
        https://docs.adyen.com/api-explorer/#/ManagementService/v1/post/companies/{companyId}/webhooks/{webhookId}/test__reqParam_notification
        object.

    Possible values if webhook ``type``: **banktransfer-notification**:

    * **PENDING**

    Possible values if webhook ``type``: **report-notification**:

    * **REPORT_AVAILABLE**

    Possible values if webhook ``type``: **ideal-notification**:

    * **AUTHORISATION**

    Possible values if webhook ``type``: **pending-notification**:

    * **PENDING**"""


class TestCompanyWebhookRequestDict(TypedDict):
    merchant_ids: NotRequired[list[str]]
    notification: NotRequired[CustomNotification1 | CustomNotification1Dict]
    types: NotRequired[list[str]]
