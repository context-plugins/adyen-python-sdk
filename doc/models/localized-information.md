
# Localized Information

## Structure

`LocalizedInformation`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `local_shopper_statement` | [`List[LocalShopperStatement]`](../../doc/models/local-shopper-statement.md) | Required | An array of local shopper statements. Card schemes use this in the bank statement.<br><br>For Japan local shopper statements in both ja-Hani and ja-Kana are required. |

## Example

```python
from adyen.models.local_shopper_statement import LocalShopperStatement
from adyen.models.localized_information import LocalizedInformation

localized_information = LocalizedInformation(
    local_shopper_statement=[
        LocalShopperStatement(
            script='script4',
            value='value6'
        )
    ]
)
```

