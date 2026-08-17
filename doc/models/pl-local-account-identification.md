
# PL Local Account Identification

## Structure

`PLLocalAccountIdentification`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_number` | `str` | Required | The 26-digit bank account number ([Numer rachunku](https://pl.wikipedia.org/wiki/Numer_Rachunku_Bankowego)), without separators or whitespace.<br><br>**Constraints**: *Minimum Length*: `26`, *Maximum Length*: `26` |
| `mtype` | `str` | Required, Constant | **plLocal**<br><br>**Value**: `"plLocal"` |

## Example

```python
from adyen.models.pl_local_account_identification import PLLocalAccountIdentification

pl_local_account_identification = PLLocalAccountIdentification(
    account_number='accountNumber0'
)
```

