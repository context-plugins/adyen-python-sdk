
# Get Dynamic Offers Response

## Structure

`GetDynamicOffersResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `dynamic_offers` | [`List[DynamicOffer]`](../../doc/models/dynamic-offer.md) | Required | Contains a list of available dynamic offers for the specified account holder. |

## Example

```python
import dateutil.parser

from adyen.models.amount_17 import Amount17
from adyen.models.contract_type_enum import ContractTypeEnum
from adyen.models.dynamic_offer import DynamicOffer
from adyen.models.dynamic_offer_repayment_2 import DynamicOfferRepayment2
from adyen.models.financing_type_2_enum import FinancingType2Enum
from adyen.models.get_dynamic_offers_response import GetDynamicOffersResponse
from adyen.models.repayment_term import RepaymentTerm

get_dynamic_offers_response = GetDynamicOffersResponse(
    dynamic_offers=[
        DynamicOffer(
            account_holder_id='accountHolderId4',
            contract_type=ContractTypeEnum.CASHADVANCE,
            expires_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            financing_type=FinancingType2Enum.HARDWAREFINANCING,
            id='id2',
            maximum_amount=Amount17(
                currency='currency0',
                value=190
            ),
            minimum_amount=Amount17(
                currency='currency2',
                value=96
            ),
            repayment=DynamicOfferRepayment2(
                term=RepaymentTerm(
                    estimated_days=248,
                    maximum_days=24
                )
            ),
            starts_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
        )
    ]
)
```

