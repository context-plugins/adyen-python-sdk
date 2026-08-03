
# Disbursement Repayment Info Update

*This model accepts additional fields of type Any.*

## Structure

`DisbursementRepaymentInfoUpdate`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `basis_points` | `int` | Optional | The percentage of your user's incoming net volume that is deducted for repaying the grant. The percentage expressed in [basis points](https://www.investopedia.com/terms/b/basispoint.asp).<br><br>**Constraints**: `>= 0`, `<= 10000` |
| `update_description` | `str` | Optional | **Constraints**: *Minimum Length*: `0`, *Maximum Length*: `240` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.disbursement_repayment_info_update import DisbursementRepaymentInfoUpdate

disbursement_repayment_info_update = DisbursementRepaymentInfoUpdate(
    basis_points=84,
    update_description='updateDescription6',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

