
# NZ Local Account Identification

## Structure

`NZLocalAccountIdentification`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_number` | `str` | Required | The 15-16 digit bank account number. The first 2 digits are the bank number, the next 4 digits are the branch number, the next 7 digits are the account number, and the final 2-3 digits are the suffix.<br><br>**Constraints**: *Minimum Length*: `15`, *Maximum Length*: `16` |
| `mtype` | `str` | Required, Constant | **nzLocal**<br><br>**Value**: `"nzLocal"` |

## Example

```python
from adyen.models.nz_local_account_identification import NZLocalAccountIdentification

nz_local_account_identification = NZLocalAccountIdentification(
    account_number='accountNumber0'
)
```

