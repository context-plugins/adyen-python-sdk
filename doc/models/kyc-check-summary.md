
# Kyc Check Summary

*This model accepts additional fields of type Any.*

## Structure

`KycCheckSummary`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `kyc_check_code` | `int` | Optional | The code of the check. For possible values, refer to [Verification codes](https://docs.adyen.com/classic-platforms/verification-process/verification-codes). |
| `kyc_check_description` | `str` | Optional | A description of the check. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.kyc_check_summary import KycCheckSummary

kyc_check_summary = KycCheckSummary(
    kyc_check_code=6,
    kyc_check_description='kycCheckDescription0',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

