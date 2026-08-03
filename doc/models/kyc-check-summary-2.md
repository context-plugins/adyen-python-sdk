
# Kyc Check Summary 2

A summary of the execution of the check.

*This model accepts additional fields of type Any.*

## Structure

`KycCheckSummary2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `kyc_check_code` | `int` | Optional | The code of the check. For possible values, refer to [Verification codes](https://docs.adyen.com/classic-platforms/verification-process/verification-codes). |
| `kyc_check_description` | `str` | Optional | A description of the check. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.kyc_check_summary_2 import KycCheckSummary2

kyc_check_summary_2 = KycCheckSummary2(
    kyc_check_code=98,
    kyc_check_description='kycCheckDescription4',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

