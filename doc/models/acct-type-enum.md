
# Acct Type Enum

Indicates the type of account. For example, for a multi-account card product. Length: 2 characters. Allowed values:

* **01** — Not applicable
* **02** — Credit
* **03** — Debit

## Enumeration

`AcctTypeEnum`

## Fields

| Name |
|  --- |
| `ENUM_01` |
| `ENUM_02` |
| `ENUM_03` |

## Example

```python
from adyen.models.acct_type_enum import AcctTypeEnum

acct_type = AcctTypeEnum.ENUM_03
```

