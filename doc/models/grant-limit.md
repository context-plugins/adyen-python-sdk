
# Grant Limit

## Structure

`GrantLimit`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount` | [`Amount17`](../../doc/models/amount-17.md) | Optional | The amount available on the grant account. |

## Example

```python
from adyen.models.amount_17 import Amount17
from adyen.models.grant_limit import GrantLimit

grant_limit = GrantLimit(
    amount=Amount17(
        currency='currency2',
        value=110
    )
)
```

