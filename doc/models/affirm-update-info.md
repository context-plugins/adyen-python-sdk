
# Affirm Update Info

## Structure

`AffirmUpdateInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `price_plan` | `str` | Optional | Selected Affirm financing package. Choose from **core**, **standard**, or **signature**. Defaults to **core** if no selection made. |

## Example

```python
from adyen.models.affirm_update_info import AffirmUpdateInfo

affirm_update_info = AffirmUpdateInfo(
    price_plan='pricePlan4'
)
```

