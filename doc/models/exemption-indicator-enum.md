
# Exemption Indicator Enum

Indicates the exemption type that was applied by the issuer to the authentication, if exemption applied.
Allowed values:

* `lowValue`
* `secureCorporate`
* `trustedBeneficiary`
* `transactionRiskAnalysis`

## Enumeration

`ExemptionIndicatorEnum`

## Fields

| Name |
|  --- |
| `LOWVALUE` |
| `SECURECORPORATE` |
| `TRUSTEDBENEFICIARY` |
| `TRANSACTIONRISKANALYSIS` |

## Example

```python
from adyen.models.exemption_indicator_enum import ExemptionIndicatorEnum

exemption_indicator = ExemptionIndicatorEnum.TRUSTEDBENEFICIARY
```

