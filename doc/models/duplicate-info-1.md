
# Duplicate Info 1

Additional information for raising a dispute of `type` **duplicate**. Required for disputes of `type` **duplicate**.

*This model accepts additional fields of type Any.*

## Structure

`DuplicateInfo1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `duplicate_transaction_id` | `str` | Required | The transaction id associated with the duplicate charge for which you are disputing. The disputed transaction must be in the same amount as the duplicate transaction.<br><br>**Constraints**: *Minimum Length*: `1` |
| `same_card` | `bool` | Required | The duplicate charge was made on the same card. Possible values: **true**, **false**. |
| `same_issuer` | `bool` | Optional | The issuer associated with each charge is the same. Possible values: **true**, **false**. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.duplicate_info_1 import DuplicateInfo1

duplicate_info_1 = DuplicateInfo1(
    duplicate_transaction_id='duplicateTransactionId0',
    same_card=False,
    same_issuer=False,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

