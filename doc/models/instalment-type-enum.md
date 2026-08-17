
# Instalment Type Enum

Type of instalment transaction. For requesting an instalment payment transaction.
Possible values:

* **DeferredInstalments**
* **EqualInstalments**
* **InequalInstalments**

## Enumeration

`InstalmentTypeEnum`

## Fields

| Name |
|  --- |
| `DEFERREDINSTALMENTS` |
| `EQUALINSTALMENTS` |
| `INEQUALINSTALMENTS` |

## Example

```python
from adyen.models.instalment_type_enum import InstalmentTypeEnum

instalment_type = InstalmentTypeEnum.EQUALINSTALMENTS
```

