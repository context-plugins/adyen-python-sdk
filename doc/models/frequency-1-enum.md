
# Frequency 1 Enum

The frequency of payouts initiated by this payout schedule.

Possible values:

* daily
* weekdays
* weekly
* monthly

Default value: The `defaultFrequency` from the balance platform schedule that you are applying.

## Enumeration

`Frequency1Enum`

## Fields

| Name |
|  --- |
| `DAILY` |
| `WEEKLY` |
| `WEEKDAYS` |
| `MONTHLY` |

## Example

```python
from adyen.models.frequency_1_enum import Frequency1Enum

frequency_1 = Frequency1Enum.WEEKDAYS
```

