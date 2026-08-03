
# Repayment Term 2

An object containing the details of the configuration for repayment term.

*This model accepts additional fields of type Any.*

## Structure

`RepaymentTerm2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `estimated_days` | `int` | Required | The estimated term for repaying the grant, in days. |
| `maximum_days` | `int` | Optional | The maximum term for repaying the grant, in days. Only applies when `contractType` is **loan**. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.repayment_term_2 import RepaymentTerm2

repayment_term_2 = RepaymentTerm2(
    estimated_days=114,
    maximum_days=146,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

