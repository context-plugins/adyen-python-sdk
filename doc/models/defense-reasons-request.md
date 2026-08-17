
# Defense Reasons Request

## Structure

`DefenseReasonsRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `dispute_psp_reference` | `str` | Required | The PSP reference assigned to the dispute. |
| `merchant_account_code` | `str` | Required | The merchant account identifier, for which you want to process the dispute transaction. |

## Example

```python
from adyen.models.defense_reasons_request import DefenseReasonsRequest

defense_reasons_request = DefenseReasonsRequest(
    dispute_psp_reference='disputePspReference0',
    merchant_account_code='merchantAccountCode2'
)
```

