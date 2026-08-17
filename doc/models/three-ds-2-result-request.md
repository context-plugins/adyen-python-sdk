
# Three DS 2 Result Request

## Structure

`ThreeDS2ResultRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `merchant_account` | `str` | Required | The merchant account identifier, with which you want to process the transaction. |
| `psp_reference` | `str` | Required | The pspReference returned in the /authorise call. |

## Example

```python
from adyen.models.three_ds_2_result_request import ThreeDS2ResultRequest

three_ds_2_result_request = ThreeDS2ResultRequest(
    merchant_account='merchantAccount8',
    psp_reference='pspReference8'
)
```

