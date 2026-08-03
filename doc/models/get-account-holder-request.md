
# Get Account Holder Request

*This model accepts additional fields of type Any.*

## Structure

`GetAccountHolderRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_code` | `str` | Optional | The code of the account of which to retrieve the details.<br><br>> Required if no `accountHolderCode` is provided. |
| `account_holder_code` | `str` | Optional | The code of the account holder of which to retrieve the details.<br><br>> Required if no `accountCode` is provided. |
| `show_details` | `bool` | Optional | True if the request should return the account holder details |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.get_account_holder_request import GetAccountHolderRequest

get_account_holder_request = GetAccountHolderRequest(
    account_code='accountCode0',
    account_holder_code='accountHolderCode4',
    show_details=False,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

