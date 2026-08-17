
# Cost Estimate Assumptions

## Structure

`CostEstimateAssumptions`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `assume_3_d_secure_authenticated` | `bool` | Optional | If true, the cardholder is expected to successfully authorise via 3D Secure. |
| `assume_level_3_data` | `bool` | Optional | If true, the transaction is expected to have valid Level 3 data. |
| `installments` | `int` | Optional | If not zero, the number of installments. |

## Example

```python
from adyen.models.cost_estimate_assumptions import CostEstimateAssumptions

cost_estimate_assumptions = CostEstimateAssumptions(
    assume_3_d_secure_authenticated=False,
    assume_level_3_data=False,
    installments=80
)
```

