
# Grant Offer

## Structure

`GrantOffer`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_holder_id` | `str` | Required | The identifier of the account holder to which the grant is offered. |
| `amount` | [`Amount17`](../../doc/models/amount-17.md) | Optional | The principal amount of the grant. |
| `contract_type` | [`ContractTypeEnum`](../../doc/models/contract-type-enum.md) | Optional | The contract type of the grant offer. Possible value: **cashAdvance**, **loan**. |
| `expires_at` | `datetime` | Optional | The end date of the grant offer validity period. |
| `fee` | [`Fee1`](../../doc/models/fee-1.md) | Optional | Details of the fee configuration. |
| `id` | `str` | Optional | The unique identifier of the grant offer. |
| `repayment` | [`Repayment2`](../../doc/models/repayment-2.md) | Optional | Details of the repayment configuration. |
| `starts_at` | `datetime` | Optional | The starting date of the grant offer validity period. |

## Example

```python
import dateutil.parser

from adyen.models.amount_17 import Amount17
from adyen.models.contract_type_enum import ContractTypeEnum
from adyen.models.fee_1 import Fee1
from adyen.models.grant_offer import GrantOffer

grant_offer = GrantOffer(
    account_holder_id='accountHolderId4',
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
    id='id2'
)
```

