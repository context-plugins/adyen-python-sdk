
# Terminal Reassignment Target 2

Indicates where the terminal is in the process of being reassigned to.

## Structure

`TerminalReassignmentTarget2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `company_id` | `str` | Optional | The unique identifier of the company account to which the terminal is reassigned. |
| `inventory` | `bool` | Required | Indicates if the terminal is reassigned to the inventory of the merchant account.<br><br>- If **true**, the terminal is in the inventory of the merchant account and cannot process transactions.<br>- If **false**, the terminal is reassigned directly to the merchant account and can process transactions. |
| `merchant_id` | `str` | Optional | The unique identifier of the merchant account to which the terminal is reassigned. |
| `store_id` | `str` | Optional | The unique identifier of the store to which the terminal is reassigned. |

## Example

```python
from adyen.models.terminal_reassignment_target_2 import TerminalReassignmentTarget2

terminal_reassignment_target_2 = TerminalReassignmentTarget2(
    inventory=False,
    company_id='companyId0',
    merchant_id='merchantId6',
    store_id='storeId4'
)
```

