
# Grant Limit 1

## Structure

`GrantLimit1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount` | [`Amount17`](../../doc/models/amount-17.md) | Optional | The limit amount of the grant account. |

## Example

```python
from adyen.models.amount_17 import Amount17
from adyen.models.grant_limit_1 import GrantLimit1

grant_limit_1 = GrantLimit1(
    amount=Amount17(
        currency='currency2',
        value=110
    )
)
```

