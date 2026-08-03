
# Transfer Limit List Response

*This model accepts additional fields of type Any.*

## Structure

`TransferLimitListResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `transfer_limits` | [`List[TransferLimit]`](../../doc/models/transfer-limit.md) | Required | List of available transfer limits. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from adyen.models.amount_5 import Amount5
from adyen.models.limit_status import LimitStatus
from adyen.models.sca_exemption import ScaExemption
from adyen.models.sca_information import ScaInformation
from adyen.models.sca_status import ScaStatus
from adyen.models.scope import Scope
from adyen.models.transfer_limit import TransferLimit
from adyen.models.transfer_limit_list_response import TransferLimitListResponse
from adyen.models.transfer_type import TransferType

transfer_limit_list_response = TransferLimitListResponse(
    transfer_limits=[
        TransferLimit(
            amount=Amount5(
                currency='currency2',
                value=110,
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            id='id8',
            limit_status=LimitStatus.PENDINGSCA,
            scope=Scope.PERDAY,
            starts_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            transfer_type=TransferType.INSTANT,
            ends_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            reference='reference6',
            sca_information=ScaInformation(
                status=ScaStatus.PENDING,
                exemption=ScaExemption.NOTREGULATED,
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

