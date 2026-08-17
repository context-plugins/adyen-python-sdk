
# Grant Offers

## Structure

`GrantOffers`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `grant_offers` | [`List[GrantOffer]`](../../doc/models/grant-offer.md) | Required | A list of available grant offers. |

## Example

```python
import dateutil.parser

from adyen.models.amount_17 import Amount17
from adyen.models.contract_type_enum import ContractTypeEnum
from adyen.models.fee_1 import Fee1
from adyen.models.grant_offer import GrantOffer
from adyen.models.grant_offers import GrantOffers

grant_offers = GrantOffers(
    grant_offers=[
        GrantOffer(
            account_holder_id='accountHolderId0',
            amount=Amount17(
                currency='currency2',
                value=110
            ),
            contract_type=ContractTypeEnum.CASHADVANCE,
            expires_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            fee=Fee1(
                amount=Amount17(
                    currency='currency2',
                    value=110
                )
            ),
            id='id8'
        )
    ]
)
```

