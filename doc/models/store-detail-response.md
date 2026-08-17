
# Store Detail Response

## Structure

`StoreDetailResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `additional_data` | `Dict[str, str]` | Optional | This field contains additional data, which may be returned in a particular response. |
| `psp_reference` | `str` | Required | A new reference to uniquely identify this request. |
| `recurring_detail_reference` | `str` | Required | The token which you can use later on for submitting the payout. |
| `result_code` | `str` | Required | The result code of the transaction. `Success` indicates that the details were stored successfully. |

## Example

```python
from adyen.models.store_detail_response import StoreDetailResponse

store_detail_response = StoreDetailResponse(
    psp_reference='pspReference2',
    recurring_detail_reference='recurringDetailReference6',
    result_code='resultCode8',
    additional_data={
        'key0': 'additionalData6'
    }
)
```

