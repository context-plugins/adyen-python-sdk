from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class TestOutput(SdkBaseModel):
    merchant_id: Optional[str] = Field(default=UNSET, alias="merchantId")
    """Unique identifier of the merchant account that the notification is about."""

    output: Optional[str] = UNSET
    """A short, human-readable explanation of the test result.

    Your server must respond with **HTTP 2xx* for the test webhook to be successful (``data.status``: **success**). Find
    out more about `accepting notifications <https://docs.adyen.com/development-resources/webhooks/#accept-webhooks>`__

    You can use the value of this field together with the
    https://docs.adyen.com/api-explorer/#/ManagementService/v1/post/merchants/{merchantId}/webhooks/{id}/test__resParam_data-responseCode
    value to troubleshoot unsuccessful test webhooks."""

    request_sent: Optional[str] = Field(default=UNSET, alias="requestSent")
    """The `body of the notification webhook
    <https://docs.adyen.com/development-resources/webhooks/understand-notifications#notification-structure>`__ that was
    sent to your server."""

    response_code: Optional[str] = Field(default=UNSET, alias="responseCode")
    """The HTTP response code for your server's response to the test webhook.

    You can use the value of this field together with the the
    https://docs.adyen.com/api-explorer/#/ManagementService/v1/post/merchants/{merchantId}/webhooks/{id}/test__resParam_data-output
    field value to troubleshoot failed test webhooks."""

    response_time: Optional[str] = Field(default=UNSET, alias="responseTime")
    """The time between sending the test webhook and receiving the response from your server. You can use it as an
    indication of how long your server takes to process a webhook notification. Measured in milliseconds, for example
    **304 ms**."""

    status: str
    """The status of the test request. Possible values are:
    * **success**, ``data.responseCode``: **2xx**.
    * **failed**, in all other cases.

    You can use the value of the
    https://docs.adyen.com/api-explorer/#/ManagementService/v1/post/merchants/{merchantId}/webhooks/{id}/test__resParam_data-output
    field together with the
    https://docs.adyen.com/api-explorer/#/ManagementService/v1/post/merchants/{merchantId}/webhooks/{id}/test__resParam_data-responseCode
    value to troubleshoot failed test webhooks."""


class TestOutputDict(TypedDict):
    merchant_id: NotRequired[str]
    output: NotRequired[str]
    request_sent: NotRequired[str]
    response_code: NotRequired[str]
    response_time: NotRequired[str]
    status: str
