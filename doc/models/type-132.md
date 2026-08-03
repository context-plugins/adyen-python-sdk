
# Type 132

Type of identity data. For individuals, the following types are supported. See our [onboarding guide](https://docs.adyen.com/platforms/onboard-users/onboarding-steps/?onboarding_type=custom) for other supported countries.

- Australia: **driversLicense**, **passport**

- Hong Kong: **driversLicense**, **nationalIdNumber**, **passport**

- New Zealand: **driversLicense**, **passport**

- Singapore: **driversLicense**, **nationalIdNumber**, **passport**

- All other supported countries: **nationalIdNumber**

## Enumeration

`Type132`

## Fields

| Name |
|  --- |
| `NATIONALIDNUMBER` |
| `PASSPORT` |
| `DRIVERSLICENSE` |
| `IDENTITYCARD` |

## Example

```python
from adyen.models.type_132 import Type132

type_132 = Type132.NATIONALIDNUMBER
```

