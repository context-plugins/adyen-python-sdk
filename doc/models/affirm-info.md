
# Affirm Info

## Structure

`AffirmInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `price_plan` | `str` | Optional | Selected Affirm financing package. Choose from **core**, **standard**, or **signature**. Defaults to **core** if no selection made. |
| `support_email` | `str` | Required | Merchant support email used to manage disputes. |

## Example

```python
from adyen.models.affirm_info import AffirmInfo

affirm_info = AffirmInfo(
    support_email='supportEmail4',
    price_plan='pricePlan6'
)
```

