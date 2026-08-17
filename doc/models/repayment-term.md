
# Repayment Term

An object containing the details of the configuration for repayment term., Contains information about the time period in which your user must repay the total amount of the grant.

## Structure

`RepaymentTerm`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `estimated_days` | `int` | Required | The estimated term for repaying the grant, in days. |
| `maximum_days` | `int` | Optional | The maximum term for repaying the grant, in days. Only applies when `contractType` is **loan**. |

## Example

```python
from adyen.models.repayment_term import RepaymentTerm

repayment_term = RepaymentTerm(
    estimated_days=246,
    maximum_days=22
)
```

