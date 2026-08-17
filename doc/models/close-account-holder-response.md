
# Close Account Holder Response

## Structure

`CloseAccountHolderResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_holder_status` | [`AccountHolderStatus1`](../../doc/models/account-holder-status-1.md) | Optional | The new status of the Account Holder. |
| `invalid_fields` | [`List[ErrorFieldType]`](../../doc/models/error-field-type.md) | Optional | Contains field validation errors that would prevent requests from being processed. |
| `psp_reference` | `str` | Optional | The reference of a request. Can be used to uniquely identify the request. |
| `result_code` | `str` | Optional | The result code. |

## Example

```python
import dateutil.parser

from adyen.models.account_event import AccountEvent
from adyen.models.account_holder_status_1 import AccountHolderStatus1
from adyen.models.account_payout_state_2 import AccountPayoutState2
from adyen.models.account_processing_state_2 import AccountProcessingState2
from adyen.models.amount import Amount
from adyen.models.close_account_holder_response import CloseAccountHolderResponse
from adyen.models.error_field_type import ErrorFieldType
from adyen.models.event_enum import EventEnum
from adyen.models.field_name_enum import FieldNameEnum
from adyen.models.field_type import FieldType
from adyen.models.status_12_enum import Status12Enum

close_account_holder_response = CloseAccountHolderResponse(
    account_holder_status=AccountHolderStatus1(
        status=Status12Enum.INACTIVE,
        events=[
            AccountEvent(
                event=EventEnum.INACTIVATEACCOUNT,
                execution_date=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
                reason='reason6'
            )
        ],
        payout_state=AccountPayoutState2(
            allow_payout=False,
            disable_reason='disableReason2',
            disabled=False,
            not_allowed_reason='notAllowedReason4',
            payout_limit=Amount(
                currency='currency8',
                value=88
            )
        ),
        processing_state=AccountProcessingState2(
            disable_reason='disableReason2',
            disabled=False,
            processed_from=Amount(
                currency='currency4',
                value=148
            ),
            processed_to=Amount(
                currency='currency2',
                value=54
            ),
            tier_number=156
        ),
        status_reason='statusReason8'
    ),
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
    psp_reference='pspReference0',
    result_code='resultCode6'
)
```

