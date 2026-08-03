# Cash Out

```python
cash_out_api = client.cash_out
```

## Class Name

`CashOutApi`


# Post-Cashouts

Initiates a [cashout](https://docs.adyen.com/platforms/cash-out-instantly) request.

:information_source: **Note** This endpoint does not require authentication.

```python
def post_cashouts(self,
                 body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`CashOutInfo`](../../doc/models/cash-out-info.md) | Body, Required | - |

## Response Type

**200**: OK - The request has succeeded.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`CashOut`](../../doc/models/cash-out.md).

## Example Usage

```python
body = CashOutInfo(
    amount=Amount5(
        currency='EUR',
        value=50000
    ),
    instructing_balance_account_id='BA00000000000000000000001',
    counterparty=CashOutInfoCounterparty(
        transfer_instrument_id='SE00000000000000000000001'
    ),
    description='Cashout to bank account',
    fee=Fee2(
        amount=Amount5(
            currency='EUR',
            value=500
        )
    ),
    reference_for_beneficiary='CASHOUT-REF-001'
)

result = cash_out_api.post_cashouts(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "id": "CO00000000000000000000001",
  "instructingBalanceAccountId": "BA00000000000000000000001",
  "amount": {
    "currency": "EUR",
    "value": 50000
  },
  "counterparty": {
    "transferInstrumentId": "SE00000000000000000000001"
  },
  "description": "Cashout to bank account",
  "referenceForBeneficiary": "CASHOUT-REF-001",
  "fee": {
    "amount": {
      "currency": "EUR",
      "value": 500
    }
  },
  "transfers": [
    {
      "id": "400F6060JMB1I0AB",
      "type": "cashoutRepayment",
      "amount": {
        "currency": "EUR",
        "value": 50500
      }
    },
    {
      "id": "400F6060JMB1I0AA",
      "type": "cashoutFee",
      "amount": {
        "currency": "EUR",
        "value": 500
      }
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - The request is malformed or is not in the expected format. | [`Cashouts400ErrorException`](../../doc/models/cashouts-400-error-exception.md) |
| 401 | Unauthorized - The API credential used in the request is invalid. | [`Cashouts401ErrorException`](../../doc/models/cashouts-401-error-exception.md) |
| 403 | Forbidden - The API credential does not have the right permissions. | [`Cashouts403ErrorException`](../../doc/models/cashouts-403-error-exception.md) |
| 404 | Not Found - The requested resource was not found. | [`Cashouts404ErrorException`](../../doc/models/cashouts-404-error-exception.md) |
| 422 | Unprocessable Entity - A request validation error. | [`Cashouts422ErrorException`](../../doc/models/cashouts-422-error-exception.md) |
| 429 | Too Many Requests - Request rate limit exceeded. | [`Cashouts429ErrorException`](../../doc/models/cashouts-429-error-exception.md) |
| 500 | Internal Service Error - An unrecoverable error occurred while trying to perform the request. | [`Cashouts500ErrorException`](../../doc/models/cashouts-500-error-exception.md) |

