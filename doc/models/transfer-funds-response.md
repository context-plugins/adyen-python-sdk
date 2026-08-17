
# Transfer Funds Response

## Structure

`TransferFundsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `invalid_fields` | [`List[ErrorFieldType]`](../../doc/models/error-field-type.md) | Optional | Contains field validation errors that would prevent requests from being processed. |
| `merchant_reference` | `str` | Optional | The value supplied by the executing user when initiating the transfer; may be used to link multiple transactions. |
| `psp_reference` | `str` | Optional | The reference of a request. Can be used to uniquely identify the request. |
| `result_code` | `str` | Optional | The result code. |

## Example

```python
from adyen.models.error_field_type import ErrorFieldType
from adyen.models.field_name_enum import FieldNameEnum
from adyen.models.field_type import FieldType
from adyen.models.transfer_funds_response import TransferFundsResponse

transfer_funds_response = TransferFundsResponse(
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
    merchant_reference='merchantReference2',
    psp_reference='pspReference4',
    result_code='resultCode0'
)
```

