
# Exemption Indicator

Indicates the exemption type that was applied by the issuer to the authentication, if exemption applied.
Allowed values:

* `lowValue`
* `secureCorporate`
* `trustedBeneficiary`
* `transactionRiskAnalysis`

## Enumeration

`ExemptionIndicator`

## Fields

| Name |
|  --- |
| `LOWVALUE` |
| `SECURECORPORATE` |
| `TRUSTEDBENEFICIARY` |
| `TRANSACTIONRISKANALYSIS` |

## Example

```python
from adyen.models.exemption_indicator import ExemptionIndicator

exemption_indicator = ExemptionIndicator.TRUSTEDBENEFICIARY
```

