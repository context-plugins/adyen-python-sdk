
# Category 2 Enum

The type of transfer.

Possible values:

- **bank**: Transfer to a [transfer instrument](https://docs.adyen.com/api-explorer/#/legalentity/latest/post/transferInstruments__resParam_id) or a bank account.

## Enumeration

`Category2Enum`

## Fields

| Name |
|  --- |
| `BANK` |
| `CARD` |
| `GRANTS` |
| `INTEREST` |
| `INTERNAL` |
| `ISSUEDCARD` |
| `MIGRATION` |
| `PLATFORMPAYMENT` |
| `TOPUP` |
| `UPGRADE` |

## Example

```python
from adyen.models.category_2_enum import Category2Enum

category_2 = Category2Enum.TOPUP
```

