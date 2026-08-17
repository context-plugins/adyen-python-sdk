
# Sub Type 11 Enum

The specific category of **other** dispute that you are raising.

Possible values: **atmDispute**, **cancelledGoodsServices**, **cancelledRecurring**, **counterfeit**, **creditNotProcessed**, **notAsDescribed**.

## Enumeration

`SubType11Enum`

## Fields

| Name |
|  --- |
| `ATMDISPUTE` |
| `CANCELLEDGOODSSERVICES` |
| `CANCELLEDRECURRING` |
| `CREDITNOTPROCESSED` |
| `COUNTERFEIT` |
| `NOTASDESCRIBED` |

## Example

```python
from adyen.models.sub_type_11_enum import SubType11Enum

sub_type_11 = SubType11Enum.COUNTERFEIT
```

