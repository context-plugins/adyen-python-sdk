
# Authentication Result Request

## Structure

`AuthenticationResultRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `merchant_account` | `str` | Required | The merchant account identifier, with which the authentication was processed. |
| `psp_reference` | `str` | Required | The pspReference identifier for the transaction. |

## Example

```python
from adyen.models.authentication_result_request import AuthenticationResultRequest

authentication_result_request = AuthenticationResultRequest(
    merchant_account='merchantAccount2',
    psp_reference='pspReference2'
)
```

