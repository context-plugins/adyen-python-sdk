
# Account Identification 1

Contains the account number to which the payment funds are sent.

## Structure

`AccountIdentification1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | `str` | Optional | - |

## Example

```python
from adyen.models.account_identification_1 import AccountIdentification1

account_identification_1 = AccountIdentification1(
    mtype='AccountIdentification1'
)
```

