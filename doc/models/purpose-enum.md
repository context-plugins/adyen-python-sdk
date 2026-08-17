
# Purpose Enum

Specifies the reason for creating the rule.

Possible values:

* **fraud**: the rule is created to regulate fraudulent activity.
* **policy**: the rule is created to ensure that the transaction adheres to your business' policies. For example, if your business has policies about the Merchant Category Codes (MCCs) allowed on a transaction, you can create a rule to block transactions that have specific MCCs.

## Enumeration

`PurposeEnum`

## Fields

| Name |
|  --- |
| `COMPLIANCE` |
| `FRAUD` |
| `INTERNALPOLICY` |
| `POLICY` |
| `SYSTEM` |

## Example

```python
from adyen.models.purpose_enum import PurposeEnum

purpose = PurposeEnum.FRAUD
```

