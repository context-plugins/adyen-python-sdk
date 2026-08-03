
# Frequency

The frequency of payouts initiated by this payout schedule.

Possible values:

* daily
* weekdays
* weekly
* monthly

Default value: The `defaultFrequency` from the balance platform schedule that you are applying.

## Enumeration

`Frequency`

## Fields

| Name |
|  --- |
| `DAILY` |
| `WEEKLY` |
| `WEEKDAYS` |
| `MONTHLY` |

## Example

```python
from adyen.models.frequency import Frequency

frequency = Frequency.DAILY
```

