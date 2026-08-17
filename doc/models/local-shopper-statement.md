
# Local Shopper Statement

## Structure

`LocalShopperStatement`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `script` | `str` | Required | The character set of the local shopper statement.<br><br>Possible values: **ja-Hani**, **ja-Kana**. |
| `value` | `str` | Required | The text of the local shopper statement in the specified character set. |

## Example

```python
from adyen.models.local_shopper_statement import LocalShopperStatement

local_shopper_statement = LocalShopperStatement(
    script='script4',
    value='value6'
)
```

