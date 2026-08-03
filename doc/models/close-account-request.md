
# Close Account Request

*This model accepts additional fields of type Any.*

## Structure

`CloseAccountRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_code` | `str` | Required | The code of account to be closed. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.close_account_request import CloseAccountRequest

close_account_request = CloseAccountRequest(
    account_code='accountCode0',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

