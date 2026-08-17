
# Cost Estimate Response

## Structure

`CostEstimateResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `card_bin` | [`CardBin1`](../../doc/models/card-bin-1.md) | Optional | Card BIN details. |
| `cost_estimate_amount` | [`Amount`](../../doc/models/amount.md) | Optional | The estimated cost (scheme fee + interchange) in the settlement currency. If the settlement currency cannot be determined, the fee in EUR is returned. |
| `cost_estimate_reference` | `str` | Optional | Adyen's 16-character reference associated with the request. |
| `result_code` | `str` | Optional | The result of the cost estimation. |

## Example

```python
from adyen.models.amount import Amount
from adyen.models.card_bin_1 import CardBin1
from adyen.models.cost_estimate_response import CostEstimateResponse

cost_estimate_response = CostEstimateResponse(
    card_bin=CardBin1(
        bin='bin6',
        commercial=False,
        funding_source='fundingSource0',
        funds_availability='fundsAvailability0',
        issuer_bin='issuerBin8'
    ),
    cost_estimate_amount=Amount(
        currency='currency8',
        value=90
    ),
    cost_estimate_reference='costEstimateReference4',
    result_code='resultCode8'
)
```

