
# Frequency Enum

The frequency with which a shopper should be charged.

Possible values: **adhoc**, **daily**, **weekly**, **biWeekly**, **monthly**, **quarterly**, **halfYearly**, **yearly**., The frequency with which a shopper should be charged.

Possible values: **daily**, **weekly**, **biWeekly**, **monthly**, **quarterly**, **halfYearly**, **yearly**.

## Enumeration

`FrequencyEnum`

## Fields

| Name |
|  --- |
| `ADHOC` |
| `DAILY` |
| `WEEKLY` |
| `BIWEEKLY` |
| `MONTHLY` |
| `QUARTERLY` |
| `HALFYEARLY` |
| `YEARLY` |

## Example

```python
from adyen.models.frequency_enum import FrequencyEnum

frequency = FrequencyEnum.MONTHLY
```

