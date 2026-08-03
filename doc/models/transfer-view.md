
# Transfer View

*This model accepts additional fields of type Any.*

## Structure

`TransferView`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `category_data` | [BankCategoryData](../../doc/models/bank-category-data.md) \| [InternalCategoryData](../../doc/models/internal-category-data.md) \| [IssuedCard](../../doc/models/issued-card.md) \| [PlatformPayment](../../doc/models/platform-payment.md) \| None | Optional | This is a container for one-of cases. |
| `id` | `str` | Optional | The ID of the resource. |
| `reference` | `str` | Required | The [`reference`](https://docs.adyen.com/api-explorer/#/transfers/latest/post/transfers__reqParam_reference) from the `/transfers` request. If you haven't provided any, Adyen generates a unique reference. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.bank_category_data import BankCategoryData
from adyen.models.priority import Priority
from adyen.models.transfer_view import TransferView
from adyen.models.type_312 import Type312

transfer_view = TransferView(
    reference='reference6',
    category_data=BankCategoryData(
        priority=Priority.INSTANT,
        mtype=Type312.BANK,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    id='id8',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

