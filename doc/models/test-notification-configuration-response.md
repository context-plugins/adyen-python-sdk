
# Test Notification Configuration Response

## Structure

`TestNotificationConfigurationResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `error_messages` | `List[str]` | Optional | Any error messages encountered. |
| `event_types` | [`List[EventType1Enum]`](../../doc/models/event-type-1-enum.md) | Optional | The event types that were tested.<br><br>> Permitted values: `ACCOUNT_HOLDER_CREATED`, `ACCOUNT_CREATED`, `ACCOUNT_UPDATED`, `ACCOUNT_HOLDER_UPDATED`, `ACCOUNT_HOLDER_STATUS_CHANGE`, `ACCOUNT_HOLDER_STORE_STATUS_CHANGE` `ACCOUNT_HOLDER_VERIFICATION`, `ACCOUNT_HOLDER_LIMIT_REACHED`, `ACCOUNT_HOLDER_PAYOUT`, `PAYMENT_FAILURE`, `SCHEDULED_REFUNDS`, `REPORT_AVAILABLE`, `TRANSFER_FUNDS`, `BENEFICIARY_SETUP`, `COMPENSATE_NEGATIVE_BALANCE`. |
| `exchange_messages` | [`List[ExchangeMessage]`](../../doc/models/exchange-message.md) | Optional | The notification message and related response messages. |
| `invalid_fields` | [`List[ErrorFieldType]`](../../doc/models/error-field-type.md) | Optional | Contains field validation errors that would prevent requests from being processed. |
| `notification_id` | `int` | Required | The ID of the notification subscription configuration. |
| `ok_messages` | `List[str]` | Optional | A list of messages describing the testing steps. |
| `psp_reference` | `str` | Optional | The reference of a request. Can be used to uniquely identify the request. |
| `result_code` | `str` | Optional | The result code. |

## Example

```python
from adyen.models.error_field_type import ErrorFieldType
from adyen.models.event_type_1_enum import EventType1Enum
from adyen.models.exchange_message import ExchangeMessage
from adyen.models.field_name_enum import FieldNameEnum
from adyen.models.field_type import FieldType
from adyen.models.test_notification_configuration_response import TestNotificationConfigurationResponse

test_notification_configuration_response = TestNotificationConfigurationResponse(
    notification_id=198,
    error_messages=[
        'errorMessages3',
        'errorMessages4',
        'errorMessages5'
    ],
    event_types=[
        EventType1Enum.PENDING_CREDIT
    ],
    exchange_messages=[
        ExchangeMessage(
            message_code='messageCode8',
            message_description='messageDescription8'
        ),
        ExchangeMessage(
            message_code='messageCode8',
            message_description='messageDescription8'
        )
    ],
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
    ok_messages=[
        'okMessages8',
        'okMessages9',
        'okMessages0'
    ]
)
```

