
# Transfer Limit

The transfer limit configured to regulate outgoing transfers.

## Structure

`TransferLimit`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount` | [`Amount17`](../../doc/models/amount-17.md) | Required | The amount for the transfer limit. This is the maximum amount allowed per transfer or per day based on the `scope` of the limit. |
| `ends_at` | `datetime` | Optional | The date and time when the transfer limit becomes inactive. If you do not specify an end date, the limit stays active until you override it with a new limit.<br><br>Format [ISO 8601](https://www.w3.org/TR/NOTE-datetime): **YYYY-MM-DDThh:mm:ss.sssTZD** |
| `id` | `str` | Required | The unique identifier of the transfer limit. |
| `limit_status` | [`LimitStatusEnum`](../../doc/models/limit-status-enum.md) | Required | The status of the transfer limit. Possible values:<br><br>* **active**: the limit is currently active.<br>* **inactive**: the limit is currently inactive.<br>* **pendingSCA**: the limit is pending until your user performs SCA.<br>* **scheduled**: the limit is scheduled to become active at a future date. |
| `reference` | `str` | Optional | Your reference for the transfer limit. |
| `sca_information` | [`ScaInformation1`](../../doc/models/sca-information-1.md) | Optional | Information for the Strong Customer Authentication (SCA) |
| `scope` | [`ScopeEnum`](../../doc/models/scope-enum.md) | Required | The scope to which the transfer limit applies. Possible values:<br><br>* **perTransaction**: you set a maximum amount for each transfer made from the balance account or balance platform.<br>* **perDay**: you set a maximum total amount for all transfers made from the balance account or balance platform in a day. |
| `starts_at` | `datetime` | Required | The date and time when the transfer limit becomes active. If you specify a date in the future, we will schedule a transfer limit.<br><br>Format [ISO 8601](https://www.w3.org/TR/NOTE-datetime): **YYYY-MM-DDThh:mm:ss.sssTZD** |
| `transfer_type` | [`TransferTypeEnum`](../../doc/models/transfer-type-enum.md) | Required | The type of transfer to which the limit applies. Possible values:<br><br>* **instant**: the limit applies to transfers with an **instant** priority.<br>* **all**: the limit applies to all transfers, regardless of priority. |

## Example

```python
import dateutil.parser

from adyen.models.amount_17 import Amount17
from adyen.models.limit_status_enum import LimitStatusEnum
from adyen.models.sca_exemption_enum import ScaExemptionEnum
from adyen.models.sca_information_1 import ScaInformation1
from adyen.models.sca_status_enum import ScaStatusEnum
from adyen.models.scope_enum import ScopeEnum
from adyen.models.transfer_limit import TransferLimit
from adyen.models.transfer_type_enum import TransferTypeEnum

transfer_limit = TransferLimit(
    amount=Amount17(
        currency='currency2',
        value=110
    ),
    id='id8',
    limit_status=LimitStatusEnum.ACTIVE,
    scope=ScopeEnum.PERDAY,
    starts_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    transfer_type=TransferTypeEnum.INSTANT,
    ends_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    reference='reference6',
    sca_information=ScaInformation1(
        status=ScaStatusEnum.PENDING,
        exemption=ScaExemptionEnum.NOTREGULATED
    )
)
```

