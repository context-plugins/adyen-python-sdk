
# KYC Check Summary

## Structure

`KYCCheckSummary`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `kyc_check_code` | `int` | Optional | The code of the check. For possible values, refer to [Verification codes](https://docs.adyen.com/classic-platforms/verification-process/verification-codes). |
| `kyc_check_description` | `str` | Optional | A description of the check. |

## Example

```python
from adyen.models.kyc_check_summary import KYCCheckSummary

kyc_check_summary = KYCCheckSummary(
    kyc_check_code=6,
    kyc_check_description='kycCheckDescription0'
)
```

