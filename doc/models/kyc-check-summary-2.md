
# KYC Check Summary 2

A summary of the execution of the check.

## Structure

`KYCCheckSummary2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `kyc_check_code` | `int` | Optional | The code of the check. For possible values, refer to [Verification codes](https://docs.adyen.com/classic-platforms/verification-process/verification-codes). |
| `kyc_check_description` | `str` | Optional | A description of the check. |

## Example

```python
from adyen.models.kyc_check_summary_2 import KYCCheckSummary2

kyc_check_summary_2 = KYCCheckSummary2(
    kyc_check_code=98,
    kyc_check_description='kycCheckDescription4'
)
```

