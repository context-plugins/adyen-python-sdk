
# KYC Signatory Check Result

## Structure

`KYCSignatoryCheckResult`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `checks` | [`List[KYCCheckStatusData]`](../../doc/models/kyc-check-status-data.md) | Optional | A list of the checks and their statuses. |
| `signatory_code` | `str` | Optional | The code of the signatory to which the check applies. |

## Example

```python
from adyen.models.kyc_check_status_data import KYCCheckStatusData
from adyen.models.kyc_check_summary_2 import KYCCheckSummary2
from adyen.models.kyc_signatory_check_result import KYCSignatoryCheckResult
from adyen.models.status_32_enum import Status32Enum
from adyen.models.type_211_enum import Type211Enum

kyc_signatory_check_result = KYCSignatoryCheckResult(
    checks=[
        KYCCheckStatusData(
            status=Status32Enum.INVALID_DATA,
            mtype=Type211Enum.PASSPORT_VERIFICATION,
            required_fields=[
                'requiredFields0',
                'requiredFields1'
            ],
            summary=KYCCheckSummary2(
                kyc_check_code=128,
                kyc_check_description='kycCheckDescription8'
            )
        ),
        KYCCheckStatusData(
            status=Status32Enum.INVALID_DATA,
            mtype=Type211Enum.PASSPORT_VERIFICATION,
            required_fields=[
                'requiredFields0',
                'requiredFields1'
            ],
            summary=KYCCheckSummary2(
                kyc_check_code=128,
                kyc_check_description='kycCheckDescription8'
            )
        )
    ],
    signatory_code='signatoryCode2'
)
```

