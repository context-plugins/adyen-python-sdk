from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .amount import Amount, AmountDict
from .enums.result_code1 import ResultCode1OrStr
from .fraud_result2 import FraudResult2, FraudResult2Dict


class PayoutResponse(SdkBaseModel):
    additional_data: Optional[dict[str, str]] = Field(default=UNSET, alias="additionalData")
    """Contains additional information about the payment. Some data fields are included only if you select them first:
    Go to **Customer Area** > **Developers** > **Additional data**."""

    auth_code: Optional[str] = Field(default=UNSET, alias="authCode")
    """Authorisation code:
    * When the payment is authorised successfully, this field holds the authorisation code for the payment.
    * When the payment is not authorised, this field is empty."""

    dcc_amount: Optional[Amount] = Field(default=UNSET, alias="dccAmount")
    """Includes the currency of the conversion and the value of the transaction.
    > This value only applies if you have implemented Dynamic Currency Conversion. For more information, `contact
        Support <https://www.adyen.help/hc/en-us/requests/new>`__."""

    dcc_signature: Optional[str] = Field(default=UNSET, alias="dccSignature")
    """Cryptographic signature used to verify ``dccQuote``.
    > This value only applies if you have implemented Dynamic Currency Conversion. For more information, `contact
        Support <https://www.adyen.help/hc/en-us/requests/new>`__."""

    fraud_result: Optional[FraudResult2] = Field(default=UNSET, alias="fraudResult")
    """The fraud result properties of the payment."""

    issuer_url: Optional[str] = Field(default=UNSET, alias="issuerUrl")
    """The URL to direct the shopper to.
    > In case of SecurePlus, do not redirect a shopper to this URL."""

    md: Optional[str] = UNSET
    """The payment session."""

    pa_request: Optional[str] = Field(default=UNSET, alias="paRequest")
    """The 3D request data for the issuer.

    If the value is **CUPSecurePlus-CollectSMSVerificationCode**, collect an SMS code from the shopper and pass it in
    the ``/authorise3D`` request. For more information, see `3D Secure
    <https://docs.adyen.com/classic-integration/3d-secure>`__."""

    psp_reference: Optional[str] = Field(default=UNSET, alias="pspReference")
    """Adyen's 16-character reference associated with the transaction/request. This value is globally unique; quote it
    when communicating with us about this request."""

    refusal_reason: Optional[str] = Field(default=UNSET, alias="refusalReason")
    """If the payment's authorisation is refused or an error occurs during authorisation, this field holds Adyen's
    mapped reason for the refusal or a description of the error. When a transaction fails, the authorisation response
    includes ``resultCode`` and ``refusalReason`` values.

    For more information, see `Refusal reasons <https://docs.adyen.com/development-resources/refusal-reasons>`__."""

    result_code: Optional[ResultCode1OrStr] = Field(default=UNSET, alias="resultCode")
    """The result of the payment. For more information, see `Result codes
    <https://docs.adyen.com/online-payments/payment-result-codes>`__.

    Possible values:

    * **AuthenticationFinished** – The payment has been successfully authenticated with 3D Secure 2. Returned for 3D
        Secure 2 authentication-only transactions.
    * **AuthenticationNotRequired** – The transaction does not require 3D Secure authentication. Returned for
        `standalone authentication-only integrations
        <https://docs.adyen.com/online-payments/3d-secure/other-3ds-flows/authentication-only>`__.
    * **Authorised** – The payment was successfully authorised. This state serves as an indicator to proceed with the
        delivery of goods and services. This is a final state.
    * **Cancelled** – Indicates the payment has been cancelled (either by the shopper or the merchant) before processing
        was completed. This is a final state.
    * **ChallengeShopper** – The issuer requires further shopper interaction before the payment can be authenticated.
        Returned for 3D Secure 2 transactions.
    * **Error** – There was an error when the payment was being processed. The reason is given in the ``refusalReason``
        field. This is a final state.
    * **IdentifyShopper** – The issuer requires the shopper's device fingerprint before the payment can be
        authenticated. Returned for 3D Secure 2 transactions.
    * **PartiallyAuthorised** – The payment has been authorised for a partial amount.
    This happens for card payments when the merchant supports Partial Authorisations and the cardholder has insufficient
    funds.
    * **Pending** – Indicates that it is not possible to obtain the final status of the payment. This can happen if the
        systems providing final status information for the payment are unavailable, or if the shopper needs to take
        further action to complete the payment.
    * **PresentToShopper** – Indicates that the response contains additional information that you need to present to a
        shopper, so that they can use it to complete a payment.
    * **Received** – Indicates the payment has successfully been received by Adyen, and will be processed. This is the
        initial state for all payments.
    * **RedirectShopper** – Indicates the shopper should be redirected to an external web page or app to complete the
        authorisation.
    * **Refused** – Indicates the payment was refused. The reason is given in the ``refusalReason`` field. This is a
        final state."""


class PayoutResponseDict(TypedDict):
    additional_data: NotRequired[dict[str, str]]
    auth_code: NotRequired[str]
    dcc_amount: NotRequired[AmountDict]
    dcc_signature: NotRequired[str]
    fraud_result: NotRequired[FraudResult2Dict]
    issuer_url: NotRequired[str]
    md: NotRequired[str]
    pa_request: NotRequired[str]
    psp_reference: NotRequired[str]
    refusal_reason: NotRequired[str]
    result_code: NotRequired[ResultCode1OrStr]
