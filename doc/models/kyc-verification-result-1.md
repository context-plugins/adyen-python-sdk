
# KYC Verification Result 1

The details of KYC Verification of the account holder.

## Structure

`KYCVerificationResult1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_holder` | [`KYCCheckResult2`](../../doc/models/kyc-check-result-2.md) | Optional | The results of the checks on the account holder. |
| `legal_arrangements` | [`List[KYCLegalArrangementCheckResult]`](../../doc/models/kyc-legal-arrangement-check-result.md) | Optional | The results of the checks on the legal arrangements. |
| `legal_arrangements_entities` | [`List[KYCLegalArrangementEntityCheckResult]`](../../doc/models/kyc-legal-arrangement-entity-check-result.md) | Optional | The results of the checks on the legal arrangement entities. |
| `payout_methods` | [`List[KYCPayoutMethodCheckResult]`](../../doc/models/kyc-payout-method-check-result.md) | Optional | The results of the checks on the payout methods. |
| `shareholders` | [`List[KYCShareholderCheckResult]`](../../doc/models/kyc-shareholder-check-result.md) | Optional | The results of the checks on the shareholders. |
| `signatories` | [`List[KYCSignatoryCheckResult]`](../../doc/models/kyc-signatory-check-result.md) | Optional | The results of the checks on the signatories. |
| `ultimate_parent_company` | [`List[KYCUltimateParentCompanyCheckResult]`](../../doc/models/kyc-ultimate-parent-company-check-result.md) | Optional | The result of the check on the Ultimate Parent Company. |

## Example

```python
from adyen.models.kyc_check_result_2 import KYCCheckResult2
from adyen.models.kyc_check_status_data import KYCCheckStatusData
from adyen.models.kyc_check_summary_2 import KYCCheckSummary2
from adyen.models.kyc_legal_arrangement_check_result import KYCLegalArrangementCheckResult
from adyen.models.kyc_legal_arrangement_entity_check_result import KYCLegalArrangementEntityCheckResult
from adyen.models.kyc_payout_method_check_result import KYCPayoutMethodCheckResult
from adyen.models.kyc_shareholder_check_result import KYCShareholderCheckResult
from adyen.models.kyc_verification_result_1 import KYCVerificationResult1
from adyen.models.status_32_enum import Status32Enum
from adyen.models.type_211_enum import Type211Enum

kyc_verification_result_1 = KYCVerificationResult1(
    account_holder=KYCCheckResult2(
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
        ]
    ),
    legal_arrangements=[
        KYCLegalArrangementCheckResult(
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
                )
            ],
            legal_arrangement_code='legalArrangementCode2'
        ),
        KYCLegalArrangementCheckResult(
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
                )
            ],
            legal_arrangement_code='legalArrangementCode2'
        ),
        KYCLegalArrangementCheckResult(
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
                )
            ],
            legal_arrangement_code='legalArrangementCode2'
        )
    ],
    legal_arrangements_entities=[
        KYCLegalArrangementEntityCheckResult(
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
                )
            ],
            legal_arrangement_code='legalArrangementCode6',
            legal_arrangement_entity_code='legalArrangementEntityCode8'
        ),
        KYCLegalArrangementEntityCheckResult(
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
                )
            ],
            legal_arrangement_code='legalArrangementCode6',
            legal_arrangement_entity_code='legalArrangementEntityCode8'
        ),
        KYCLegalArrangementEntityCheckResult(
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
                )
            ],
            legal_arrangement_code='legalArrangementCode6',
            legal_arrangement_entity_code='legalArrangementEntityCode8'
        )
    ],
    payout_methods=[
        KYCPayoutMethodCheckResult(
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
            payout_method_code='payoutMethodCode8'
        ),
        KYCPayoutMethodCheckResult(
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
            payout_method_code='payoutMethodCode8'
        ),
        KYCPayoutMethodCheckResult(
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
            payout_method_code='payoutMethodCode8'
        )
    ],
    shareholders=[
        KYCShareholderCheckResult(
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
                )
            ],
            legal_arrangement_code='legalArrangementCode0',
            legal_arrangement_entity_code='legalArrangementEntityCode2',
            shareholder_code='shareholderCode6'
        ),
        KYCShareholderCheckResult(
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
                )
            ],
            legal_arrangement_code='legalArrangementCode0',
            legal_arrangement_entity_code='legalArrangementEntityCode2',
            shareholder_code='shareholderCode6'
        ),
        KYCShareholderCheckResult(
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
                )
            ],
            legal_arrangement_code='legalArrangementCode0',
            legal_arrangement_entity_code='legalArrangementEntityCode2',
            shareholder_code='shareholderCode6'
        )
    ]
)
```

