
# Close Account Holder Request

*This model accepts additional fields of type Any.*

## Structure

`CloseAccountHolderRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_holder_code` | `str` | Required | The code of the Account Holder to be closed. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.close_account_holder_request import CloseAccountHolderRequest

close_account_holder_request = CloseAccountHolderRequest(
    account_holder_code='accountHolderCode0',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

