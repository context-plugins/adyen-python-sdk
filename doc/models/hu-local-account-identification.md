
# HU Local Account Identification

## Structure

`HULocalAccountIdentification`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_number` | `str` | Required | The 24-digit bank account number, without separators or whitespace.<br><br>**Constraints**: *Minimum Length*: `24`, *Maximum Length*: `24` |
| `mtype` | `str` | Required, Constant | **huLocal**<br><br>**Value**: `"huLocal"` |

## Example

```python
from adyen.models.hu_local_account_identification import HULocalAccountIdentification

hu_local_account_identification = HULocalAccountIdentification(
    account_number='accountNumber4'
)
```

