# Utility

```python
utility_api = client.utility
```

## Class Name

`UtilityApi`

## Methods

* [Post-Apple Pay-Sessions](../../doc/controllers/utility.md#post-apple-pay-sessions)
* [Post-Origin Keys](../../doc/controllers/utility.md#post-origin-keys)
* [Post-Paypal-Update Order](../../doc/controllers/utility.md#post-paypal-update-order)
* [Post-Validate Shopper Id](../../doc/controllers/utility.md#post-validate-shopper-id)


# Post-Apple Pay-Sessions

You need to use this endpoint if you have an API-only integration with Apple Pay which uses Adyen's Apple Pay certificate.

The endpoint returns the Apple Pay session data which you need to complete the [Apple Pay session validation](https://docs.adyen.com/payment-methods/apple-pay/api-only?tab=adyen-certificate-validation_1#complete-apple-pay-session-validation).

```python
def post_apple_pay_sessions(self,
                           idempotency_key=None,
                           body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `idempotency_key` | `str` | Header, Optional | A unique identifier for the message with a maximum of 64 characters (we recommend a UUID). |
| `body` | [`ApplePaySessionRequest`](../../doc/models/apple-pay-session-request.md) | Body, Optional | - |

## Response Type

**200**: OK - the request has succeeded.

[`ApplePaySessionResponse`](../../doc/models/apple-pay-session-response.md)

## Example Usage

```python
body = ApplePaySessionRequest(
    display_name='YOUR_MERCHANT_NAME',
    domain_name='YOUR_DOMAIN_NAME',
    merchant_identifier='YOUR_MERCHANT_ID'
)

result = utility_api.post_apple_pay_sessions(
    body=body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "data": "eyJ2Z..."
}
```


# Post-Origin Keys

**This endpoint is deprecated.**

This operation takes the origin domains and returns a JSON object containing the corresponding origin keys for the domains.

> If you're still using origin key for your Web Drop-in or Components integration, we recommend [switching to client key](https://docs.adyen.com/development-resources/client-side-authentication/migrate-from-origin-key-to-client-key). This allows you to use a single key for all origins, add or remove origins without generating a new key, and detect the card type from the number entered in your payment form.

```python
def post_origin_keys(self,
                    idempotency_key=None,
                    body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `idempotency_key` | `str` | Header, Optional | A unique identifier for the message with a maximum of 64 characters (we recommend a UUID). |
| `body` | [`UtilityRequest`](../../doc/models/utility-request.md) | Body, Optional | - |

## Response Type

**200**: OK - the request has succeeded.

[`UtilityResponse`](../../doc/models/utility-response.md)

## Example Usage

```python
body = UtilityRequest(
    origin_domains=[
        'https://www.your-domain1.com',
        'https://www.your-domain2.com',
        'https://www.your-domain3.com'
    ]
)

result = utility_api.post_origin_keys(
    body=body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "originKeys": {
    "https://www.your-domain1.com": "pub.v2.8116178901076090.aHR0cHM6Ly93d3cueW91ci1kb21haW4xLmNvbQ.pvbYlrXz0ICP4kwMJXDGDLVMqALhwXr1MSRjT-fkhvw",
    "https://www.your-domain3.com": "pub.v2.8116178901076090.aHR0cHM6Ly93d3cueW91ci1kb21haW4zLmNvbQ.FrTpVz7_RzAywKasM0kXCRoMfoMkKIKaxjFymRGORIc",
    "https://www.your-domain2.com": "pub.v2.8116178901076090.aHR0cHM6Ly93d3cueW91ci1kb21haW4yLmNvbQ.LdN9kvJ35fYFFiBSJA4idMnwwxJ5_yXpeNS__Ap5wkg"
  }
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - a problem reading or understanding the request. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |
| 401 | Unauthorized - authentication required. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |


# Post-Paypal-Update Order

Updates the order for PayPal Express Checkout. This can be used to update the PayPal lightbox with an updated amount and delivery methods based on the delivery address.

```python
def post_paypal_update_order(self,
                            idempotency_key=None,
                            body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `idempotency_key` | `str` | Header, Optional | A unique identifier for the message with a maximum of 64 characters (we recommend a UUID). |
| `body` | [`PaypalUpdateOrderRequest`](../../doc/models/paypal-update-order-request.md) | Body, Optional | - |

## Response Type

**200**: OK - the request has succeeded.

[`PaypalUpdateOrderResponse`](../../doc/models/paypal-update-order-response.md)

## Example Usage

```python
body = PaypalUpdateOrderRequest(
    amount=Amount44(
        currency='EUR',
        value=12000
    ),
    delivery_methods=[
        DeliveryMethod(
            amount=Amount24(
                currency='EUR',
                value=1000
            ),
            description='Express Shipping',
            reference='1',
            selected=True,
            mtype=Type21Enum.SHIPPING
        ),
        DeliveryMethod(
            amount=Amount24(
                currency='EUR',
                value=500
            ),
            description='Standard Ground',
            reference='2',
            selected=False,
            mtype=Type21Enum.SHIPPING
        )
    ],
    payment_data='po7XZ...',
    psp_reference='DZ4DPSHB4WD2WN82'
)

result = utility_api.post_paypal_update_order(
    body=body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "paymentData": "po7XZ...",
  "status": "success"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - a problem reading or understanding the request. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |
| 401 | Unauthorized - authentication required. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |


# Post-Validate Shopper Id

Validates the shopperId.

:information_source: **Note** This endpoint does not require authentication.

```python
def post_validate_shopper_id(self,
                            body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`ValidateShopperIdRequest`](../../doc/models/validate-shopper-id-request.md) | Body, Required | - |

## Response Type

**200**: OK - the request has succeeded.

[`ValidateShopperIdResponse`](../../doc/models/validate-shopper-id-response.md)

## Example Usage

```python
body = ValidateShopperIdRequest(
    merchant_account='merchantAccount2',
    payment_method=ShopperIdPaymentMethod1(
        mtype='ShopperIdPaymentMethod1'
    )
)

result = utility_api.post_validate_shopper_id(body)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - a problem reading or understanding the request. | [`CheckoutErrorResponseEntityException`](../../doc/models/checkout-error-response-entity-exception.md) |
| 401 | Unauthorized - authentication required. | [`CheckoutErrorResponseEntityException`](../../doc/models/checkout-error-response-entity-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`CheckoutErrorResponseEntityException`](../../doc/models/checkout-error-response-entity-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`CheckoutErrorResponseEntityException`](../../doc/models/checkout-error-response-entity-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`CheckoutErrorResponseEntityException`](../../doc/models/checkout-error-response-entity-exception.md) |

