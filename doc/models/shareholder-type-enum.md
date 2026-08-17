
# Shareholder Type Enum

Specifies how the person is associated with the account holder.

Possible values:

* **Owner**: Individuals who directly or indirectly own 25% or more of a company.

* **Controller**: Individuals who are members of senior management staff responsible for managing a company or organization.

## Enumeration

`ShareholderTypeEnum`

## Fields

| Name |
|  --- |
| `CONTROLLER` |
| `OWNER` |
| `SIGNATORY` |

## Example

```python
from adyen.models.shareholder_type_enum import ShareholderTypeEnum

shareholder_type = ShareholderTypeEnum.OWNER
```

