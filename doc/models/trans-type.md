
# Trans Type

Identifies the type of transaction being authenticated. Length: 2 characters. Allowed values:

* **01** — Goods/Service Purchase
* **03** — Check Acceptance
* **10** — Account Funding
* **11** — Quasi-Cash Transaction
* **28** — Prepaid Activation and Load

## Enumeration

`TransType`

## Fields

| Name |
|  --- |
| `ENUM_01` |
| `ENUM_03` |
| `ENUM_10` |
| `ENUM_11` |
| `ENUM_28` |

## Example

```python
from adyen.models.trans_type import TransType

trans_type = TransType.ENUM_11
```

