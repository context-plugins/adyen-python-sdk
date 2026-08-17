
# Transfer Limit List Response

## Structure

`TransferLimitListResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `transfer_limits` | [`List[TransferLimit]`](../../doc/models/transfer-limit.md) | Required | List of available transfer limits. |

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
from adyen.models.transfer_limit_list_response import TransferLimitListResponse
from adyen.models.transfer_type_enum import TransferTypeEnum

transfer_limit_list_response = TransferLimitListResponse(
    transfer_limits=[
        TransferLimit(
            amount=Amount17(
                currency='currency2',
                value=110
            ),
            id='id8',
            limit_status=LimitStatusEnum.PENDINGSCA,
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
    ]
)
```

