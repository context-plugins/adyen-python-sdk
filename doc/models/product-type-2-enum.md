
# Product Type 2 Enum

The type of component.

For [Onboarding components](https://docs.adyen.com/platforms/onboard-users/components), set this to **onboarding**.

For [Platform Experience components](https://docs.adyen.com/platforms/build-user-dashboards), set this to **platform**.

## Enumeration

`ProductType2Enum`

## Fields

| Name |
|  --- |
| `ONBOARDING` |
| `PLATFORM` |
| `BANK` |

## Example

```python
from adyen.models.product_type_2_enum import ProductType2Enum

product_type_2 = ProductType2Enum.BANK
```

