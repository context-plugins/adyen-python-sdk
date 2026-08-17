
# Localized Information 4

The localized information of the store.

## Structure

`LocalizedInformation4`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `local_shopper_statement` | [`List[LocalShopperStatement]`](../../doc/models/local-shopper-statement.md) | Required | An array of local shopper statements. Card schemes use this in the bank statement.<br><br>For Japan local shopper statements in both ja-Hani and ja-Kana are required. |

## Example

```python
from adyen.models.local_shopper_statement import LocalShopperStatement
from adyen.models.localized_information_4 import LocalizedInformation4

localized_information_4 = LocalizedInformation4(
    local_shopper_statement=[
        LocalShopperStatement(
            script='script4',
            value='value6'
        )
    ]
)
```

