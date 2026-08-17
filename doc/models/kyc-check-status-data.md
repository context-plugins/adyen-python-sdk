
# KYC Check Status Data

## Structure

`KYCCheckStatusData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `required_fields` | `List[str]` | Optional | A list of the fields required for execution of the check. |
| `status` | [`Status32Enum`](../../doc/models/status-32-enum.md) | Required | The status of the check.<br><br>Possible values: **AWAITING_DATA** , **DATA_PROVIDED**, **FAILED**, **INVALID_DATA**, **PASSED**, **PENDING**, **RETRY_LIMIT_REACHED**. |
| `summary` | [`KYCCheckSummary2`](../../doc/models/kyc-check-summary-2.md) | Optional | A summary of the execution of the check. |
| `mtype` | [`Type211Enum`](../../doc/models/type-211-enum.md) | Required | The type of check.<br><br>Possible values:<br><br>* **BANK_ACCOUNT_VERIFICATION**: Used in v5 and earlier. Replaced by **PAYOUT_METHOD_VERIFICATION** in v6 and later.<br><br>* **COMPANY_VERIFICATION**<br><br>* **CARD_VERIFICATION**<br><br>* **IDENTITY_VERIFICATION**<br><br>* **LEGAL_ARRANGEMENT_VERIFICATION**<br><br>* **NONPROFIT_VERIFICATION**<br><br>* **PASSPORT_VERIFICATION**<br><br>* **PAYOUT_METHOD_VERIFICATION**: Used in v6 and later.<br><br>* **PCI_VERIFICATION** |

## Example

```python
from adyen.models.kyc_check_status_data import KYCCheckStatusData
from adyen.models.kyc_check_summary_2 import KYCCheckSummary2
from adyen.models.status_32_enum import Status32Enum
from adyen.models.type_211_enum import Type211Enum

kyc_check_status_data = KYCCheckStatusData(
    status=Status32Enum.PENDING,
    mtype=Type211Enum.PAYOUT_METHOD_VERIFICATION,
    required_fields=[
        'requiredFields8',
        'requiredFields7',
        'requiredFields6'
    ],
    summary=KYCCheckSummary2(
        kyc_check_code=128,
        kyc_check_description='kycCheckDescription8'
    )
)
```

