
# Grant Offer Fee

## Structure

`GrantOfferFee`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount` | [`Amount17`](../../doc/models/amount-17.md) | Required | Contains the amount of the offer fee. |
| `apr_basis_points` | `int` | Optional | Annual Percentage Rate (APR) of the offer. The percentage is expressed in [basis points](https://www.investopedia.com/terms/b/basispoint.asp). |

## Example

```python
from adyen.models.amount_17 import Amount17
from adyen.models.grant_offer_fee import GrantOfferFee

grant_offer_fee = GrantOfferFee(
    amount=Amount17(
        currency='currency2',
        value=110
    ),
    apr_basis_points=206
)
```

