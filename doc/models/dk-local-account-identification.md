
# DK Local Account Identification

## Structure

`DKLocalAccountIdentification`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_number` | `str` | Required | The 4-10 digits bank account number (Kontonummer) (without separators or whitespace).<br><br>**Constraints**: *Minimum Length*: `4`, *Maximum Length*: `10` |
| `bank_code` | `str` | Required | The 4-digit bank code (Registreringsnummer) (without separators or whitespace).<br><br>**Constraints**: *Minimum Length*: `4`, *Maximum Length*: `4` |
| `mtype` | `str` | Required, Constant | **dkLocal**<br><br>**Value**: `"dkLocal"` |

## Example

```python
from adyen.models.dk_local_account_identification import DKLocalAccountIdentification

dk_local_account_identification = DKLocalAccountIdentification(
    account_number='accountNumber0',
    bank_code='bankCode2'
)
```

