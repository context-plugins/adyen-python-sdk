
# Modify Request

## Structure

`ModifyRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `additional_data` | `Dict[str, str]` | Optional | This field contains additional data, which may be required for a particular payout request. |
| `merchant_account` | `str` | Required | The merchant account identifier, with which you want to process the transaction. |
| `original_reference` | `str` | Required | The PSP reference received in the `/submitThirdParty` response. |

## Example

```python
from adyen.models.modify_request import ModifyRequest

modify_request = ModifyRequest(
    merchant_account='merchantAccount2',
    original_reference='originalReference6',
    additional_data={
        'key0': 'additionalData0'
    }
)
```

