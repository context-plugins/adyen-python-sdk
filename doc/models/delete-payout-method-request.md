
# Delete Payout Method Request

## Structure

`DeletePayoutMethodRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_holder_code` | `str` | Required | The code of the account holder, from which to delete the payout methods. |
| `payout_method_codes` | `List[str]` | Required | The codes of the payout methods to be deleted. |

## Example

```python
from adyen.models.delete_payout_method_request import DeletePayoutMethodRequest

delete_payout_method_request = DeletePayoutMethodRequest(
    account_holder_code='accountHolderCode6',
    payout_method_codes=[
        'payoutMethodCodes6',
        'payoutMethodCodes7'
    ]
)
```

