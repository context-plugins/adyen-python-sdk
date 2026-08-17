
# Donation Type 1 Enum

The type of donation to collect from the shopper. Possible values:

- **roundup**: Round up the transaction amount.

- **fixedAmounts**: Choose a fixed amount.

- **fixedAmountsRoundup**: Round up, or choose a fixed amount.

## Enumeration

`DonationType1Enum`

## Fields

| Name |
|  --- |
| `ROUNDUP` |
| `FIXEDAMOUNTS` |
| `FIXEDAMOUNTSROUNDUP` |

## Example

```python
from adyen.models.donation_type_1_enum import DonationType1Enum

donation_type_1 = DonationType1Enum.ROUNDUP
```

