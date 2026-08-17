# Recurring

```python
recurring_api = client.recurring
```

## Class Name

`RecurringApi`

## Methods

* [Post-Forward](../../doc/controllers/recurring.md#post-forward)
* [Get-Stored Payment Methods](../../doc/controllers/recurring.md#get-stored-payment-methods)
* [Post-Stored Payment Methods](../../doc/controllers/recurring.md#post-stored-payment-methods)
* [Delete-Stored Payment Methods-Stored Payment Method Id](../../doc/controllers/recurring.md#delete-stored-payment-methods-stored-payment-method-id)


# Post-Forward

Forwards the payment details you stored with Adyen to a third-party that you specify and returns the response from the third-party. Supports forwarding stored card details or [network tokens](https://docs.adyen.com/online-payments/network-tokenization). For more information, see [Forward stored payment details](https://docs.adyen.com/online-payments/tokenization/forward-payment-details).

```python
def post_forward(self,
                idempotency_key=None,
                body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `idempotency_key` | `str` | Header, Optional | A unique identifier for the message with a maximum of 64 characters (we recommend a UUID). |
| `body` | [`CheckoutForwardRequest`](../../doc/models/checkout-forward-request.md) | Body, Optional | - |

## Response Type

**200**: OK - the request has succeeded.

[`CheckoutForwardResponse`](../../doc/models/checkout-forward-response.md)

## Example Usage

```python
body = CheckoutForwardRequest(
    base_url='http://thirdparty.example.com',
    merchant_account='YOUR_MERCHANT_ACCOUNT',
    request=CheckoutOutgoingForwardRequest2(
        body='{"amount":{"value":100,"currency":"USD"},"paymentMethod":{"creditCard":{"holderName":"{{holderName}}","number":"{{number}}","expiryMonth":"{{expiryMonth}}","expiryYear":"{{expiryYear}}"}}}',
        http_method=HttpMethodEnum.POST,
        credentials='YOUR_CREDENTIALS_FOR_THE_THIRD_PARTY',
        headers={
            'Authorization': 'Basic {{credentials}}'
        },
        url_suffix='/payments'
    ),
    shopper_reference='YOUR_SHOPPER_REFERENCE',
    stored_payment_method_id='M5N7TQ4TG5PFWR50'
)

result = recurring_api.post_forward(
    body=body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "storedPaymentMethodId": "M5N7TQ4TG5PFWR50",
  "pspReference": "XB7XNCQ8HXSKGK82",
  "response": {
    "status": 200,
    "headers": {
      "thirdparty-version": "2023-10-16"
    },
    "body": "{\"success\": \"ok\",\"data\": {\"tokenizeCreditCard\": {\"paymentMethod\": {\"id\": \"PAYMENT_METHOD_ID\"}}}}"
  }
}
```


# Get-Stored Payment Methods

Lists the tokens for stored payment details for the shopper identified in the path, if there are any available. The token ID can be used with payment requests for the shopper's payment. A summary of the stored details is included.

```python
def get_stored_payment_methods(self,
                              shopper_reference=None,
                              merchant_account=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `shopper_reference` | `str` | Query, Optional | Your reference to uniquely identify this shopper, for example user ID or account ID. Minimum length: 3 characters.<br><br>> Your reference must not include personally identifiable information (PII), for example name or email address. |
| `merchant_account` | `str` | Query, Optional | Your merchant account. |

## Response Type

**200**: OK - the request has succeeded.

[`ListStoredPaymentMethodsResponse`](../../doc/models/list-stored-payment-methods-response.md)

## Example Usage

```python
result = recurring_api.get_stored_payment_methods()
print(result)
```

## Example Response *(as JSON)*

```json
{
  "merchantAccount": "YOUR_MERCHANT_ACCOUNT",
  "shopperReference": "YOUR_SHOPPER_REFERENCE",
  "storedPaymentMethods": [
    {
      "brand": "visa",
      "expiryMonth": "10",
      "expiryYear": "30",
      "holderName": "John Smith",
      "id": "7219687191761347",
      "issuerName": "ISSUER_NAME",
      "lastFour": "1111",
      "name": "VISA",
      "shopperEmail": "john.smith@example.com",
      "shopperReference": "YOUR_SHOPPER_REFERENCE",
      "supportedRecurringProcessingModels": [
        "CardOnFile",
        "Subscription",
        "UnscheduledCardOnFile"
      ],
      "type": "scheme"
    }
  ]
}
```


# Post-Stored Payment Methods

Creates a token to store the shopper's payment details. This token can be used for the shopper's future payments.

```python
def post_stored_payment_methods(self,
                               idempotency_key=None,
                               body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `idempotency_key` | `str` | Header, Optional | A unique identifier for the message with a maximum of 64 characters (we recommend a UUID). |
| `body` | [`StoredPaymentMethodRequest`](../../doc/models/stored-payment-method-request.md) | Body, Optional | - |

## Response Type

**201**: Created - the request has been fulfilled and has resulted in one or more new resources being created.

[`StoredPaymentMethodResource`](../../doc/models/stored-payment-method-resource.md)

## Example Usage

```python
body = StoredPaymentMethodRequest(
    merchant_account='YOUR_MERCHANT_ACCOUNT',
    payment_method=PaymentMethodToStore1(
        encrypted_card_number='test_4111111111111111',
        encrypted_expiry_month='test_03',
        encrypted_expiry_year='test_2030',
        encrypted_security_code='test_737',
        holder_name='John Smith',
        mtype='scheme'
    ),
    recurring_processing_model=RecurringProcessingModel1Enum.SUBSCRIPTION,
    shopper_reference='YOUR_SHOPPER_REFERENCE',
    shopper_email='s.hopper@test.com',
    shopper_ip='192.0.2.1'
)

result = recurring_api.post_stored_payment_methods(
    body=body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "expiryMonth": "03",
  "expiryYear": "2030",
  "holderName": "John Smith",
  "id": "KHQC5N7G84BLNK43",
  "lastFour": "1111",
  "shopperReference": "YOUR_SHOPPER_REFERENCE",
  "type": "scheme"
}
```


# Delete-Stored Payment Methods-Stored Payment Method Id

Deletes the token identified in the path. The token can no longer be used with payment requests.

```python
def delete_stored_payment_methods_stored_payment_method_id(self,
                                                          stored_payment_method_id,
                                                          shopper_reference,
                                                          merchant_account)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `stored_payment_method_id` | `str` | Template, Required | The unique identifier of the token. |
| `shopper_reference` | `str` | Query, Required | Your reference to uniquely identify this shopper, for example user ID or account ID. Minimum length: 3 characters.<br><br>> Your reference must not include personally identifiable information (PII), for example name or email address. |
| `merchant_account` | `str` | Query, Required | Your merchant account. |

## Response Type

**204**: No Content - look at the actual response code for the status of the request.

`void`

## Example Usage

```python
stored_payment_method_id = 'storedPaymentMethodId4'

shopper_reference = 'shopperReference8'

merchant_account = 'merchantAccount8'

recurring_api.delete_stored_payment_methods_stored_payment_method_id(
    stored_payment_method_id,
    shopper_reference,
    merchant_account
)
```

