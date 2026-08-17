
# Create Permit Request

## Structure

`CreatePermitRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `merchant_account` | `str` | Required | The merchant account identifier, with which you want to process the transaction. |
| `permits` | [`List[Permit]`](../../doc/models/permit.md) | Required | The permits to create for this recurring contract. |
| `recurring_detail_reference` | `str` | Required | The recurring contract the new permits will use. |
| `shopper_reference` | `str` | Required | The shopper's reference to uniquely identify this shopper (e.g. user ID or account ID). |

## Example

```python
import dateutil.parser

from adyen.models.amount import Amount
from adyen.models.create_permit_request import CreatePermitRequest
from adyen.models.permit import Permit
from adyen.models.permit_restriction_2 import PermitRestriction2

create_permit_request = CreatePermitRequest(
    merchant_account='merchantAccount6',
    permits=[
        Permit(
            partner_id='partnerId8',
            profile_reference='profileReference0',
            restriction=PermitRestriction2(
                max_amount=Amount(
                    currency='currency4',
                    value=160
                ),
                single_transaction_limit=Amount(
                    currency='currency8',
                    value=122
                ),
                single_use=False
            ),
            result_key='resultKey4',
            valid_till_date=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
        )
    ],
    recurring_detail_reference='recurringDetailReference4',
    shopper_reference='shopperReference2'
)
```

