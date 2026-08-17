
# Calculate Grant Offer Request

## Structure

`CalculateGrantOfferRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount` | [`Amount17`](../../doc/models/amount-17.md) | Required | The financing amount that the user selected from a dynamic offer. Adyen uses this amount to calculate a preliminary offer. |

## Example

```python
from adyen.models.amount_17 import Amount17
from adyen.models.calculate_grant_offer_request import CalculateGrantOfferRequest

calculate_grant_offer_request = CalculateGrantOfferRequest(
    amount=Amount17(
        currency='currency2',
        value=110
    )
)
```

