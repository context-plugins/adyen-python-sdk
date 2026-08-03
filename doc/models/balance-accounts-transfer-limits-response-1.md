
# Balance Accounts Transfer Limits Response 1

*This model accepts additional fields of type Any.*

## Structure

`BalanceAccountsTransferLimitsResponse1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount` | [`Amount5`](../../doc/models/amount-5.md) | Required | - |
| `ends_at` | `datetime` | Optional | The date and time when the transfer limit becomes inactive. If you do not specify an end date, the limit stays active until you override it with a new limit.<br><br>Format [ISO 8601](https://www.w3.org/TR/NOTE-datetime): **YYYY-MM-DDThh:mm:ss.sssTZD** |
| `id` | `str` | Required | The unique identifier of the transfer limit. |
| `limit_status` | [`LimitStatus`](../../doc/models/limit-status.md) | Required | - |
| `reference` | `str` | Optional | Your reference for the transfer limit. |
| `sca_information` | [`ScaInformation`](../../doc/models/sca-information.md) | Optional | - |
| `scope` | [`Scope`](../../doc/models/scope.md) | Required | - |
| `starts_at` | `datetime` | Required | The date and time when the transfer limit becomes active. If you specify a date in the future, we will schedule a transfer limit.<br><br>Format [ISO 8601](https://www.w3.org/TR/NOTE-datetime): **YYYY-MM-DDThh:mm:ss.sssTZD** |
| `transfer_type` | [`TransferType`](../../doc/models/transfer-type.md) | Required | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from adyen.models.amount_5 import Amount5
from adyen.models.balance_accounts_transfer_limits_response_1 import BalanceAccountsTransferLimitsResponse1
from adyen.models.limit_status import LimitStatus
from adyen.models.sca_exemption import ScaExemption
from adyen.models.sca_information import ScaInformation
from adyen.models.sca_status import ScaStatus
from adyen.models.scope import Scope
from adyen.models.transfer_type import TransferType

balance_accounts_transfer_limits_response_1 = BalanceAccountsTransferLimitsResponse1(
    amount=Amount5(
        currency='currency2',
        value=110,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    id='id0',
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
```

