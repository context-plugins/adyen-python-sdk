
# Assign Terminals Request

## Structure

`AssignTerminalsRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `company_account` | `str` | Required | Your company account. To return terminals to the company inventory, specify only this parameter and the `terminals`. |
| `merchant_account` | `str` | Optional | Name of the merchant account. Specify this parameter to assign terminals to this merchant account or to a store under this merchant account. |
| `merchant_inventory` | `bool` | Optional | Boolean that indicates if you are assigning the terminals to the merchant inventory. Do not use when assigning terminals to a store. Required when assigning the terminal to a merchant account.<br><br>- Set this to **true** to assign the terminals to the merchant inventory. This also means that the terminals cannot be boarded.<br><br>- Set this to **false** to assign the terminals to the merchant account as in-store terminals. This makes the terminals ready to be boarded and to process payments through the specified merchant account. |
| `store` | `str` | Optional | The store code of the store that you want to assign the terminals to. |
| `terminals` | `List[str]` | Required | Array containing a list of terminal IDs that you want to assign or reassign to the merchant account or store, or that you want to return to the company inventory.<br><br>For example, `["V400m-324689776","P400Plus-329127412"]`. |

## Example

```python
from adyen.models.assign_terminals_request import AssignTerminalsRequest

assign_terminals_request = AssignTerminalsRequest(
    company_account='companyAccount4',
    terminals=[
        'terminals7'
    ],
    merchant_account='merchantAccount2',
    merchant_inventory=False,
    store='store0'
)
```

