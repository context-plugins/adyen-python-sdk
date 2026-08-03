
# Delete Shareholder Request

*This model accepts additional fields of type Any.*

## Structure

`DeleteShareholderRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_holder_code` | `str` | Required | The code of the Account Holder from which to delete the Shareholders. |
| `shareholder_codes` | `List[str]` | Required | The code(s) of the Shareholders to be deleted. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.delete_shareholder_request import DeleteShareholderRequest

delete_shareholder_request = DeleteShareholderRequest(
    account_holder_code='accountHolderCode8',
    shareholder_codes=[
        'shareholderCodes7',
        'shareholderCodes8'
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

