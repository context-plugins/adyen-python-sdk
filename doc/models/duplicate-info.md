
# Duplicate Info

## Structure

`DuplicateInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `duplicate_transaction_id` | `str` | Required | The transaction id associated with the duplicate charge for which you are disputing. The disputed transaction must be in the same amount as the duplicate transaction.<br><br>**Constraints**: *Minimum Length*: `1` |
| `same_card` | `bool` | Required | The duplicate charge was made on the same card. Possible values: **true**, **false**. |
| `same_issuer` | `bool` | Optional | The issuer associated with each charge is the same. Possible values: **true**, **false**. |

## Example

```python
from adyen.models.duplicate_info import DuplicateInfo

duplicate_info = DuplicateInfo(
    duplicate_transaction_id='duplicateTransactionId8',
    same_card=False,
    same_issuer=False
)
```

