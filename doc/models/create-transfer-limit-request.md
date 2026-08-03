
# Create Transfer Limit Request

*This model accepts additional fields of type Any.*

## Structure

`CreateTransferLimitRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount` | [`Amount5`](../../doc/models/amount-5.md) | Required | - |
| `ends_at` | `datetime` | Optional | The date and time when the transfer limit becomes inactive. If you do not specify an end date, the limit stays active until you override it with a new limit.<br><br>Format [ISO 8601](https://www.w3.org/TR/NOTE-datetime): **YYYY-MM-DDThh:mm:ss.sssTZD** |
| `reference` | `str` | Optional | Your reference for the transfer limit. |
| `sca_information` | [`CreateScaInformation`](../../doc/models/create-sca-information.md) | Optional | - |
| `scope` | [`Scope`](../../doc/models/scope.md) | Required | - |
| `starts_at` | `datetime` | Optional | The date and time when the transfer limit becomes active. If you specify a date in the future, we will schedule a transfer limit.<br><br>Format [ISO 8601](https://www.w3.org/TR/NOTE-datetime): **YYYY-MM-DDThh:mm:ss.sssTZD** |
| `transfer_type` | [`TransferType`](../../doc/models/transfer-type.md) | Required | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from adyen.models.amount_5 import Amount5
from adyen.models.create_sca_information import CreateScaInformation
from adyen.models.create_transfer_limit_request import CreateTransferLimitRequest
from adyen.models.sca_exemption import ScaExemption
from adyen.models.scope import Scope
from adyen.models.transfer_type import TransferType

create_transfer_limit_request = CreateTransferLimitRequest(
    amount=Amount5(
        currency='currency2',
        value=110,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    scope=Scope.PERDAY,
    transfer_type=TransferType.INSTANT,
    ends_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    reference='reference0',
    sca_information=CreateScaInformation(
        exemption=ScaExemption.NOTREGULATED,
        sca_on_approval=False,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    starts_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

