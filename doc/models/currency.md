
# Currency

## Structure

`Currency`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount` | `int` | Optional | Surcharge amount per transaction, in [minor units](https://docs.adyen.com/development-resources/currency-codes). |
| `currency_code` | `str` | Required | Three-character [ISO currency code](https://docs.adyen.com/development-resources/currency-codes). For example, **AUD**. |
| `max_amount` | `int` | Optional | The maximum surcharge amount per transaction, in [minor units](https://docs.adyen.com/development-resources/currency-codes). |
| `percentage` | `float` | Optional | Surcharge percentage per transaction. The maximum number of decimal places is two. For example, **1%** or **2.27%**. |

## Example

```python
from adyen.models.currency import Currency

currency = Currency(
    currency_code='currencyCode0',
    amount=158,
    max_amount=148,
    percentage=85.58
)
```

