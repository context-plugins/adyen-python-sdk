
# Repayment Term

Contains information about the time period in which your user must repay the total amount of the grant.

*This model accepts additional fields of type Any.*

## Structure

`RepaymentTerm`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `estimated_days` | `int` | Required | The estimated term for repaying the grant, in days. |
| `maximum_days` | `int` | Optional | The maximum term for repaying the grant, in days. Only applies when `contractType` is **loan**. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.repayment_term import RepaymentTerm

repayment_term = RepaymentTerm(
    estimated_days=246,
    maximum_days=22,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

