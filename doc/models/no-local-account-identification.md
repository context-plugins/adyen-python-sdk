
# NO Local Account Identification

## Structure

`NOLocalAccountIdentification`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_number` | `str` | Required | The 11-digit bank account number, without separators or whitespace.<br><br>**Constraints**: *Minimum Length*: `11`, *Maximum Length*: `11` |
| `mtype` | `str` | Required, Constant | **noLocal**<br><br>**Value**: `"noLocal"` |

## Example

```python
from adyen.models.no_local_account_identification import NOLocalAccountIdentification

no_local_account_identification = NOLocalAccountIdentification(
    account_number='accountNumber6'
)
```

