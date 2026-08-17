
# Funding Source Enum

The funding source that should be used when multiple sources are available. For Brazilian combo cards, by default the funding source is credit. To use debit, set this value to **debit**.

## Enumeration

`FundingSourceEnum`

## Fields

| Name |
|  --- |
| `CREDIT` |
| `DEBIT` |
| `PREPAID` |

## Example

```python
from adyen.models.funding_source_enum import FundingSourceEnum

funding_source = FundingSourceEnum.CREDIT
```

