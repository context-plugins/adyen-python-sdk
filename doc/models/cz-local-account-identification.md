
# CZ Local Account Identification

## Structure

`CZLocalAccountIdentification`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_number` | `str` | Required | The 2- to 16-digit bank account number (Číslo účtu) in the following format:<br><br>- The optional prefix (předčíslí).<br><br>- The required second part (základní část) which must be at least two non-zero digits.<br><br>Examples:<br><br>- **19-123457** (with prefix)<br><br>- **123457** (without prefix)<br><br>- **000019-0000123457** (with prefix, normalized)<br><br>- **000000-0000123457** (without prefix, normalized)<br><br>**Constraints**: *Minimum Length*: `2`, *Maximum Length*: `17` |
| `bank_code` | `str` | Required | The 4-digit bank code (Kód banky), without separators or whitespace.<br><br>**Constraints**: *Minimum Length*: `4`, *Maximum Length*: `4` |
| `mtype` | `str` | Required, Constant | **czLocal**<br><br>**Value**: `"czLocal"` |

## Example

```python
from adyen.models.cz_local_account_identification import CZLocalAccountIdentification

cz_local_account_identification = CZLocalAccountIdentification(
    account_number='accountNumber8',
    bank_code='bankCode0'
)
```

