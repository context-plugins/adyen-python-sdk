
# Disbursement Repayment 2

Contains information about the basis points configured for repaying the disbursement.

## Structure

`DisbursementRepayment2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `basis_points` | `int` | Required | The percentage of your user's incoming net volume that is deducted for repaying the grant. The percentage expressed in [basis points](https://www.investopedia.com/terms/b/basispoint.asp).<br><br>**Constraints**: `>= 0`, `<= 10000` |
| `update_description` | `str` | Required | **Constraints**: *Minimum Length*: `1`, *Maximum Length*: `240` |

## Example

```python
from adyen.models.disbursement_repayment_2 import DisbursementRepayment2

disbursement_repayment_2 = DisbursementRepayment2(
    basis_points=54,
    update_description='updateDescription8'
)
```

