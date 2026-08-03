
# Instalment Type

Type of instalment transaction. For requesting an instalment payment transaction.
Possible values:

* **DeferredInstalments**
* **EqualInstalments**
* **InequalInstalments**

## Enumeration

`InstalmentType`

## Fields

| Name |
|  --- |
| `DEFERREDINSTALMENTS` |
| `EQUALINSTALMENTS` |
| `INEQUALINSTALMENTS` |

## Example

```python
from adyen.models.instalment_type import InstalmentType

instalment_type = InstalmentType.EQUALINSTALMENTS
```

