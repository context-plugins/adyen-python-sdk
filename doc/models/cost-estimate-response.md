
# Cost Estimate Response

*This model accepts additional fields of type Any.*

## Structure

`CostEstimateResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `card_bin` | [`CardBin`](../../doc/models/card-bin.md) | Optional | - |
| `cost_estimate_amount` | [`CostEstimateAmount`](../../doc/models/cost-estimate-amount.md) | Optional | - |
| `cost_estimate_reference` | `str` | Optional | Adyen's 16-character reference associated with the request. |
| `result_code` | `str` | Optional | The result of the cost estimation. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.card_bin import CardBin
from adyen.models.cost_estimate_amount import CostEstimateAmount
from adyen.models.cost_estimate_response import CostEstimateResponse

cost_estimate_response = CostEstimateResponse(
    card_bin=CardBin(
        bin='bin6',
        commercial=False,
        funding_source='fundingSource0',
        funds_availability='fundsAvailability0',
        issuer_bin='issuerBin8',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    cost_estimate_amount=CostEstimateAmount(
        currency='currency8',
        value=90,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    cost_estimate_reference='costEstimateReference4',
    result_code='resultCode8',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

