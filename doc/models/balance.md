
# Balance

## Structure

`Balance`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `available` | `int` | Required | The balance available for use. |
| `balance` | `int` | Required | The sum of the transactions that have already been settled. |
| `currency` | `str` | Required | The three-character [ISO currency code](https://docs.adyen.com/development-resources/currency-codes) of the balance. |
| `pending` | `int` | Optional | The sum of the transactions that will be settled in the future. |
| `pending_available` | `int` | Optional | The balance that will become the available balance after the pending balance is settled.<br><br>The pending available balance is equal to the lower of the following:<br><br>- The `pending` balance<br>- The `pending` balance plus the `available` balance. |
| `reserved` | `int` | Required | The balance currently held in reserve. |

## Example

```python
from adyen.models.balance import Balance

balance = Balance(
    available=248,
    balance=128,
    currency='currency4',
    reserved=62,
    pending=56,
    pending_available=248
)
```

