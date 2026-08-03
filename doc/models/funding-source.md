
# Funding Source

The funding source that should be used when multiple sources are available. For Brazilian combo cards, by default the funding source is credit. To use debit, set this value to **debit**.

## Enumeration

`FundingSource`

## Fields

| Name |
|  --- |
| `CREDIT` |
| `DEBIT` |
| `PREPAID` |

## Example

```python
from adyen.models.funding_source import FundingSource

funding_source = FundingSource.CREDIT
```

