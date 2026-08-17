
# Transfer View 2

Contains information about the transfer related to the transaction.

## Structure

`TransferView2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `category_data` | [BankCategoryData](../../doc/models/bank-category-data.md) \| [InternalCategoryData](../../doc/models/internal-category-data.md) \| [IssuedCard](../../doc/models/issued-card.md) \| [PlatformPayment](../../doc/models/platform-payment.md) \| None | Optional | This is a container for one-of cases. |
| `id` | `str` | Optional | The ID of the resource. |
| `reference` | `str` | Required | The [`reference`](https://docs.adyen.com/api-explorer/#/transfers/latest/post/transfers__reqParam_reference) from the `/transfers` request. If you haven't provided any, Adyen generates a unique reference. |

## Example

```python
from adyen.models.bank_category_data import BankCategoryData
from adyen.models.priority_1_enum import Priority1Enum
from adyen.models.transfer_view_2 import TransferView2
from adyen.models.type_310_enum import Type310Enum

transfer_view_2 = TransferView2(
    reference='reference4',
    category_data=BankCategoryData(
        priority=Priority1Enum.INSTANT,
        mtype=Type310Enum.BANK
    ),
    id='id0'
)
```

