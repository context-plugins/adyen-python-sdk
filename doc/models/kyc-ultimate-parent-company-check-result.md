
# KYC Ultimate Parent Company Check Result

## Structure

`KYCUltimateParentCompanyCheckResult`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `checks` | [`List[KYCCheckStatusData]`](../../doc/models/kyc-check-status-data.md) | Optional | A list of the checks and their statuses. |
| `ultimate_parent_company_code` | `str` | Optional | The code of the Ultimate Parent Company to which the check applies. |

## Example

```python
from adyen.models.kyc_check_status_data import KYCCheckStatusData
from adyen.models.kyc_check_summary_2 import KYCCheckSummary2
from adyen.models.kyc_ultimate_parent_company_check_result import KYCUltimateParentCompanyCheckResult
from adyen.models.status_32_enum import Status32Enum
from adyen.models.type_211_enum import Type211Enum

kyc_ultimate_parent_company_check_result = KYCUltimateParentCompanyCheckResult(
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
    ultimate_parent_company_code='ultimateParentCompanyCode2'
)
```

