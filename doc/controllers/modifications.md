# Modifications

```python
modifications_api = client.modifications
```

## Class Name

`ModificationsApi`

## Methods

* [Post-Cancels](../../doc/controllers/modifications.md#post-cancels)
* [Post-Payments-Payment Psp Reference-Amount Updates](../../doc/controllers/modifications.md#post-payments-payment-psp-reference-amount-updates)
* [Post-Payments-Payment Psp Reference-Cancels](../../doc/controllers/modifications.md#post-payments-payment-psp-reference-cancels)
* [Post-Payments-Payment Psp Reference-Captures](../../doc/controllers/modifications.md#post-payments-payment-psp-reference-captures)
* [Post-Payments-Payment Psp Reference-Refunds](../../doc/controllers/modifications.md#post-payments-payment-psp-reference-refunds)
* [Post-Payments-Payment Psp Reference-Reversals](../../doc/controllers/modifications.md#post-payments-payment-psp-reference-reversals)
* [Post-Adjust Authorisation](../../doc/controllers/modifications.md#post-adjust-authorisation)
* [Post-Cancel](../../doc/controllers/modifications.md#post-cancel)
* [Post-Cancel or Refund](../../doc/controllers/modifications.md#post-cancel-or-refund)
* [Post-Capture](../../doc/controllers/modifications.md#post-capture)
* [Post-Donate](../../doc/controllers/modifications.md#post-donate)
* [Post-Refund](../../doc/controllers/modifications.md#post-refund)
* [Post-Technical Cancel](../../doc/controllers/modifications.md#post-technical-cancel)
* [Post-Void Pending Refund](../../doc/controllers/modifications.md#post-void-pending-refund)


# Post-Cancels

Cancels the authorisation on a payment that has not yet been [captured](https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/payments/{paymentPspReference}/captures), and returns a unique reference for this request. You get the outcome of the request asynchronously, in a [**TECHNICAL_CANCEL** webhook](https://docs.adyen.com/online-payments/cancel#cancellation-webhook).

If you want to cancel a payment using the [`pspReference`](https://docs.adyen.com/api-explorer/Checkout/latest/post/payments#responses-200-pspReference), use the [`/payments/{paymentPspReference}/cancels`](https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/payments/{paymentPspReference}/cancels) endpoint instead.

If you want to cancel a payment but are not sure whether it has been captured, use the [`/payments/{paymentPspReference}/reversals`](https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/payments/{paymentPspReference}/reversals) endpoint instead.

For more information, refer to [Cancel](https://docs.adyen.com/online-payments/cancel).

```python
def post_cancels(self,
                idempotency_key=None,
                body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `idempotency_key` | `str` | Header, Optional | A unique identifier for the message with a maximum of 64 characters (we recommend a UUID). |
| `body` | [`StandalonePaymentCancelRequest`](../../doc/models/standalone-payment-cancel-request.md) | Body, Optional | - |

## Response Type

**201**: Created - the request has been fulfilled and has resulted in one or more new resources being created.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`StandalonePaymentCancelResponse`](../../doc/models/standalone-payment-cancel-response.md).

## Example Usage

```python
body = StandalonePaymentCancelRequest(
    merchant_account='YOUR_MERCHANT_ACCOUNT',
    payment_reference='YOUR_UNIQUE_REFERENCE_FOR_THE_PAYMENT',
    reference='YOUR_UNIQUE_REFERENCE_FOR_THE_CANCELLATION'
)

result = modifications_api.post_cancels(
    body=body
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "merchantAccount": "YOUR_MERCHANT_ACCOUNT",
  "paymentReference": "YOUR_UNIQUE_REFERENCE_FOR_THE_PAYMENT",
  "reference": "YOUR_UNIQUE_REFERENCE_FOR_THE_CANCELLATION",
  "pspReference": "993617894906488A",
  "status": "received"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - a problem reading or understanding the request. | [`ServiceError1Exception`](../../doc/models/service-error-1-exception.md) |
| 401 | Unauthorized - authentication required. | [`ServiceError1Exception`](../../doc/models/service-error-1-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`ServiceError1Exception`](../../doc/models/service-error-1-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`ServiceError1Exception`](../../doc/models/service-error-1-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`ServiceError1Exception`](../../doc/models/service-error-1-exception.md) |


# Post-Payments-Payment Psp Reference-Amount Updates

Increases or decreases the authorised payment amount and returns a unique reference for this request. You get the outcome of the request asynchronously, in an [**AUTHORISATION_ADJUSTMENT** webhook](https://docs.adyen.com/development-resources/webhooks/webhook-types/#event-codes).

You can only update authorised amounts that have not yet been [captured](https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/payments/{paymentPspReference}/captures).

The amount you specify in the request is the updated amount, which is larger or smaller than the initial authorised amount.

For more information, refer to [Authorisation adjustment](https://docs.adyen.com/online-payments/adjust-authorisation#use-cases).

```python
def post_payments_payment_psp_reference_amount_updates(self,
                                                      payment_psp_reference,
                                                      idempotency_key=None,
                                                      body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `payment_psp_reference` | `str` | Template, Required | The [`pspReference`](https://docs.adyen.com/api-explorer/Checkout/latest/post/payments#responses-200-pspReference) of the payment. |
| `idempotency_key` | `str` | Header, Optional | A unique identifier for the message with a maximum of 64 characters (we recommend a UUID). |
| `body` | [`PaymentAmountUpdateRequest`](../../doc/models/payment-amount-update-request.md) | Body, Optional | - |

## Response Type

**201**: Created - the request has been fulfilled and has resulted in one or more new resources being created.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`PaymentAmountUpdateResponse`](../../doc/models/payment-amount-update-response.md).

## Example Usage

```python
payment_psp_reference = 'paymentPspReference2'

body = PaymentAmountUpdateRequest(
    amount=Amount16(
        currency='EUR',
        value=2500
    ),
    merchant_account='YOUR_MERCHANT_ACCOUNT',
    reference='YOUR_UNIQUE_REFERENCE'
)

result = modifications_api.post_payments_payment_psp_reference_amount_updates(
    payment_psp_reference,
    body=body
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "merchantAccount": "YOUR_MERCHANT_ACCOUNT",
  "paymentPspReference": "993617894903480A",
  "reference": "YOUR_UNIQUE_REFERENCE",
  "pspReference": "993617894906488A",
  "status": "received",
  "amount": {
    "currency": "EUR",
    "value": 2500
  }
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - a problem reading or understanding the request. | [`ServiceError1Exception`](../../doc/models/service-error-1-exception.md) |
| 401 | Unauthorized - authentication required. | [`ServiceError1Exception`](../../doc/models/service-error-1-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`ServiceError1Exception`](../../doc/models/service-error-1-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`ServiceError1Exception`](../../doc/models/service-error-1-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`ServiceError1Exception`](../../doc/models/service-error-1-exception.md) |


# Post-Payments-Payment Psp Reference-Cancels

Cancels the authorisation on a payment that has not yet been [captured](https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/payments/{paymentPspReference}/captures), and returns a unique reference for this request. You get the outcome of the request asynchronously, in a [**CANCELLATION** webhook](https://docs.adyen.com/online-payments/cancel#cancellation-webhook).

If you want to cancel a payment but don't have the [`pspReference`](https://docs.adyen.com/api-explorer/Checkout/latest/post/payments#responses-200-pspReference), use the [`/cancels`](https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/cancels) endpoint instead.

If you want to cancel a payment but are not sure whether it has been captured, use the [`/payments/{paymentPspReference}/reversals`](https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/payments/{paymentPspReference}/reversals) endpoint instead.

For more information, refer to [Cancel](https://docs.adyen.com/online-payments/cancel).

```python
def post_payments_payment_psp_reference_cancels(self,
                                               payment_psp_reference,
                                               idempotency_key=None,
                                               body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `payment_psp_reference` | `str` | Template, Required | The [`pspReference`](https://docs.adyen.com/api-explorer/Checkout/latest/post/payments#responses-200-pspReference) of the payment that you want to cancel. |
| `idempotency_key` | `str` | Header, Optional | A unique identifier for the message with a maximum of 64 characters (we recommend a UUID). |
| `body` | [`PaymentCancelRequest`](../../doc/models/payment-cancel-request.md) | Body, Optional | - |

## Response Type

**201**: Created - the request has been fulfilled and has resulted in one or more new resources being created.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`PaymentCancelResponse`](../../doc/models/payment-cancel-response.md).

## Example Usage

```python
payment_psp_reference = 'paymentPspReference2'

body = PaymentCancelRequest(
    merchant_account='YOUR_MERCHANT_ACCOUNT',
    reference='YOUR_UNIQUE_REFERENCE'
)

result = modifications_api.post_payments_payment_psp_reference_cancels(
    payment_psp_reference,
    body=body
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "merchantAccount": "YOUR_MERCHANT_ACCOUNT",
  "paymentPspReference": "993617894903480A",
  "reference": "YOUR_UNIQUE_REFERENCE",
  "pspReference": "993617894906488A",
  "status": "received"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - a problem reading or understanding the request. | [`ServiceError1Exception`](../../doc/models/service-error-1-exception.md) |
| 401 | Unauthorized - authentication required. | [`ServiceError1Exception`](../../doc/models/service-error-1-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`ServiceError1Exception`](../../doc/models/service-error-1-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`ServiceError1Exception`](../../doc/models/service-error-1-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`ServiceError1Exception`](../../doc/models/service-error-1-exception.md) |


# Post-Payments-Payment Psp Reference-Captures

Captures an authorised payment and returns a unique reference for this request. You get the outcome of the request asynchronously, in a [**CAPTURE** webhook](https://docs.adyen.com/online-payments/capture#capture-notification).

You can capture either the full authorised amount or a part of the authorised amount. By default, any unclaimed amount after a partial capture gets cancelled. This does not apply if you enabled multiple partial captures on your account and the payment method supports multiple partial captures.

[Automatic capture](https://docs.adyen.com/online-payments/capture#automatic-capture) is the default setting for most payment methods. In these cases, you don't need to make capture requests. However, making capture requests for payments that are captured automatically does not result in double charges.

For more information, refer to [Capture](https://docs.adyen.com/online-payments/capture).

```python
def post_payments_payment_psp_reference_captures(self,
                                                payment_psp_reference,
                                                idempotency_key=None,
                                                body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `payment_psp_reference` | `str` | Template, Required | The [`pspReference`](https://docs.adyen.com/api-explorer/Checkout/latest/post/payments#responses-200-pspReference) of the payment that you want to capture. |
| `idempotency_key` | `str` | Header, Optional | A unique identifier for the message with a maximum of 64 characters (we recommend a UUID). |
| `body` | [`PaymentCaptureRequest`](../../doc/models/payment-capture-request.md) | Body, Optional | - |

## Response Type

**201**: Created - the request has been fulfilled and has resulted in one or more new resources being created.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`PaymentCaptureResponse`](../../doc/models/payment-capture-response.md).

## Example Usage

```python
payment_psp_reference = 'paymentPspReference2'

body = PaymentCaptureRequest(
    amount=Amount16(
        currency='EUR',
        value=2000
    ),
    merchant_account='YOUR_MERCHANT_ACCOUNT',
    reference='YOUR_UNIQUE_REFERENCE'
)

result = modifications_api.post_payments_payment_psp_reference_captures(
    payment_psp_reference,
    body=body
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "merchantAccount": "YOUR_MERCHANT_ACCOUNT",
  "paymentPspReference": "993617894903480A",
  "reference": "YOUR_UNIQUE_REFERENCE",
  "pspReference": "993617894906488A",
  "status": "received",
  "amount": {
    "value": 2000,
    "currency": "EUR"
  }
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - a problem reading or understanding the request. | [`ServiceError1Exception`](../../doc/models/service-error-1-exception.md) |
| 401 | Unauthorized - authentication required. | [`ServiceError1Exception`](../../doc/models/service-error-1-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`ServiceError1Exception`](../../doc/models/service-error-1-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`ServiceError1Exception`](../../doc/models/service-error-1-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`ServiceError1Exception`](../../doc/models/service-error-1-exception.md) |


# Post-Payments-Payment Psp Reference-Refunds

Refunds a payment that has been [captured](https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/payments/{paymentPspReference}/captures), and returns a unique reference for this request. You get the outcome of the request asynchronously, in a [**REFUND** webhook](https://docs.adyen.com/online-payments/refund#refund-webhook).

You can refund either the full captured amount or a part of the captured amount. You can also perform multiple partial refunds, as long as their sum doesn't exceed the captured amount.

> Some payment methods do not support partial refunds. To learn if a payment method supports partial refunds, refer to the payment method page such as [cards](https://docs.adyen.com/payment-methods/cards#supported-cards), [iDEAL](https://docs.adyen.com/payment-methods/ideal), or [Klarna](https://docs.adyen.com/payment-methods/klarna).

If you want to refund a payment but are not sure whether it has been captured, use the [`/payments/{paymentPspReference}/reversals`](https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/payments/{paymentPspReference}/reversals) endpoint instead.

For more information, refer to [Refund](https://docs.adyen.com/online-payments/refund).

```python
def post_payments_payment_psp_reference_refunds(self,
                                               payment_psp_reference,
                                               idempotency_key=None,
                                               body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `payment_psp_reference` | `str` | Template, Required | The [`pspReference`](https://docs.adyen.com/api-explorer/Checkout/latest/post/payments#responses-200-pspReference) of the payment that you want to refund. |
| `idempotency_key` | `str` | Header, Optional | A unique identifier for the message with a maximum of 64 characters (we recommend a UUID). |
| `body` | [`PaymentRefundRequest`](../../doc/models/payment-refund-request.md) | Body, Optional | - |

## Response Type

**201**: Created - the request has been fulfilled and has resulted in one or more new resources being created.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`PaymentRefundResponse`](../../doc/models/payment-refund-response.md).

## Example Usage

```python
payment_psp_reference = 'paymentPspReference2'

body = PaymentRefundRequest(
    amount=Amount16(
        currency='EUR',
        value=2500
    ),
    merchant_account='YOUR_MERCHANT_ACCOUNT',
    reference='YOUR_UNIQUE_REFERENCE'
)

result = modifications_api.post_payments_payment_psp_reference_refunds(
    payment_psp_reference,
    body=body
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "merchantAccount": "YOUR_MERCHANT_ACCOUNT",
  "paymentPspReference": "993617894903480A",
  "reference": "YOUR_UNIQUE_REFERENCE",
  "pspReference": "993617894906488A",
  "status": "received",
  "amount": {
    "currency": "EUR",
    "value": 2500
  }
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - a problem reading or understanding the request. | [`ServiceError1Exception`](../../doc/models/service-error-1-exception.md) |
| 401 | Unauthorized - authentication required. | [`ServiceError1Exception`](../../doc/models/service-error-1-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`ServiceError1Exception`](../../doc/models/service-error-1-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`ServiceError1Exception`](../../doc/models/service-error-1-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`ServiceError1Exception`](../../doc/models/service-error-1-exception.md) |


# Post-Payments-Payment Psp Reference-Reversals

[Refunds](https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/payments/{paymentPspReference}/refunds) a payment if it has already been captured, and [cancels](https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/payments/{paymentPspReference}/cancels) a payment if it has not yet been captured. Returns a unique reference for this request. You get the outcome of the request asynchronously, in a [**CANCEL_OR_REFUND** webhook](https://docs.adyen.com/online-payments/reversal/#cancel-or-refund-webhook).

The reversed amount is always the full payment amount.

> Do not use this request for payments that involve multiple partial captures.

For more information, refer to [Reversal](https://docs.adyen.com/online-payments/reversal).

```python
def post_payments_payment_psp_reference_reversals(self,
                                                 payment_psp_reference,
                                                 idempotency_key=None,
                                                 body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `payment_psp_reference` | `str` | Template, Required | The [`pspReference`](https://docs.adyen.com/api-explorer/Checkout/latest/post/payments#responses-200-pspReference) of the payment that you want to reverse. |
| `idempotency_key` | `str` | Header, Optional | A unique identifier for the message with a maximum of 64 characters (we recommend a UUID). |
| `body` | [`PaymentReversalRequest`](../../doc/models/payment-reversal-request.md) | Body, Optional | - |

## Response Type

**201**: Created - the request has been fulfilled and has resulted in one or more new resources being created.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`PaymentReversalResponse`](../../doc/models/payment-reversal-response.md).

## Example Usage

```python
payment_psp_reference = 'paymentPspReference2'

body = PaymentReversalRequest(
    merchant_account='YOUR_MERCHANT_ACCOUNT',
    reference='YOUR_UNIQUE_REFERENCE'
)

result = modifications_api.post_payments_payment_psp_reference_reversals(
    payment_psp_reference,
    body=body
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "merchantAccount": "YOUR_MERCHANT_ACCOUNT",
  "paymentPspReference": "993617894903480A",
  "reference": "YOUR_UNIQUE_REFERENCE",
  "pspReference": "993617894906488A",
  "status": "received"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - a problem reading or understanding the request. | [`ServiceError1Exception`](../../doc/models/service-error-1-exception.md) |
| 401 | Unauthorized - authentication required. | [`ServiceError1Exception`](../../doc/models/service-error-1-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`ServiceError1Exception`](../../doc/models/service-error-1-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`ServiceError1Exception`](../../doc/models/service-error-1-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`ServiceError1Exception`](../../doc/models/service-error-1-exception.md) |


# Post-Adjust Authorisation

Allows you to increase or decrease the authorised amount after the initial authorisation has taken place. This functionality enables for example tipping, improving the chances your authorisation will be valid, or charging the shopper when they have already left the merchant premises.

> This endpoint is [inactive](https://docs.adyen.com/online-payments/upgrade-your-integration#checkout-api-lifecycle) and is no longer supported for new integrations.
> 
> * If you are building a new integration, use the Checkout API [`/payments/{paymentPspReference}/amountUpdates`](https://docs.adyen.com/api-explorer/Checkout/latest/post/payments/(paymentPspReference)/amountUpdates) endpoint instead.
> * If you have an existing integration using this endpoint, reach out to your Adyen contact and [migrate to the Checkout API](https://docs.adyen.com/online-payments/upgrade-your-integration/migrate-to-checkout-api).

> The Checkout API enables your [online payments](https://docs.adyen.com/online-payments) integration to accept all supported payment methods, use the latest features, and access more benefits.

```python
def post_adjust_authorisation(self,
                             body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`AdjustAuthorisationRequest`](../../doc/models/adjust-authorisation-request.md) | Body, Optional | - |

## Response Type

**200**: OK - the request has succeeded.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ModificationResult`](../../doc/models/modification-result.md).

## Example Usage

```python
body = AdjustAuthorisationRequest(
    merchant_account='YOUR_MERCHANT_ACCOUNT',
    modification_amount=ModificationAmount(
        currency='USD',
        value=1700
    ),
    original_reference='COPY_PSP_REFERENCE_FROM_AUTHORISE_RESPONSE',
    reference='YourModificationReference'
)

result = modifications_api.post_adjust_authorisation(
    body=body
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "pspReference": "851617892360718D",
  "response": "[adjustAuthorisation-received]"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - a problem reading or understanding the request. | [`ServiceError1Exception`](../../doc/models/service-error-1-exception.md) |
| 401 | Unauthorized - authentication required. | [`ServiceError1Exception`](../../doc/models/service-error-1-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`ServiceError1Exception`](../../doc/models/service-error-1-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`ServiceError1Exception`](../../doc/models/service-error-1-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`ServiceError1Exception`](../../doc/models/service-error-1-exception.md) |


# Post-Cancel

Cancels the authorisation hold on a payment, returning a unique reference for this request. You can cancel payments after authorisation only for payment methods that support distinct authorisations and captures.

For more information, refer to [Cancel](https://docs.adyen.com/online-payments/classic-integrations/modify-payments/cancel).

> This endpoint is [inactive](https://docs.adyen.com/online-payments/upgrade-your-integration#checkout-api-lifecycle) and is no longer supported for new integrations.
> 
> * If you are building a new integration, use the Checkout API [`/payments/{paymentPspReference}/cancels`](https://docs.adyen.com/api-explorer/Checkout/latest/post/payments/(paymentPspReference)/cancels) endpoint instead.
> * If you have an existing integration using this endpoint, reach out to your Adyen contact and [migrate to the Checkout API](https://docs.adyen.com/online-payments/upgrade-your-integration/migrate-to-checkout-api).

> The Checkout API enables your [online payments](https://docs.adyen.com/online-payments) integration to accept all supported payment methods, use the latest features, and access more benefits.

```python
def post_cancel(self,
               body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`CancelRequest`](../../doc/models/cancel-request.md) | Body, Optional | - |

## Response Type

**200**: OK - the request has succeeded.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ModificationResult`](../../doc/models/modification-result.md).

## Example Usage

```python
body = CancelRequest(
    merchant_account='YOUR_MERCHANT_ACCOUNT',
    original_reference='COPY_PSP_REFERENCE_FROM_AUTHORISE_RESPONSE',
    reference='YourModificationReference'
)

result = modifications_api.post_cancel(
    body=body
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - a problem reading or understanding the request. | [`ServiceError1Exception`](../../doc/models/service-error-1-exception.md) |
| 401 | Unauthorized - authentication required. | [`ServiceError1Exception`](../../doc/models/service-error-1-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`ServiceError1Exception`](../../doc/models/service-error-1-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`ServiceError1Exception`](../../doc/models/service-error-1-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`ServiceError1Exception`](../../doc/models/service-error-1-exception.md) |


# Post-Cancel or Refund

Cancels a payment if it has not been captured yet, or refunds it if it has already been captured. This is useful when it is not certain if the payment has been captured or not (for example, when using auto-capture).

Do not use this endpoint for payments that involve:

* [Multiple partial captures](https://docs.adyen.com/online-payments/capture).
* [Split data](https://docs.adyen.com/classic-platforms/processing-payments#providing-split-information) either at time of payment or capture for Adyen for Platforms.

Instead, check if the payment has been captured and make a corresponding [`/refund`](https://docs.adyen.com/api-explorer/#/Payment/refund) or [`/cancel`](https://docs.adyen.com/api-explorer/#/Payment/cancel) call.

For more information, refer to [Cancel or refund](https://docs.adyen.com/online-payments/classic-integrations/modify-payments/cancel-or-refund).

> This endpoint is [inactive](https://docs.adyen.com/online-payments/upgrade-your-integration#checkout-api-lifecycle) and is no longer supported for new integrations.
> 
> * If you are building a new integration, use the Checkout API [`/payments/{paymentPspReference}/reversals`](https://docs.adyen.com/api-explorer/Checkout/latest/post/payments/(paymentPspReference)/reversals) endpoint instead.
> * If you have an existing integration using this endpoint, reach out to your Adyen contact and [migrate to the Checkout API](https://docs.adyen.com/online-payments/upgrade-your-integration/migrate-to-checkout-api).

> The Checkout API enables your [online payments](https://docs.adyen.com/online-payments) integration to accept all supported payment methods, use the latest features, and access more benefits.

```python
def post_cancel_or_refund(self,
                         body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`CancelOrRefundRequest`](../../doc/models/cancel-or-refund-request.md) | Body, Optional | - |

## Response Type

**200**: OK - the request has succeeded.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ModificationResult`](../../doc/models/modification-result.md).

## Example Usage

```python
body = CancelOrRefundRequest(
    merchant_account='YOUR_MERCHANT_ACCOUNT',
    original_reference='COPY_PSP_REFERENCE_FROM_AUTHORISE_RESPONSE',
    reference='YourModificationReference'
)

result = modifications_api.post_cancel_or_refund(
    body=body
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "pspReference": "851617892359708H",
  "response": "[cancelOrRefund-received]"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - a problem reading or understanding the request. | [`ServiceError1Exception`](../../doc/models/service-error-1-exception.md) |
| 401 | Unauthorized - authentication required. | [`ServiceError1Exception`](../../doc/models/service-error-1-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`ServiceError1Exception`](../../doc/models/service-error-1-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`ServiceError1Exception`](../../doc/models/service-error-1-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`ServiceError1Exception`](../../doc/models/service-error-1-exception.md) |


# Post-Capture

Captures the authorisation hold on a payment, returning a unique reference for this request. Usually the full authorisation amount is captured, however it's also possible to capture a smaller amount, which results in cancelling the remaining authorisation balance.

Payment methods that are captured automatically after authorisation don't need to be captured. However, submitting a capture request on these transactions will not result in double charges. If immediate or delayed auto-capture is enabled, calling the capture method is not necessary.

For more information refer to [Capture](https://docs.adyen.com/online-payments/classic-integrations/modify-payments/capture).

> This endpoint is [inactive](https://docs.adyen.com/online-payments/upgrade-your-integration#checkout-api-lifecycle) and is no longer supported for new integrations.
> 
> * If you are building a new integration, use the Checkout API [`/payments/{paymentPspReference}/captures`](https://docs.adyen.com/api-explorer/Checkout/latest/post/payments/(paymentPspReference)/captures) endpoint instead.
> * If you have an existing integration using this endpoint, reach out to your Adyen contact and [migrate to the Checkout API](https://docs.adyen.com/online-payments/upgrade-your-integration/migrate-to-checkout-api).

> The Checkout API enables your [online payments](https://docs.adyen.com/online-payments) integration to accept all supported payment methods, use the latest features, and access more benefits.

```python
def post_capture(self,
                body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`CaptureRequest`](../../doc/models/capture-request.md) | Body, Optional | - |

## Response Type

**200**: OK - the request has succeeded.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ModificationResult`](../../doc/models/modification-result.md).

## Example Usage

```python
body = CaptureRequest(
    merchant_account='YOUR_MERCHANT_ACCOUNT',
    modification_amount=ModificationAmount(
        currency='EUR',
        value=500
    ),
    original_reference='COPY_PSP_REFERENCE_FROM_AUTHORISE_RESPONSE',
    reference='YOUR_REFERENCE'
)

result = modifications_api.post_capture(
    body=body
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "pspReference": "861617892359057J",
  "response": "[capture-received]"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - a problem reading or understanding the request. | [`ServiceError1Exception`](../../doc/models/service-error-1-exception.md) |
| 401 | Unauthorized - authentication required. | [`ServiceError1Exception`](../../doc/models/service-error-1-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`ServiceError1Exception`](../../doc/models/service-error-1-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`ServiceError1Exception`](../../doc/models/service-error-1-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`ServiceError1Exception`](../../doc/models/service-error-1-exception.md) |


# Post-Donate

**This endpoint is deprecated.**

Schedules a new payment to be created (including a new authorisation request) for the specified donation using the payment details of the original payment.

> This endpoint is [inactive](https://docs.adyen.com/online-payments/upgrade-your-integration#checkout-api-lifecycle) and is no longer supported for new integrations.
> 
> * If you are building a new integration, use the Checkout API [`/donations`](https://docs.adyen.com/api-explorer/Checkout/latest/post/donations) endpoint instead.
> * If you have an existing integration using this endpoint, reach out to your Adyen contact and [migrate to the Checkout API](https://docs.adyen.com/online-payments/upgrade-your-integration/migrate-to-checkout-api).

> The Checkout API enables your [online payments](https://docs.adyen.com/online-payments) integration to accept all supported payment methods, use the latest features, and access more benefits.

```python
def post_donate(self,
               body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`DonationRequest`](../../doc/models/donation-request.md) | Body, Optional | - |

## Response Type

**200**: OK - the request has succeeded.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ModificationResult`](../../doc/models/modification-result.md).

## Example Usage

```python
body = DonationRequest(
    donation_account='AdyenGivingDemo',
    merchant_account='YOUR_MERCHANT_ACCOUNT',
    modification_amount=ModificationAmount(
        currency='EUR',
        value=500
    ),
    original_reference='COPY_PSP_REFERENCE_FROM_AUTHORISE_RESPONSE',
    reference='YOUR_DONATION_REFERENCE'
)

result = modifications_api.post_donate(
    body=body
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - a problem reading or understanding the request. | [`ServiceError1Exception`](../../doc/models/service-error-1-exception.md) |
| 401 | Unauthorized - authentication required. | [`ServiceError1Exception`](../../doc/models/service-error-1-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`ServiceError1Exception`](../../doc/models/service-error-1-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`ServiceError1Exception`](../../doc/models/service-error-1-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`ServiceError1Exception`](../../doc/models/service-error-1-exception.md) |


# Post-Refund

Refunds a payment that has previously been captured, returning a unique reference for this request. Refunding can be done on the full captured amount or a partial amount. Multiple (partial) refunds will be accepted as long as their sum doesn't exceed the captured amount. Payments which have been authorised, but not captured, cannot be refunded, use the /cancel method instead.

Some payment methods/gateways do not support partial/multiple refunds.
A margin above the captured limit can be configured to cover shipping/handling costs.

For more information, refer to [Refund](https://docs.adyen.com/online-payments/classic-integrations/modify-payments/refund).

> This endpoint is [inactive](https://docs.adyen.com/online-payments/upgrade-your-integration#checkout-api-lifecycle) and is no longer supported for new integrations.
> 
> * If you are building a new integration, use the Checkout API [`/payments/{paymentPspReference}/refunds`](https://docs.adyen.com/api-explorer/Checkout/latest/post/payments/(paymentPspReference)/refunds) endpoint instead.
> * If you have an existing integration using this endpoint, reach out to your Adyen contact and [migrate to the Checkout API](https://docs.adyen.com/online-payments/upgrade-your-integration/migrate-to-checkout-api).

> The Checkout API enables your [online payments](https://docs.adyen.com/online-payments) integration to accept all supported payment methods, use the latest features, and access more benefits.

```python
def post_refund(self,
               body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`RefundRequest`](../../doc/models/refund-request.md) | Body, Optional | - |

## Response Type

**200**: OK - the request has succeeded.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ModificationResult`](../../doc/models/modification-result.md).

## Example Usage

```python
body = RefundRequest(
    merchant_account='YOUR_MERCHANT_ACCOUNT',
    modification_amount=ModificationAmount(
        currency='EUR',
        value=500
    ),
    original_reference='COPY_PSP_REFERENCE_FROM_AUTHORISE_RESPONSE',
    reference='YOUR_REFERENCE'
)

result = modifications_api.post_refund(
    body=body
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "pspReference": "861617892360059B",
  "response": "[refund-received]"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - a problem reading or understanding the request. | [`ServiceError1Exception`](../../doc/models/service-error-1-exception.md) |
| 401 | Unauthorized - authentication required. | [`ServiceError1Exception`](../../doc/models/service-error-1-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`ServiceError1Exception`](../../doc/models/service-error-1-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`ServiceError1Exception`](../../doc/models/service-error-1-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`ServiceError1Exception`](../../doc/models/service-error-1-exception.md) |


# Post-Technical Cancel

This endpoint allows you to cancel a payment if you do not have the PSP reference of the original payment request available.

In your call, refer to the original payment by using the `reference` that you specified in your payment request.

For more information, see [Technical cancel](https://docs.adyen.com/online-payments/classic-integrations/modify-payments/cancel#technical-cancel).

> This endpoint is [inactive](https://docs.adyen.com/online-payments/upgrade-your-integration#checkout-api-lifecycle) and is no longer supported for new integrations.
> 
> * If you are building a new integration, use the Checkout API [`/cancels`](https://docs.adyen.com/api-explorer/Checkout/latest/post/cancels) endpoint instead.
> * If you have an existing integration using this endpoint, reach out to your Adyen contact and [migrate to the Checkout API](https://docs.adyen.com/online-payments/upgrade-your-integration/migrate-to-checkout-api).

> The Checkout API enables your [online payments](https://docs.adyen.com/online-payments) integration to accept all supported payment methods, use the latest features, and access more benefits.

```python
def post_technical_cancel(self,
                         body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`TechnicalCancelRequest`](../../doc/models/technical-cancel-request.md) | Body, Optional | - |

## Response Type

**200**: OK - the request has succeeded.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ModificationResult`](../../doc/models/modification-result.md).

## Example Usage

```python
body = TechnicalCancelRequest(
    merchant_account='YOUR_MERCHANT_ACCOUNT',
    original_merchant_reference='YOUR_MERCHANT_REFERENCE',
    reference='YOUR_MODIFICATION_REFERENCE'
)

result = modifications_api.post_technical_cancel(
    body=body
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "pspReference": "881617892361436J",
  "response": "[technical-cancel-received]"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - a problem reading or understanding the request. | [`ServiceError1Exception`](../../doc/models/service-error-1-exception.md) |
| 401 | Unauthorized - authentication required. | [`ServiceError1Exception`](../../doc/models/service-error-1-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`ServiceError1Exception`](../../doc/models/service-error-1-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`ServiceError1Exception`](../../doc/models/service-error-1-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`ServiceError1Exception`](../../doc/models/service-error-1-exception.md) |


# Post-Void Pending Refund

This endpoint allows you to cancel an unreferenced refund request before it has been completed.

In your call, you can refer to the original refund request either by using the `tenderReference`, or the `pspReference`. We recommend implementing based on the `tenderReference`, as this is generated for both offline and online transactions.

For more information, refer to [Cancel an unreferenced refund](https://docs.adyen.com/point-of-sale/basic-tapi-integration/refund-payment/cancel-unreferenced).

```python
def post_void_pending_refund(self,
                            body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`VoidPendingRefundRequest`](../../doc/models/void-pending-refund-request.md) | Body, Optional | - |

## Response Type

**200**: OK - the request has succeeded.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ModificationResult`](../../doc/models/modification-result.md).

## Example Usage

```python
body = VoidPendingRefundRequest(
    merchant_account='YOUR_MERCHANT_ACCOUNT',
    original_reference='9914748988390044'
)

result = modifications_api.post_void_pending_refund(
    body=body
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "pspReference": "861617892360062F",
  "response": "[voidPendingRefund-received]"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - a problem reading or understanding the request. | [`ServiceError1Exception`](../../doc/models/service-error-1-exception.md) |
| 401 | Unauthorized - authentication required. | [`ServiceError1Exception`](../../doc/models/service-error-1-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`ServiceError1Exception`](../../doc/models/service-error-1-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`ServiceError1Exception`](../../doc/models/service-error-1-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`ServiceError1Exception`](../../doc/models/service-error-1-exception.md) |

