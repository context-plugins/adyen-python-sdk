
# Payment Details Response

## Structure

`PaymentDetailsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `action` | [CheckoutThreeDS2Action](../../doc/models/checkout-three-ds-2-action.md) \| None | Optional | This is a container for one-of cases. |
| `additional_data` | `Dict[str, str]` | Optional | Contains additional information about the payment. Some data fields are included only if you select them first: Go to **Customer Area** > **Developers** > **Additional data**. |
| `amount` | [`Amount26`](../../doc/models/amount-26.md) | Optional | Authorised amount in the transaction. |
| `donation_token` | `str` | Optional | Donation Token containing payment details for Adyen Giving. |
| `fraud_result` | [`FraudResult1`](../../doc/models/fraud-result-1.md) | Optional | The fraud result properties of the payment. |
| `merchant_reference` | `str` | Optional | The reference used during the /payments request. |
| `order` | [`CheckoutOrderResponse1`](../../doc/models/checkout-order-response-1.md) | Optional | Contains updated information regarding the order in case order information was provided in the request. |
| `payment_method` | [`PaymentResponse1`](../../doc/models/payment-response-1.md) | Optional | Details about the payment method used in the transaction.<br>Only returned if `resultCode` is **Authorised**. |
| `payment_validations` | [`PaymentResponse2`](../../doc/models/payment-response-2.md) | Optional | The object that contains the validation outcomes.<br>Only returned if `resultCode` is **Authorised** and if you have requested a payment validation in the request. |
| `psp_reference` | `str` | Optional | Adyen's 16-character string reference associated with the transaction/request. This value is globally unique; quote it when communicating with us about this request. |
| `refusal_reason` | `str` | Optional | If the payment's authorisation is refused or an error occurs during authorisation, this field holds Adyen's mapped reason for the refusal or a description of the error. When a transaction fails, the authorisation response includes `resultCode` and `refusalReason` values.<br><br>For more information, see [Refusal reasons](https://docs.adyen.com/development-resources/refusal-reasons). |
| `refusal_reason_code` | `str` | Optional | Code that specifies the refusal reason. For more information, see [Authorisation refusal reasons](https://docs.adyen.com/development-resources/refusal-reasons). |
| `result_code` | [`ResultCode1Enum`](../../doc/models/result-code-1-enum.md) | Optional | The result of the payment. For more information, see [Result codes](https://docs.adyen.com/online-payments/payment-result-codes).<br><br>Possible values:<br><br>* **AuthenticationFinished** – The payment has been successfully authenticated with 3D Secure 2. Returned for 3D Secure 2 authentication-only transactions.<br>* **AuthenticationNotRequired** – The transaction does not require 3D Secure authentication. Returned for [standalone authentication-only integrations](https://docs.adyen.com/online-payments/3d-secure/other-3ds-flows/authentication-only).<br>* **Authorised** – The payment was successfully authorised. This state serves as an indicator to proceed with the delivery of goods and services. This is a final state.<br>* **Cancelled** – Indicates the payment has been cancelled (either by the shopper or the merchant) before processing was completed. This is a final state.<br>* **ChallengeShopper** – The issuer requires further shopper interaction before the payment can be authenticated. Returned for 3D Secure 2 transactions.<br>* **Error** – There was an error when the payment was being processed. The reason is given in the `refusalReason` field. This is a final state.<br>* **IdentifyShopper** – The issuer requires the shopper's device fingerprint before the payment can be authenticated. Returned for 3D Secure 2 transactions.<br>* **PartiallyAuthorised** – The payment has been authorised for a partial amount.<br>  This happens for card payments when the merchant supports Partial Authorisations and the cardholder has insufficient funds.<br>* **Pending** – Indicates that it is not possible to obtain the final status of the payment. This can happen if the systems providing final status information for the payment are unavailable, or if the shopper needs to take further action to complete the payment.<br>* **PresentToShopper** – Indicates that the response contains additional information that you need to present to a shopper, so that they can use it to complete a payment.<br>* **Received** – Indicates the payment has successfully been received by Adyen, and will be processed. This is the initial state for all payments.<br>* **RedirectShopper** – Indicates the shopper should be redirected to an external web page or app to complete the authorisation.<br>* **Refused** – Indicates the payment was refused. The reason is given in the `refusalReason` field. This is a final state. |
| `shopper_locale` | `str` | Optional | The shopperLocale. |
| `three_ds_2_response_data` | [`ThreeDS2ResponseData1`](../../doc/models/three-ds-2-response-data-1.md) | Optional | Response of the 3D Secure 2 authentication. |
| `three_ds_2_result` | [`ThreeDS2Result1`](../../doc/models/three-ds-2-result-1.md) | Optional | Result of the 3D Secure 2 authentication. |
| `three_ds_payment_data` | `str` | Optional | When non-empty, contains a value that you must submit to the `/payments/details` endpoint as `paymentData`. |

## Example

```python
from adyen.models.amount_26 import Amount26
from adyen.models.checkout_three_ds_2_action import CheckoutThreeDS2Action
from adyen.models.fraud_check_result import FraudCheckResult
from adyen.models.fraud_result_1 import FraudResult1
from adyen.models.payment_details_response import PaymentDetailsResponse

payment_details_response = PaymentDetailsResponse(
    action=CheckoutThreeDS2Action(
        authorisation_token='authorisationToken0',
        payment_data='paymentData8',
        payment_method_type='paymentMethodType8',
        subtype='subtype8',
        token='token0'
    ),
    additional_data={
        'key0': 'additionalData8',
        'key1': 'additionalData9',
        'key2': 'additionalData0'
    },
    amount=Amount26(
        currency='currency2',
        value=110
    ),
    donation_token='donationToken0',
    fraud_result=FraudResult1(
        account_score=232,
        results=[
            FraudCheckResult(
                account_score=102,
                check_id=246,
                name='name6'
            ),
            FraudCheckResult(
                account_score=102,
                check_id=246,
                name='name6'
            )
        ]
    )
)
```

