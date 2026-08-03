
# List Nonprofits Request

*This model accepts additional fields of type Any.*

## Structure

`ListNonprofitsRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_holder_ids` | `List[str]` | Required | The unique identifiers of the account holders to be included in a donation campaign.<br><br>**Constraints**: *Minimum Items*: `1` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.list_nonprofits_request import ListNonprofitsRequest

list_nonprofits_request = ListNonprofitsRequest(
    account_holder_ids=[
        'accountHolderIds1',
        'accountHolderIds2',
        'accountHolderIds3'
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

