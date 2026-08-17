
# Counterparty 11

Contains information about the party that receives the payment funds.

## Structure

`Counterparty11`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_holder` | [`AccountHolder11`](../../doc/models/account-holder-11.md) | Required | Contains the full name of the person or entity that receives the payment funds). |
| `account_identification` | [`AccountIdentification1`](../../doc/models/account-identification-1.md) | Required | Contains the account number to which the payment funds are sent. |

## Example

```python
from adyen.models.account_holder_11 import AccountHolder11
from adyen.models.account_identification_1 import AccountIdentification1
from adyen.models.counterparty_11 import Counterparty11

counterparty_11 = Counterparty11(
    account_holder=AccountHolder11(
        full_name='John Doe'
    ),
    account_identification=AccountIdentification1(
        mtype='AccountIdentification1'
    )
)
```

