
# Create Grant Offer Request

## Structure

`CreateGrantOfferRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount` | [`Amount17`](../../doc/models/amount-17.md) | Required | The financing amount that the user selected from the dynamic offer. Adyen uses this amount to create a static offer. |

## Example

```python
from adyen.models.amount_17 import Amount17
from adyen.models.create_grant_offer_request import CreateGrantOfferRequest

create_grant_offer_request = CreateGrantOfferRequest(
    amount=Amount17(
        currency='currency2',
        value=110
    )
)
```

