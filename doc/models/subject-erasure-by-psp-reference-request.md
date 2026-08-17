
# Subject Erasure by Psp Reference Request

## Structure

`SubjectErasureByPspReferenceRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `force_erasure` | `bool` | Optional | Set this to **true** if you want to delete shopper-related data, even if the shopper has an existing recurring transaction. This only deletes the shopper-related data for the specific payment, but does not cancel the existing recurring transaction. |
| `merchant_account` | `str` | Optional | Your merchant account |
| `psp_reference` | `str` | Optional | The PSP reference of the payment. We will delete all shopper-related data for this payment. |

## Example

```python
from adyen.models.subject_erasure_by_psp_reference_request import SubjectErasureByPspReferenceRequest

subject_erasure_by_psp_reference_request = SubjectErasureByPspReferenceRequest(
    force_erasure=False,
    merchant_account='merchantAccount6',
    psp_reference='pspReference4'
)
```

