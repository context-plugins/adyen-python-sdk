
# KYC Payout Method Check Result

## Structure

`KYCPayoutMethodCheckResult`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `checks` | [`List[KYCCheckStatusData]`](../../doc/models/kyc-check-status-data.md) | Optional | A list of the checks and their statuses. |
| `payout_method_code` | `str` | Optional | The unique ID of the payoput method to which the check applies. |

## Example

```python
from adyen.models.kyc_check_status_data import KYCCheckStatusData
from adyen.models.kyc_check_summary_2 import KYCCheckSummary2
from adyen.models.kyc_payout_method_check_result import KYCPayoutMethodCheckResult
from adyen.models.status_32_enum import Status32Enum
from adyen.models.type_211_enum import Type211Enum

kyc_payout_method_check_result = KYCPayoutMethodCheckResult(
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
    payout_method_code='payoutMethodCode6'
)
```

