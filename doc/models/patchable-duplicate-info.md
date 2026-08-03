
# Patchable Duplicate Info

*This model accepts additional fields of type Any.*

## Structure

`PatchableDuplicateInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `duplicate_transaction_id` | `str` | Optional | The transaction id associated with the duplicate charge for which you are disputing. The disputed transaction must be in the same amount as the duplicate transaction.<br><br>**Constraints**: *Minimum Length*: `1` |
| `same_card` | `bool` | Optional | The duplicate charge was made on the same card. Possible values: **true**, **false**. |
| `same_issuer` | `bool` | Optional | The issuer associated with each charge is the same. Possible values: **true**, **false**. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.patchable_duplicate_info import PatchableDuplicateInfo

patchable_duplicate_info = PatchableDuplicateInfo(
    duplicate_transaction_id='duplicateTransactionId8',
    same_card=False,
    same_issuer=False,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

