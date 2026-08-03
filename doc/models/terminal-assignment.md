
# Terminal Assignment

*This model accepts additional fields of type Any.*

## Structure

`TerminalAssignment`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `company_id` | `str` | Required | The unique identifier of the company account to which terminal is assigned. |
| `merchant_id` | `str` | Optional | The unique identifier of the merchant account to which terminal is assigned. |
| `reassignment_target` | [`TerminalReassignmentTarget`](../../doc/models/terminal-reassignment-target.md) | Optional | - |
| `status` | [`Status24`](../../doc/models/status-24.md) | Required | - |
| `store_id` | `str` | Optional | The unique identifier of the store to which terminal is assigned. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.status_24 import Status24
from adyen.models.terminal_assignment import TerminalAssignment
from adyen.models.terminal_reassignment_target import TerminalReassignmentTarget

terminal_assignment = TerminalAssignment(
    company_id='companyId0',
    status=Status24.INVENTORY,
    merchant_id='merchantId6',
    reassignment_target=TerminalReassignmentTarget(
        inventory=False,
        company_id='companyId4',
        merchant_id='merchantId0',
        store_id='storeId8',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    store_id='storeId6',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

