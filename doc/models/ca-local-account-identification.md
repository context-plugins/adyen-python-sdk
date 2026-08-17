
# CA Local Account Identification

## Structure

`CALocalAccountIdentification`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_number` | `str` | Required | The 5- to 12-digit bank account number, without separators or whitespace.<br><br>**Constraints**: *Minimum Length*: `5`, *Maximum Length*: `12` |
| `account_type` | [`AccountType2Enum`](../../doc/models/account-type-2-enum.md) | Optional | The bank account type.<br><br>Possible values: **checking** or **savings**. Defaults to **checking**.<br><br>**Default**: `"checking"` |
| `institution_number` | `str` | Required | The 3-digit institution number, without separators or whitespace.<br><br>**Constraints**: *Minimum Length*: `3`, *Maximum Length*: `3` |
| `transit_number` | `str` | Required | The 5-digit transit number, without separators or whitespace.<br><br>**Constraints**: *Minimum Length*: `5`, *Maximum Length*: `5` |
| `mtype` | `str` | Required, Constant | **caLocal**<br><br>**Value**: `"caLocal"` |

## Example

```python
from adyen.models.account_type_2_enum import AccountType2Enum
from adyen.models.ca_local_account_identification import CALocalAccountIdentification

ca_local_account_identification = CALocalAccountIdentification(
    account_number='accountNumber2',
    institution_number='institutionNumber4',
    transit_number='transitNumber2',
    account_type=AccountType2Enum.CHECKING
)
```

