# Rates

```python
rates_api = client.rates
```

## Class Name

`RatesApi`


# Post-Rates-Calculate

Returns the calculated amounts and rates required to convert the currency of a transaction.

:information_source: **Note** This endpoint does not require authentication.

```python
def post_rates_calculate(self,
                        body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`CalculateRateRequest`](../../doc/models/calculate-rate-request.md) | Body, Required | - |

## Response Type

**200**: Successful operation

[`CalculateRateResponse`](../../doc/models/calculate-rate-response.md)

## Example Usage

```python
body = CalculateRateRequest(
    exchange_calculations=[
        CalculateRateRequestItem(
            exchange_side=ExchangeSide2Enum.BUY,
            source_amount=Amount19(
                currency='CZK',
                value=112300
            ),
            target_currency='EUR',
            mtype=RateType2Enum.SPLITPAYMENT
        ),
        CalculateRateRequestItem(
            exchange_side=ExchangeSide2Enum.SELL,
            source_amount=Amount19(
                currency='CZK',
                value=24000
            ),
            target_currency='USD',
            mtype=RateType2Enum.SPLITREFUND
        )
    ]
)

result = rates_api.post_rates_calculate(body)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "exchangeCalculations": [
    {
      "type": "splitPayment",
      "exchangeSide": "buy",
      "sourceAmount": {
        "value": 112300,
        "currency": "CZK"
      },
      "targetAmount": {
        "value": 4480,
        "currency": "EUR"
      },
      "appliedExchangeRate": 0.039893143366
    },
    {
      "type": "splitRefund",
      "exchangeSide": "sell",
      "sourceAmount": {
        "value": 24000,
        "currency": "CZK"
      },
      "targetAmount": {
        "value": 992,
        "currency": "USD"
      },
      "appliedExchangeRate": 0.0413333333333
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |
| 403 | Forbidden | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |

