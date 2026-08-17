
# Debit Account Holder Response

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

## Example

```python
from adyen.models.debit_account_holder_response import DebitAccountHolderResponse
from adyen.models.error_field_type import ErrorFieldType
from adyen.models.field_name_enum import FieldNameEnum
from adyen.models.field_type import FieldType

debit_account_holder_response = DebitAccountHolderResponse(
    account_holder_code='accountHolderCode8',
    bank_account_uuid='bankAccountUUID2',
    invalid_fields=[
        ErrorFieldType(
            error_code=78,
            error_description='errorDescription6',
            field_type=FieldType(
                field='field6',
                field_name=FieldNameEnum.DRIVINGLICENCEFRONT,
                shareholder_code='shareholderCode0'
            )
        ),
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
    merchant_references=[
        'merchantReferences1',
        'merchantReferences2'
    ],
    psp_reference='pspReference2'
)
```

