
# UK Local Account Identification

## Structure

`UKLocalAccountIdentification`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_number` | `str` | Required | The 8-digit bank account number, without separators or whitespace.<br><br>**Constraints**: *Minimum Length*: `8`, *Maximum Length*: `8` |
| `sort_code` | `str` | Required | The 6-digit [sort code](https://en.wikipedia.org/wiki/Sort_code), without separators or whitespace.<br><br>**Constraints**: *Minimum Length*: `6`, *Maximum Length*: `6` |
| `mtype` | `str` | Required, Constant | **ukLocal**<br><br>**Value**: `"ukLocal"` |

## Example

```python
from adyen.models.uk_local_account_identification import UKLocalAccountIdentification

uk_local_account_identification = UKLocalAccountIdentification(
    account_number='accountNumber6',
    sort_code='sortCode4'
)
```

