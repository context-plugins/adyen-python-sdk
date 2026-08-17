
# SG Local Account Identification

## Structure

`SGLocalAccountIdentification`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_number` | `str` | Required | The 4- to 19-digit bank account number, without separators or whitespace.<br><br>**Constraints**: *Minimum Length*: `4`, *Maximum Length*: `19` |
| `bic` | `str` | Required | The bank's 8- or 11-character BIC or SWIFT code.<br><br>**Constraints**: *Minimum Length*: `8`, *Maximum Length*: `11` |
| `mtype` | [`Type82Enum`](../../doc/models/type-82-enum.md) | Optional | **sgLocal**<br><br>**Default**: `"sgLocal"` |

## Example

```python
from adyen.models.sg_local_account_identification import SGLocalAccountIdentification
from adyen.models.type_82_enum import Type82Enum

sg_local_account_identification = SGLocalAccountIdentification(
    account_number='accountNumber4',
    bic='bic8',
    mtype=Type82Enum.SGLOCAL
)
```

