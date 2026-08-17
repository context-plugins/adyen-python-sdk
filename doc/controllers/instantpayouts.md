# Instantpayouts

```python
instantpayouts_api = client.instantpayouts
```

## Class Name

`InstantpayoutsApi`


# Post-Payout

> This endpoint is **deprecated** and no longer supports new integrations. Do one of the following:
> 
> - If you are building a new integration, use the POST [/transfers](https://docs.adyen.com/api-explorer/transfers/latest/post/transfers) endpoint instead.
> - If you are already using the Payout API, reach out to your Adyen contact to learn how to migrate to the Transfers API.
> 
> With the Transfers API, you can:
> 
> - Handle multiple payout use cases with a single API.
> - Use new payout functionalities, such as instant payouts to bank accounts.
> - Receive webhooks with more details and defined transfer states.
> 
> For more information about the payout features of the Transfers API, see our [Payouts](https://docs.adyen.com/payouts/payout-service) documentation.

With this call, you can pay out to your customers, and funds will be made available within 30 minutes on the cardholder's bank account (this is dependent on whether the issuer supports this functionality). Instant card payouts are only supported for Visa and Mastercard cards.

```python
def post_payout(self,
               body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`PayoutRequest`](../../doc/models/payout-request.md) | Body, Optional | - |

## Response Type

**200**: OK - the request has succeeded.

[`PayoutResponse`](../../doc/models/payout-response.md)

## Example Usage

```python
body = PayoutRequest(
    amount=Amount(
        currency='USD',
        value=2500
    ),
    merchant_account='YOUR_MERCHANT_ACCOUNT',
    reference='P9999999999999999',
    billing_address=Address(
        city='Beverly Hills',
        country='US',
        house_number_or_name='121',
        postal_code='90210',
        street='Brannan Street',
        state_or_province='CA'
    ),
    card=Card(
        expiry_month='03',
        expiry_year='2030',
        holder_name='John Smith',
        number='4111111111111111'
    ),
    shopper_name=Name(
        first_name='John',
        last_name='Smith'
    )
)

result = instant_payouts_api.post_payout(
    body=body
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - a problem reading or understanding the request. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |
| 401 | Unauthorized - authentication required. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |

