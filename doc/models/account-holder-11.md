
# Account Holder 11

Contains the full name of the person or entity that receives the payment funds).

## Structure

`AccountHolder11`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `full_name` | `str` | Required | Full name of the account holder.<br><br>**Constraints**: *Minimum Length*: `1` |

## Example

```python
from adyen.models.account_holder_11 import AccountHolder11

account_holder_11 = AccountHolder11(
    full_name='John Doe'
)
```

