
# Close Stores Request

*This model accepts additional fields of type Any.*

## Structure

`CloseStoresRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_holder_code` | `str` | Required | The code of the account holder. |
| `stores` | `List[str]` | Required | List of stores to be closed. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.close_stores_request import CloseStoresRequest

close_stores_request = CloseStoresRequest(
    account_holder_code='accountHolderCode2',
    stores=[
        'stores7',
        'stores8'
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

