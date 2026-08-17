
# Recurring Details Request

## Structure

`RecurringDetailsRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `merchant_account` | `str` | Required | The merchant account identifier you want to process the (transaction) request with. |
| `recurring` | [`Recurring`](../../doc/models/recurring.md) | Optional | A container for the type of a recurring contract to be retrieved.<br><br>The contract value needs to match the contract value submitted in the payment transaction used to create a recurring contract.<br>However, if `ONECLICK,RECURRING` is the original contract definition in the initial payment, then `contract` should take either `ONECLICK` or `RECURRING`, depending on whether or not you want the shopper to enter their card's security code when they finalize their purchase. |
| `shopper_reference` | `str` | Required | The reference you use to uniquely identify the shopper (e.g. user ID or account ID). |

## Example

```python
import dateutil.parser

from adyen.models.contract_enum import ContractEnum
from adyen.models.recurring import Recurring
from adyen.models.recurring_details_request import RecurringDetailsRequest
from adyen.models.token_service_enum import TokenServiceEnum

recurring_details_request = RecurringDetailsRequest(
    merchant_account='merchantAccount8',
    shopper_reference='shopperReference4',
    recurring=Recurring(
        contract=ContractEnum.ENUM_ONECLICKRECURRING,
        recurring_detail_name='recurringDetailName2',
        recurring_expiry=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
        recurring_frequency='recurringFrequency0',
        token_service=TokenServiceEnum.VISATOKENSERVICE
    )
)
```

