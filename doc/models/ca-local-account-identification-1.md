
# CA Local Account Identification 1

## Structure

`CALocalAccountIdentification1`

## Inherits From

[`BankAccountIdentification`](../../doc/models/bank-account-identification.md)

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_number` | `str` | Required | The 5- to 12-digit bank account number, without separators or whitespace.<br><br>**Constraints**: *Minimum Length*: `5`, *Maximum Length*: `12` |
| `account_type` | [`AccountType2Enum`](../../doc/models/account-type-2-enum.md) | Optional | The bank account type.<br><br>Possible values: **checking** or **savings**. Defaults to **checking**. |
| `institution_number` | `str` | Required | The 3-digit institution number, without separators or whitespace.<br><br>**Constraints**: *Minimum Length*: `3`, *Maximum Length*: `3` |
| `transit_number` | `str` | Required | The 5-digit transit number, without separators or whitespace.<br><br>**Constraints**: *Minimum Length*: `5`, *Maximum Length*: `5` |

## Example

```python
from adyen.models.account_type_2_enum import AccountType2Enum
from adyen.models.bank_account_identification import CALocalAccountIdentification1

ca_local_account_identification_1 = CALocalAccountIdentification1(
    account_number='accountNumber8',
    institution_number='institutionNumber2',
    transit_number='transitNumber8',
    account_type=AccountType2Enum.CHECKING,
    mtype='caLocal'
)
```

