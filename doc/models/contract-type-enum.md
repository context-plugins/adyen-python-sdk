
# Contract Type Enum

The contract type of the grant offer. Possible value: **cashAdvance**, **loan**., The contract type of the offer.

Possible values:

* **loan**
* **cashAdvance**

## Enumeration

`ContractTypeEnum`

## Fields

| Name |
|  --- |
| `CASHADVANCE` |
| `LOAN` |

## Example

```python
from adyen.models.contract_type_enum import ContractTypeEnum

contract_type = ContractTypeEnum.CASHADVANCE
```

