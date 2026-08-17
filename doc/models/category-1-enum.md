
# Category 1 Enum

The type of transfer that results from the sweep.

Possible values:

- **bank**: Sweep to a [transfer instrument](https://docs.adyen.com/api-explorer/#/legalentity/latest/post/transferInstruments__resParam_id).

- **internal**: Transfer to another [balance account](https://docs.adyen.com/api-explorer/#/balanceplatform/latest/post/balanceAccounts__resParam_id) within your platform.

Required when setting `priorities`.

## Enumeration

`Category1Enum`

## Fields

| Name |
|  --- |
| `BANK` |
| `INTERNAL` |
| `PLATFORMPAYMENT` |

## Example

```python
from adyen.models.category_1_enum import Category1Enum

category_1 = Category1Enum.BANK
```

