
# Refund Funds Transfer Response

## Structure

`RefundFundsTransferResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `invalid_fields` | [`List[ErrorFieldType]`](../../doc/models/error-field-type.md) | Optional | Contains field validation errors that would prevent requests from being processed. |
| `merchant_reference` | `str` | Optional | The value supplied by the executing user when initiating the transfer refund; may be used to link multiple transactions. |
| `message` | `str` | Optional | The message of the response. |
| `original_reference` | `str` | Optional | A PSP reference of the original fund transfer. |
| `psp_reference` | `str` | Optional | The reference of a request. Can be used to uniquely identify the request. |
| `result_code` | `str` | Optional | The result code. |

## Example

```python
from adyen.models.error_field_type import ErrorFieldType
from adyen.models.field_name_enum import FieldNameEnum
from adyen.models.field_type import FieldType
from adyen.models.refund_funds_transfer_response import RefundFundsTransferResponse

refund_funds_transfer_response = RefundFundsTransferResponse(
    invalid_fields=[
        ErrorFieldType(
            error_code=78,
            error_description='errorDescription6',
            field_type=FieldType(
                field='field6',
                field_name=FieldNameEnum.DRIVINGLICENCEFRONT,
                shareholder_code='shareholderCode0'
            )
        )
    ],
    merchant_reference='merchantReference6',
    message='message0',
    original_reference='originalReference6',
    psp_reference='pspReference8'
)
```

