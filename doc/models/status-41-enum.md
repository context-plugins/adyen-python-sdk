
# Status 41 Enum

The status of the store. Possible values are:

- **active**: This value is assigned automatically when a store is created.
- **inactive**: The maximum [transaction limits and number of Store-and-Forward transactions](https://docs.adyen.com/point-of-sale/determine-account-structure/configure-features#payment-features) for the store are set to 0. This blocks new transactions, but captures are still possible.
- **closed**: The terminals of the store are reassigned to the merchant inventory, so they can't process payments.

You can change the status from **active** to **inactive**, and from **inactive** to **active** or **closed**.
Once **closed**, a store can't be reopened.

## Enumeration

`Status41Enum`

## Fields

| Name |
|  --- |
| `ACTIVE` |
| `CLOSED` |
| `INACTIVE` |

## Example

```python
from adyen.models.status_41_enum import Status41Enum

status_41 = Status41Enum.INACTIVE
```

