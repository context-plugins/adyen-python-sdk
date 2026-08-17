
# BR Local Account Identification

## Structure

`BRLocalAccountIdentification`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_number` | `str` | Required | The bank account number, without separators or whitespace.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `10` |
| `bank_code` | `str` | Required | The 3-digit bank code, with leading zeros.<br><br>**Constraints**: *Minimum Length*: `3`, *Maximum Length*: `3` |
| `branch_number` | `str` | Required | The bank account branch number, without separators or whitespace.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `4` |
| `ispb` | `str` | Optional | The 8-digit ISPB, with leading zeros.<br><br>**Constraints**: *Minimum Length*: `8`, *Maximum Length*: `8` |
| `mtype` | `str` | Required, Constant | **brLocal**<br><br>**Value**: `"brLocal"` |

## Example

```python
from adyen.models.br_local_account_identification import BRLocalAccountIdentification

br_local_account_identification = BRLocalAccountIdentification(
    account_number='accountNumber6',
    bank_code='bankCode6',
    branch_number='branchNumber6',
    ispb='ispb0'
)
```

