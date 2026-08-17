
# Delete Signatories Request

## Structure

`DeleteSignatoriesRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_holder_code` | `str` | Required | The code of the account holder from which to delete the signatories. |
| `signatory_codes` | `List[str]` | Required | Array of codes of the signatories to be deleted. |

## Example

```python
from adyen.models.delete_signatories_request import DeleteSignatoriesRequest

delete_signatories_request = DeleteSignatoriesRequest(
    account_holder_code='accountHolderCode2',
    signatory_codes=[
        'signatoryCodes3',
        'signatoryCodes4'
    ]
)
```

