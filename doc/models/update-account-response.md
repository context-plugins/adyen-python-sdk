
# Update Account Response

## Structure

`UpdateAccountResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_code` | `str` | Required | The code of the account. |
| `bank_account_uuid` | `str` | Optional | The bankAccountUUID of the bank account held by the account holder to couple the account with. Scheduled payouts in currencies matching the currency of this bank account will be sent to this bank account. Payouts in different currencies will be sent to a matching bank account of the account holder. |
| `description` | `str` | Optional | The description of the account. |
| `invalid_fields` | [`List[ErrorFieldType]`](../../doc/models/error-field-type.md) | Optional | A list of fields that caused the `/updateAccount` request to fail. |
| `metadata` | `Dict[str, str]` | Optional | A set of key and value pairs containing metadata. |
| `payout_method_code` | `str` | Optional | The payout method code held by the account holder to couple the account with. Scheduled card payouts will be sent using this payout method code. |
| `payout_schedule` | [`PayoutScheduleResponse3`](../../doc/models/payout-schedule-response-3.md) | Optional | The details of the payout schedule to which the account is updated. |
| `payout_speed` | [`PayoutSpeed4Enum`](../../doc/models/payout-speed-4-enum.md) | Optional | Speed at which payouts for this account are processed.<br><br>Possible values: `STANDARD`, `SAME_DAY`. |
| `psp_reference` | `str` | Optional | The reference of a request. Can be used to uniquely identify the request. |
| `result_code` | `str` | Optional | The result code. |

## Example

```python
from adyen.models.error_field_type import ErrorFieldType
from adyen.models.field_name_enum import FieldNameEnum
from adyen.models.field_type import FieldType
from adyen.models.update_account_response import UpdateAccountResponse

update_account_response = UpdateAccountResponse(
    account_code='accountCode0',
    bank_account_uuid='bankAccountUUID6',
    description='description0',
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
    metadata={
        'key0': 'metadata7',
        'key1': 'metadata6'
    },
    payout_method_code='payoutMethodCode0'
)
```

