from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class PaymentCompletionDetails(SdkBaseModel):
    md: Optional[str] = Field(default=UNSET, alias="MD")
    """A payment session identifier returned by the card issuer."""

    pa_req: Optional[str] = Field(default=UNSET, alias="PaReq")
    """(3D) Payment Authentication Request data for the card issuer."""

    pa_res: Optional[str] = Field(default=UNSET, alias="PaRes")
    """(3D) Payment Authentication Response data by the card issuer."""

    authorization_token: Optional[str] = UNSET
    billing_token: Optional[str] = Field(default=UNSET, alias="billingToken")
    """PayPal-generated token for recurring payments."""

    cupsecureplus_smscode: Optional[str] = Field(default=UNSET, alias="cupsecureplus.smscode")
    """The SMS verification code collected from the shopper."""

    facilitator_access_token: Optional[str] = Field(default=UNSET, alias="facilitatorAccessToken")
    """PayPal-generated third party access token."""

    one_time_passcode: Optional[str] = Field(default=UNSET, alias="oneTimePasscode")
    """A random number sent to the mobile phone number of the shopper to verify the payment."""

    order_id: Optional[str] = Field(default=UNSET, alias="orderID")
    """PayPal-assigned ID for the order."""

    payer_id: Optional[str] = Field(default=UNSET, alias="payerID")
    """PayPal-assigned ID for the payer (shopper)."""

    payload: Optional[str] = UNSET
    """Payload appended to the ``returnURL`` as a result of the redirect."""

    payment_id: Optional[str] = Field(default=UNSET, alias="paymentID")
    """PayPal-generated ID for the payment."""

    payment_status: Optional[str] = Field(default=UNSET, alias="paymentStatus")
    """Value passed from the WeChat MiniProgram ``wx.requestPayment`` **complete** callback. Possible values: any value
    starting with ``requestPayment:``."""

    redirect_result: Optional[str] = Field(default=UNSET, alias="redirectResult")
    """The result of the redirect as appended to the ``returnURL``."""

    result_code: Optional[str] = Field(default=UNSET, alias="resultCode")
    """Value you received from the WeChat Pay SDK."""

    return_url_query_string: Optional[str] = Field(default=UNSET, alias="returnUrlQueryString")
    """The query string as appended to the ``returnURL`` when using direct issuer links ."""

    three_ds_result: Optional[str] = Field(default=UNSET, alias="threeDSResult")
    """Base64-encoded string returned by the Component after the challenge flow. It contains the following parameters:
    ``transStatus``, ``authorisationToken``."""

    threeds2_challenge_result: Optional[str] = Field(default=UNSET, alias="threeds2.challengeResult")
    """Base64-encoded string returned by the Component after the challenge flow. It contains the following parameter:
    ``transStatus``."""

    threeds2_fingerprint: Optional[str] = Field(default=UNSET, alias="threeds2.fingerprint")
    """Base64-encoded string returned by the Component after the challenge flow. It contains the following parameter:
    ``threeDSCompInd``."""

    vault_token: Optional[str] = Field(default=UNSET, alias="vaultToken")
    """PayPalv2-generated token for recurring payments."""


class PaymentCompletionDetailsDict(TypedDict):
    md: NotRequired[str]
    pa_req: NotRequired[str]
    pa_res: NotRequired[str]
    authorization_token: NotRequired[str]
    billing_token: NotRequired[str]
    cupsecureplus_smscode: NotRequired[str]
    facilitator_access_token: NotRequired[str]
    one_time_passcode: NotRequired[str]
    order_id: NotRequired[str]
    payer_id: NotRequired[str]
    payload: NotRequired[str]
    payment_id: NotRequired[str]
    payment_status: NotRequired[str]
    redirect_result: NotRequired[str]
    result_code: NotRequired[str]
    return_url_query_string: NotRequired[str]
    three_ds_result: NotRequired[str]
    threeds2_challenge_result: NotRequired[str]
    threeds2_fingerprint: NotRequired[str]
    vault_token: NotRequired[str]
