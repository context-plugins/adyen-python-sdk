from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .amount26 import Amount26, Amount26Dict
from .checkout_order_response1 import CheckoutOrderResponse1, CheckoutOrderResponse1Dict
from .enums.result_code1 import ResultCode1OrStr
from .fraud_result1 import FraudResult1, FraudResult1Dict
from .payment_response1 import PaymentResponse1, PaymentResponse1Dict
from .payment_response2 import PaymentResponse2, PaymentResponse2Dict
from .three_ds2_response_data1 import ThreeDs2ResponseData1, ThreeDs2ResponseData1Dict
from .three_ds2_result1 import ThreeDs2Result1, ThreeDs2Result1Dict
from .unions.action11 import Action11, Action11Dict


class PaymentResponse(SdkBaseModel):
    action: Optional[Action11] = UNSET
    """Action to be taken for completing the payment."""

    additional_data: Optional[dict[str, str]] = Field(default=UNSET, alias="additionalData")
    """Contains additional information about the payment. Some data fields are included only if you select them first:
    Go to **Customer Area** > **Developers** > **Additional data**."""

    amount: Optional[Amount26] = UNSET
    """Authorised amount in the transaction."""

    donation_token: Optional[str] = Field(default=UNSET, alias="donationToken")
    """Donation Token containing payment details for Adyen Giving."""

    fraud_result: Optional[FraudResult1] = Field(default=UNSET, alias="fraudResult")
    """The fraud result properties of the payment."""

    merchant_reference: Optional[str] = Field(default=UNSET, alias="merchantReference")
    """The reference to uniquely identify a payment. This reference is used in all communication with you about the
    payment status. We recommend using a unique value per payment; however, it is not a requirement. If you need to
    provide multiple references for a transaction, separate them with hyphens ("-"). Maximum length: 80 characters."""

    order: Optional[CheckoutOrderResponse1] = UNSET
    """Contains updated information regarding the order in case order information was provided in the request."""

    payment_method: Optional[PaymentResponse1] = Field(default=UNSET, alias="paymentMethod")
    """Details about the payment method used in the transaction. Only returned if ``resultCode`` is **Authorised**."""

    payment_validations: Optional[PaymentResponse2] = Field(default=UNSET, alias="paymentValidations")
    """The object that contains the validation outcomes. Only returned if ``resultCode`` is **Authorised** and if you
    have requested a payment validation in the request."""

    psp_reference: Optional[str] = Field(default=UNSET, alias="pspReference")
    """Adyen's 16-character string reference associated with the transaction/request. This value is globally unique;
    quote it when communicating with us about this request.

    > For payment methods that require a redirect or additional action, you will get this value in the
        ``/payments/details`` response."""

    refusal_reason: Optional[str] = Field(default=UNSET, alias="refusalReason")
    """If the payment's authorisation is refused or an error occurs during authorisation, this field holds Adyen's
    mapped reason for the refusal or a description of the error. When a transaction fails, the authorisation response
    includes ``resultCode`` and ``refusalReason`` values.

    For more information, see `Refusal reasons <https://docs.adyen.com/development-resources/refusal-reasons>`__."""

    refusal_reason_code: Optional[str] = Field(default=UNSET, alias="refusalReasonCode")
    """Code that specifies the refusal reason. For more information, see `Authorisation refusal reasons
    <https://docs.adyen.com/development-resources/refusal-reasons>`__."""

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

    three_ds2_response_data: Optional[ThreeDs2ResponseData1] = Field(default=UNSET, alias="threeDS2ResponseData")
    """Response of the 3D Secure 2 authentication."""

    three_ds2_result: Optional[ThreeDs2Result1] = Field(default=UNSET, alias="threeDS2Result")
    """Result of the 3D Secure 2 authentication."""

    three_ds_payment_data: Optional[str] = Field(default=UNSET, alias="threeDSPaymentData")
    """When non-empty, contains a value that you must submit to the ``/payments/details`` endpoint as
    ``paymentData``."""


class PaymentResponseDict(TypedDict):
    action: NotRequired[Action11Dict]
    additional_data: NotRequired[dict[str, str]]
    amount: NotRequired[Amount26Dict]
    donation_token: NotRequired[str]
    fraud_result: NotRequired[FraudResult1Dict]
    merchant_reference: NotRequired[str]
    order: NotRequired[CheckoutOrderResponse1Dict]
    payment_method: NotRequired[PaymentResponse1Dict]
    payment_validations: NotRequired[PaymentResponse2Dict]
    psp_reference: NotRequired[str]
    refusal_reason: NotRequired[str]
    refusal_reason_code: NotRequired[str]
    result_code: NotRequired[ResultCode1OrStr]
    three_ds2_response_data: NotRequired[ThreeDs2ResponseData1Dict]
    three_ds2_result: NotRequired[ThreeDs2Result1Dict]
    three_ds_payment_data: NotRequired[str]
