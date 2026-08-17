
# Modify Response

## Structure

`ModifyResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `additional_data` | `Dict[str, str]` | Optional | This field contains additional data, which may be returned in a particular response. |
| `psp_reference` | `str` | Required | Adyen's 16-character string reference associated with the transaction. This value is globally unique; quote it when communicating with us about this response. |
| `response` | `str` | Required | The response:<br><br>* In case of success, it is either `payout-confirm-received` or `payout-decline-received`.<br>* In case of an error, an informational message is returned. |

## Example

```python
from adyen.models.modify_response import ModifyResponse

modify_response = ModifyResponse(
    psp_reference='pspReference4',
    response='response2',
    additional_data={
        'key0': 'additionalData2',
        'key1': 'additionalData3'
    }
)
```

