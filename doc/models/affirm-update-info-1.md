
# Affirm Update Info 1

Details to provide if `type` is **affirm**.

## Structure

`AffirmUpdateInfo1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `price_plan` | `str` | Optional | Selected Affirm financing package. Choose from **core**, **standard**, or **signature**. Defaults to **core** if no selection made. |

## Example

```python
from adyen.models.affirm_update_info_1 import AffirmUpdateInfo1

affirm_update_info_1 = AffirmUpdateInfo1(
    price_plan='pricePlan4'
)
```

