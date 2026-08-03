
# Terminal Reassignment Request

*This model accepts additional fields of type Any.*

## Structure

`TerminalReassignmentRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `company_id` | `str` | Optional | The unique identifier of the company account to which the terminal is reassigned. |
| `inventory` | `bool` | Optional | Must be specified when reassigning terminals to a merchant account:<br><br>- If set to **true**, reassigns terminals to the inventory of the merchant account and the terminals cannot process transactions.<br><br>- If set to **false**, reassigns terminals directly to the merchant account and the terminals can process transactions. |
| `merchant_id` | `str` | Optional | The unique identifier of the merchant account to which the terminal is reassigned. When reassigning terminals to a merchant account, you must specify the `inventory` field. |
| `store_id` | `str` | Optional | The unique identifier of the store to which the terminal is reassigned. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.terminal_reassignment_request import TerminalReassignmentRequest

terminal_reassignment_request = TerminalReassignmentRequest(
    company_id='companyId2',
    inventory=False,
    merchant_id='merchantId8',
    store_id='storeId4',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

