
# Fraud Risk Level Enum

The risk level of the transaction as classified by the [machine learning](https://docs.adyen.com/risk-management/configure-your-risk-profile/machine-learning-rules/) fraud risk rule. The risk level indicates the likelihood that a transaction will result in a fraudulent dispute. Possible values:

* veryLow
* low
* medium
* high
* veryHigh

## Enumeration

`FraudRiskLevelEnum`

## Fields

| Name |
|  --- |
| `VERYLOW` |
| `LOW` |
| `MEDIUM` |
| `HIGH` |
| `VERYHIGH` |

## Example

```python
from adyen.models.fraud_risk_level_enum import FraudRiskLevelEnum

fraud_risk_level = FraudRiskLevelEnum.MEDIUM
```

