
# Permit Restriction

## Structure

`PermitRestriction`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `max_amount` | [`Amount`](../../doc/models/amount.md) | Optional | The total sum amount of one or more payments made using this permit may not exceed this amount if set. |
| `single_transaction_limit` | [`Amount`](../../doc/models/amount.md) | Optional | The amount of any single payment using this permit may not exceed this amount if set. |
| `single_use` | `bool` | Optional | Only a single payment can be made using this permit if set to true, otherwise multiple payments are allowed. |

## Example

```python
from adyen.models.amount import Amount
from adyen.models.permit_restriction import PermitRestriction

permit_restriction = PermitRestriction(
    max_amount=Amount(
        currency='currency4',
        value=160
    ),
    single_transaction_limit=Amount(
        currency='currency8',
        value=122
    ),
    single_use=False
)
```

