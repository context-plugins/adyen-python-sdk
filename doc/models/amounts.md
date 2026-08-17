
# Amounts

## Structure

`Amounts`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `currency` | `str` | Required | The three-character [ISO currency code](https://docs.adyen.com/development-resources/currency-codes/). |
| `values` | `List[int]` | Required | The amounts of the donation (in [minor units](https://docs.adyen.com/development-resources/currency-codes/)). |

## Example

```python
from adyen.models.amounts import Amounts

amounts = Amounts(
    currency='currency6',
    values=[
        48,
        49
    ]
)
```

