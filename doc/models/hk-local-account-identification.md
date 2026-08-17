
# HK Local Account Identification

## Structure

`HKLocalAccountIdentification`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_number` | `str` | Required | The 9- to 17-digit bank account number, without separators or whitespace. Starts with the 3-digit branch code.<br><br>**Constraints**: *Minimum Length*: `9`, *Maximum Length*: `17` |
| `clearing_code` | `str` | Required | The 3-digit clearing code, without separators or whitespace.<br><br>**Constraints**: *Minimum Length*: `3`, *Maximum Length*: `3` |
| `mtype` | `str` | Required, Constant | **hkLocal**<br><br>**Value**: `"hkLocal"` |

## Example

```python
from adyen.models.hk_local_account_identification import HKLocalAccountIdentification

hk_local_account_identification = HKLocalAccountIdentification(
    account_number='accountNumber4',
    clearing_code='clearingCode0'
)
```

