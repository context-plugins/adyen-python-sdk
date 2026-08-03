
# Category 2

The type of transfer.

Possible values:

- **bank**: Transfer to a [transfer instrument](https://docs.adyen.com/api-explorer/#/legalentity/latest/post/transferInstruments__resParam_id) or a bank account.

## Enumeration

`Category2`

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
from adyen.models.category_2 import Category2

category_2 = Category2.TOPUP
```

