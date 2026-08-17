
# Dynamic Offer

## Structure

`DynamicOffer`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_holder_id` | `str` | Required | The unique identifier of the account holder that the dynamic offer is for. |
| `contract_type` | [`ContractTypeEnum`](../../doc/models/contract-type-enum.md) | Required | The contract type of the offer.<br><br>Possible values:<br><br>* **loan**<br>* **cashAdvance** |
| `expires_at` | `datetime` | Required | The expiration date and time of the offer validity period. |
| `financing_type` | [`FinancingType2Enum`](../../doc/models/financing-type-2-enum.md) | Required | The type of financing that the offer is for.<br><br>Possible values: **businessFinancing**. |
| `id` | `str` | Required | The unique identifier of the dynamic offer. |
| `maximum_amount` | [`Amount17`](../../doc/models/amount-17.md) | Required | The maximum financing amount available to the account holder under this offer. |
| `minimum_amount` | [`Amount17`](../../doc/models/amount-17.md) | Required | The minimum financing amount available to the account holder under this offer. |
| `repayment` | [`DynamicOfferRepayment2`](../../doc/models/dynamic-offer-repayment-2.md) | Required | Contains information about the repayment configuration of the grant. |
| `starts_at` | `datetime` | Required | The starting date and time of the offer validity period. |

## Example

```python
import dateutil.parser

from adyen.models.amount_17 import Amount17
from adyen.models.contract_type_enum import ContractTypeEnum
from adyen.models.dynamic_offer import DynamicOffer
from adyen.models.dynamic_offer_repayment_2 import DynamicOfferRepayment2
from adyen.models.financing_type_2_enum import FinancingType2Enum
from adyen.models.repayment_term import RepaymentTerm

dynamic_offer = DynamicOffer(
    account_holder_id='accountHolderId8',
    contract_type=ContractTypeEnum.CASHADVANCE,
    expires_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    financing_type=FinancingType2Enum.HARDWAREFINANCING,
    id='id6',
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
```

