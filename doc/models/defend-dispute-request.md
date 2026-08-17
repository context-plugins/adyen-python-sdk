
# Defend Dispute Request

## Structure

`DefendDisputeRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `defense_reason_code` | `str` | Required | The defense reason code that was selected to defend this dispute. |
| `dispute_psp_reference` | `str` | Required | The PSP reference assigned to the dispute. |
| `merchant_account_code` | `str` | Required | The merchant account identifier, for which you want to process the dispute transaction. |

## Example

```python
from adyen.models.defend_dispute_request import DefendDisputeRequest

defend_dispute_request = DefendDisputeRequest(
    defense_reason_code='defenseReasonCode6',
    dispute_psp_reference='disputePspReference4',
    merchant_account_code='merchantAccountCode6'
)
```

