
# Terminal Assignment 2

Indicates the account level to which the terminal is assigned, the [assignment status](https://docs.adyen.com/point-of-sale/automating-terminal-management/assign-terminals-api), and where the terminals is in the process of being reassigned to.

## Structure

`TerminalAssignment2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `company_id` | `str` | Required | The unique identifier of the company account to which terminal is assigned. |
| `merchant_id` | `str` | Optional | The unique identifier of the merchant account to which terminal is assigned. |
| `reassignment_target` | [`TerminalReassignmentTarget2`](../../doc/models/terminal-reassignment-target-2.md) | Optional | Indicates where the terminal is in the process of being reassigned to. |
| `status` | [`Status21Enum`](../../doc/models/status-21-enum.md) | Required | The status of the reassignment. Possible values:<br><br>* `reassignmentInProgress`: the terminal was boarded and is now scheduled to remove the configuration. Wait for the terminal to synchronize with the Adyen platform.<br>* `deployed`: the terminal is deployed and reassigned.<br>* `inventory`: the terminal is in inventory and cannot process transactions.<br>* `boarded`: the terminal is boarded to a store, or a merchant account representing a store, and can process transactions. |
| `store_id` | `str` | Optional | The unique identifier of the store to which terminal is assigned. |

## Example

```python
from adyen.models.status_21_enum import Status21Enum
from adyen.models.terminal_assignment_2 import TerminalAssignment2
from adyen.models.terminal_reassignment_target_2 import TerminalReassignmentTarget2

terminal_assignment_2 = TerminalAssignment2(
    company_id='companyId0',
    status=Status21Enum.BOARDED,
    merchant_id='merchantId6',
    reassignment_target=TerminalReassignmentTarget2(
        inventory=False,
        company_id='companyId4',
        merchant_id='merchantId0',
        store_id='storeId8'
    ),
    store_id='storeId4'
)
```

