
# Suspend Account Holder Response

*This model accepts additional fields of type Any.*

## Structure

`SuspendAccountHolderResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_holder_status` | [`AccountHolderStatus`](../../doc/models/account-holder-status.md) | Optional | - |
| `invalid_fields` | [`List[ErrorFieldType]`](../../doc/models/error-field-type.md) | Optional | Contains field validation errors that would prevent requests from being processed. |
| `psp_reference` | `str` | Optional | The reference of a request. Can be used to uniquely identify the request. |
| `result_code` | `str` | Optional | The result code. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from adyen.models.account_event import AccountEvent
from adyen.models.account_holder_status import AccountHolderStatus
from adyen.models.account_payout_state import AccountPayoutState
from adyen.models.account_processing_state import AccountProcessingState
from adyen.models.error_field_type import ErrorFieldType
from adyen.models.event import Event
from adyen.models.field_name import FieldName
from adyen.models.field_type_2 import FieldType2
from adyen.models.payout_limit import PayoutLimit
from adyen.models.processed_from import ProcessedFrom
from adyen.models.processed_to import ProcessedTo
from adyen.models.status_1 import Status1
from adyen.models.suspend_account_holder_response import SuspendAccountHolderResponse

suspend_account_holder_response = SuspendAccountHolderResponse(
    account_holder_status=AccountHolderStatus(
        status=Status1.INACTIVE,
        events=[
            AccountEvent(
                event=Event.INACTIVATEACCOUNT,
                execution_date=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
                reason='reason6',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            )
        ],
        payout_state=AccountPayoutState(
            allow_payout=False,
            disable_reason='disableReason2',
            disabled=False,
            not_allowed_reason='notAllowedReason4',
            payout_limit=PayoutLimit(
                currency='currency8',
                value=88,
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        processing_state=AccountProcessingState(
            disable_reason='disableReason2',
            disabled=False,
            processed_from=ProcessedFrom(
                currency='currency4',
                value=148,
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            processed_to=ProcessedTo(
                currency='currency2',
                value=54,
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            tier_number=156,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        status_reason='statusReason8',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
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
    psp_reference='pspReference6',
    result_code='resultCode0',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

