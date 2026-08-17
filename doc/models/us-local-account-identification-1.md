
# US Local Account Identification 1

## Structure

`USLocalAccountIdentification1`

## Inherits From

[`BankAccountIdentification`](../../doc/models/bank-account-identification.md)

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_number` | `str` | Required | The bank account number, without separators or whitespace.<br><br>**Constraints**: *Minimum Length*: `2`, *Maximum Length*: `18` |
| `account_type` | [`AccountType2Enum`](../../doc/models/account-type-2-enum.md) | Optional | The bank account type.<br><br>Possible values: **checking** or **savings**. Defaults to **checking**. |
| `routing_number` | `str` | Required | The 9-digit [routing number](https://en.wikipedia.org/wiki/ABA_routing_transit_number), without separators or whitespace.<br><br>**Constraints**: *Minimum Length*: `9`, *Maximum Length*: `9` |

## Example

```python
from adyen.models.account_type_2_enum import AccountType2Enum
from adyen.models.bank_account_identification import USLocalAccountIdentification1

us_local_account_identification_1 = USLocalAccountIdentification1(
    account_number='accountNumber6',
    routing_number='routingNumber0',
    account_type=AccountType2Enum.CHECKING,
    mtype='usLocal'
)
```

