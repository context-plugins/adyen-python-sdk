
# Account Holder 1

## Structure

`AccountHolder1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `full_name` | `str` | Required | Full name of the account holder.<br><br>**Constraints**: *Minimum Length*: `1` |

## Example

```python
from adyen.models.account_holder_1 import AccountHolder1

account_holder_1 = AccountHolder1(
    full_name='John Doe'
)
```

