
# Grant Offer Fee 1

Contains information about the fee that your user would pay for the grant.

## Structure

`GrantOfferFee1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount` | [`Amount17`](../../doc/models/amount-17.md) | Required | Contains the amount of the offer fee. |
| `apr_basis_points` | `int` | Optional | Annual Percentage Rate (APR) of the offer. The percentage is expressed in [basis points](https://www.investopedia.com/terms/b/basispoint.asp). |

## Example

```python
from adyen.models.amount_17 import Amount17
from adyen.models.grant_offer_fee_1 import GrantOfferFee1

grant_offer_fee_1 = GrantOfferFee1(
    amount=Amount17(
        currency='currency2',
        value=110
    ),
    apr_basis_points=142
)
```

