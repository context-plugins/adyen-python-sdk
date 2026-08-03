
# Localized Information 4

The localized information of the store.

*This model accepts additional fields of type Any.*

## Structure

`LocalizedInformation4`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `local_shopper_statement` | [`List[LocalShopperStatement]`](../../doc/models/local-shopper-statement.md) | Required | An array of local shopper statements. Card schemes use this in the bank statement.<br><br>For Japan local shopper statements in both ja-Hani and ja-Kana are required. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.local_shopper_statement import LocalShopperStatement
from adyen.models.localized_information_4 import LocalizedInformation4

localized_information_4 = LocalizedInformation4(
    local_shopper_statement=[
        LocalShopperStatement(
            script='script4',
            value='value6',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

