
# Capital Balance

An object containing the details of the existing grant., Contains information about the balances of the disbursement., Contains information about the balances of the grant.

## Structure

`CapitalBalance`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `currency` | `str` | Required | The three-character [ISO currency code](https://docs.adyen.com/development-resources/currency-codes). |
| `fee` | `int` | Required | Fee amount. |
| `principal` | `int` | Required | Principal amount. |
| `total` | `int` | Required | Total amount. A sum of principal amount and fee amount. |

## Example

```python
from adyen.models.capital_balance import CapitalBalance

capital_balance = CapitalBalance(
    currency='currency0',
    fee=236,
    principal=18,
    total=198
)
```

