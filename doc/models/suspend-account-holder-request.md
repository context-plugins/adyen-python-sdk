
# Suspend Account Holder Request

*This model accepts additional fields of type Any.*

## Structure

`SuspendAccountHolderRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_holder_code` | `str` | Required | The code of the account holder to be suspended. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.suspend_account_holder_request import SuspendAccountHolderRequest

suspend_account_holder_request = SuspendAccountHolderRequest(
    account_holder_code='accountHolderCode2',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

