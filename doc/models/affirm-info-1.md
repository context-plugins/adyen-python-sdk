
# Affirm Info 1

Details to provide if `type` is **affirm**.

## Structure

`AffirmInfo1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `price_plan` | `str` | Optional | Selected Affirm financing package. Choose from **core**, **standard**, or **signature**. Defaults to **core** if no selection made. |
| `support_email` | `str` | Required | Merchant support email used to manage disputes. |

## Example

```python
from adyen.models.affirm_info_1 import AffirmInfo1

affirm_info_1 = AffirmInfo1(
    support_email='supportEmail8',
    price_plan='pricePlan8'
)
```

