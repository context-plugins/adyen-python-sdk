
# KYC Shareholder Check Result

## Structure

`KYCShareholderCheckResult`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `checks` | [`List[KYCCheckStatusData]`](../../doc/models/kyc-check-status-data.md) | Optional | A list of the checks and their statuses. |
| `legal_arrangement_code` | `str` | Optional | The unique ID of the legal arrangement to which the shareholder belongs, if applicable. |
| `legal_arrangement_entity_code` | `str` | Optional | The unique ID of the legal arrangement entity to which the shareholder belongs, if applicable. |
| `shareholder_code` | `str` | Optional | The code of the shareholder to which the check applies. |

## Example

```python
from adyen.models.kyc_check_status_data import KYCCheckStatusData
from adyen.models.kyc_check_summary_2 import KYCCheckSummary2
from adyen.models.kyc_shareholder_check_result import KYCShareholderCheckResult
from adyen.models.status_32_enum import Status32Enum
from adyen.models.type_211_enum import Type211Enum

kyc_shareholder_check_result = KYCShareholderCheckResult(
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
    legal_arrangement_code='legalArrangementCode0',
    legal_arrangement_entity_code='legalArrangementEntityCode2',
    shareholder_code='shareholderCode6'
)
```

