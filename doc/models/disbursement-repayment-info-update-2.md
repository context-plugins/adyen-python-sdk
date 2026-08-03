
# Disbursement Repayment Info Update 2

Contains information about the basis points configured for repaying the disbursement.

*This model accepts additional fields of type Any.*

## Structure

`DisbursementRepaymentInfoUpdate2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `basis_points` | `int` | Optional | The percentage of your user's incoming net volume that is deducted for repaying the grant. The percentage expressed in [basis points](https://www.investopedia.com/terms/b/basispoint.asp).<br><br>**Constraints**: `>= 0`, `<= 10000` |
| `update_description` | `str` | Optional | **Constraints**: *Minimum Length*: `0`, *Maximum Length*: `240` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.disbursement_repayment_info_update_2 import DisbursementRepaymentInfoUpdate2

disbursement_repayment_info_update_2 = DisbursementRepaymentInfoUpdate2(
    basis_points=34,
    update_description='updateDescription4',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

