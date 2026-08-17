
# Payout Account Holder Response

## Structure

`PayoutAccountHolderResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `bank_account_uuid` | `str` | Optional | The unique ID of the Bank Account to which the payout was made. |
| `invalid_fields` | [`List[ErrorFieldType]`](../../doc/models/error-field-type.md) | Optional | Contains field validation errors that would prevent requests from being processed. |
| `merchant_reference` | `str` | Optional | The value supplied by the executing user when initiating the transfer; may be used to link multiple transactions. |
| `payout_speed` | [`PayoutSpeedEnum`](../../doc/models/payout-speed-enum.md) | Optional | Speed with which payouts for this account are processed. Permitted values: `STANDARD`, `SAME_DAY`.<br><br>**Default**: `"STANDARD"` |
| `psp_reference` | `str` | Optional | The reference of a request. Can be used to uniquely identify the request. |
| `result_code` | `str` | Optional | The result code. |

## Example

```python
from adyen.models.error_field_type import ErrorFieldType
from adyen.models.field_name_enum import FieldNameEnum
from adyen.models.field_type import FieldType
from adyen.models.payout_account_holder_response import PayoutAccountHolderResponse
from adyen.models.payout_speed_enum import PayoutSpeedEnum

payout_account_holder_response = PayoutAccountHolderResponse(
    bank_account_uuid='bankAccountUUID0',
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
    merchant_reference='merchantReference8',
    payout_speed=PayoutSpeedEnum.STANDARD,
    psp_reference='pspReference6'
)
```

