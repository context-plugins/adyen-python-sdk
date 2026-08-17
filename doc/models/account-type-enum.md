
# Account Type Enum

Indicates the type of account. For example, for a multi-account card product.
Allowed values:

* notApplicable
* credit
* debit

## Enumeration

`AccountTypeEnum`

## Fields

| Name |
|  --- |
| `NOTAPPLICABLE` |
| `CREDIT` |
| `DEBIT` |

## Example

```python
from adyen.models.account_type_enum import AccountTypeEnum

account_type = AccountTypeEnum.NOTAPPLICABLE
```

