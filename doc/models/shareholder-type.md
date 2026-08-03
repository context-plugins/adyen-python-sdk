
# Shareholder Type

Specifies how the person is associated with the account holder.

Possible values:

* **Owner**: Individuals who directly or indirectly own 25% or more of a company.

* **Controller**: Individuals who are members of senior management staff responsible for managing a company or organization.

## Enumeration

`ShareholderType`

## Fields

| Name |
|  --- |
| `CONTROLLER` |
| `OWNER` |
| `SIGNATORY` |

## Example

```python
from adyen.models.shareholder_type import ShareholderType

shareholder_type = ShareholderType.OWNER
```

