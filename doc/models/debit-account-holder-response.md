
# Debit Account Holder Response

*This model accepts additional fields of type Any.*

## Structure

`DebitAccountHolderResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_holder_code` | `str` | Optional | The code of the account holder. |
| `bank_account_uuid` | `str` | Optional | The Adyen-generated unique alphanumeric identifier (UUID) of the account holder's bank account. |
| `invalid_fields` | [`List[ErrorFieldType]`](../../doc/models/error-field-type.md) | Optional | Contains field validation errors that would prevent requests from being processed. |
| `merchant_references` | `List[str]` | Optional | List of the `reference` values from the `split` array in the request. |
| `psp_reference` | `str` | Optional | The reference of a request. Can be used to uniquely identify the request. |
| `result_code` | `str` | Optional | The result code. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.debit_account_holder_response import DebitAccountHolderResponse
from adyen.models.error_field_type import ErrorFieldType
from adyen.models.field_name import FieldName
from adyen.models.field_type_2 import FieldType2

debit_account_holder_response = DebitAccountHolderResponse(
    account_holder_code='accountHolderCode8',
    bank_account_uuid='bankAccountUUID2',
    invalid_fields=[
        ErrorFieldType(
            error_code=78,
            error_description='errorDescription6',
            field_type=FieldType2(
                field='field6',
                field_name=FieldName.DRIVINGLICENCEFRONT,
                shareholder_code='shareholderCode0',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        ErrorFieldType(
            error_code=78,
            error_description='errorDescription6',
            field_type=FieldType2(
                field='field6',
                field_name=FieldName.DRIVINGLICENCEFRONT,
                shareholder_code='shareholderCode0',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    merchant_references=[
        'merchantReferences1',
        'merchantReferences2'
    ],
    psp_reference='pspReference2',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

