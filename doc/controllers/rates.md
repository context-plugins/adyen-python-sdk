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
| `body` | [`RatesCalculateRequest`](../../doc/models/rates-calculate-request.md) | Body, Required | - |

## Response Type

**200**: Successful operation

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`RatesCalculateResponse`](../../doc/models/rates-calculate-response.md).

## Example Usage

```python
body = RatesCalculateRequest(
    exchange_calculations=[
        CalculateRateRequestItem(
            exchange_side=ExchangeSide2.BUY,
            source_amount=SourceAmount(
                currency='CZK',
                value=112300
            ),
            target_currency='EUR',
            mtype=RateType2.SPLITPAYMENT
        ),
        CalculateRateRequestItem(
            exchange_side=ExchangeSide2.SELL,
            source_amount=SourceAmount(
                currency='CZK',
                value=24000
            ),
            target_currency='USD',
            mtype=RateType2.SPLITREFUND
        )
    ]
)

result = rates_api.post_rates_calculate(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
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
| 401 | Unauthorized | [`RatesCalculate401ErrorException`](../../doc/models/rates-calculate-401-error-exception.md) |
| 403 | Forbidden | [`RatesCalculate403ErrorException`](../../doc/models/rates-calculate-403-error-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`RatesCalculate422ErrorException`](../../doc/models/rates-calculate-422-error-exception.md) |

