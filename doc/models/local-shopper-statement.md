
# Local Shopper Statement

*This model accepts additional fields of type Any.*

## Structure

`LocalShopperStatement`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `script` | `str` | Required | The character set of the local shopper statement.<br><br>Possible values: **ja-Hani**, **ja-Kana**. |
| `value` | `str` | Required | The text of the local shopper statement in the specified character set. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.local_shopper_statement import LocalShopperStatement

local_shopper_statement = LocalShopperStatement(
    script='script4',
    value='value6',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

