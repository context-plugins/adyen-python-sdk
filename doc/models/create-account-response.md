
# Create Account Response

## Structure

`CreateAccountResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_code` | `str` | Optional | The code of the new account. |
| `account_holder_code` | `str` | Optional | The code of the account holder. |
| `bank_account_uuid` | `str` | Optional | The bankAccountUUID of the bank account held by the account holder to couple the account with. Scheduled payouts in currencies matching the currency of this bank account will be sent to this bank account. Payouts in different currencies will be sent to a matching bank account of the account holder. |
| `description` | `str` | Optional | The description of the account. |
| `invalid_fields` | [`List[ErrorFieldType]`](../../doc/models/error-field-type.md) | Optional | A list of fields that caused the `/createAccount` request to fail. |
| `metadata` | `Dict[str, str]` | Optional | A set of key and value pairs containing metadata. |
| `payout_method_code` | `str` | Optional | The payout method code held by the account holder to couple the account with. Scheduled card payouts will be sent using this payout method code. |
| `payout_schedule` | [`PayoutScheduleResponse1`](../../doc/models/payout-schedule-response-1.md) | Optional | The details of the payout schedule added to the account. |
| `payout_speed` | [`PayoutSpeedEnum`](../../doc/models/payout-speed-enum.md) | Optional | Speed with which payouts for this account are processed. Permitted values: `STANDARD`, `SAME_DAY`. |
| `psp_reference` | `str` | Optional | The reference of a request. Can be used to uniquely identify the request. |
| `result_code` | `str` | Optional | The result code. |
| `status` | [`Status42Enum`](../../doc/models/status-42-enum.md) | Optional | The status of the account.<br><br>> Permitted values: `Active`. |

## Example

```python
from adyen.models.create_account_response import CreateAccountResponse
from adyen.models.error_field_type import ErrorFieldType
from adyen.models.field_name_enum import FieldNameEnum
from adyen.models.field_type import FieldType

create_account_response = CreateAccountResponse(
    account_code='accountCode6',
    account_holder_code='accountHolderCode8',
    bank_account_uuid='bankAccountUUID2',
    description='description6',
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
    ]
)
```

