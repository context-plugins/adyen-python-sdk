
# Kyc Verification Result

*This model accepts additional fields of type Any.*

## Structure

`KycVerificationResult`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_holder` | [`KycCheckResult`](../../doc/models/kyc-check-result.md) | Optional | - |
| `legal_arrangements` | [`List[KycLegalArrangementCheckResult]`](../../doc/models/kyc-legal-arrangement-check-result.md) | Optional | The results of the checks on the legal arrangements. |
| `legal_arrangements_entities` | [`List[KycLegalArrangementEntityCheckResult]`](../../doc/models/kyc-legal-arrangement-entity-check-result.md) | Optional | The results of the checks on the legal arrangement entities. |
| `payout_methods` | [`List[KycPayoutMethodCheckResult]`](../../doc/models/kyc-payout-method-check-result.md) | Optional | The results of the checks on the payout methods. |
| `shareholders` | [`List[KycShareholderCheckResult]`](../../doc/models/kyc-shareholder-check-result.md) | Optional | The results of the checks on the shareholders. |
| `signatories` | [`List[KycSignatoryCheckResult]`](../../doc/models/kyc-signatory-check-result.md) | Optional | The results of the checks on the signatories. |
| `ultimate_parent_company` | [`List[KycUltimateParentCompanyCheckResult]`](../../doc/models/kyc-ultimate-parent-company-check-result.md) | Optional | The result of the check on the Ultimate Parent Company. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.kyc_check_result import KycCheckResult
from adyen.models.kyc_check_status_data import KycCheckStatusData
from adyen.models.kyc_check_summary import KycCheckSummary
from adyen.models.kyc_legal_arrangement_check_result import KycLegalArrangementCheckResult
from adyen.models.kyc_legal_arrangement_entity_check_result import KycLegalArrangementEntityCheckResult
from adyen.models.kyc_payout_method_check_result import KycPayoutMethodCheckResult
from adyen.models.kyc_shareholder_check_result import KycShareholderCheckResult
from adyen.models.kyc_verification_result import KycVerificationResult
from adyen.models.status_3 import Status3
from adyen.models.type_2 import Type2

kyc_verification_result = KycVerificationResult(
    account_holder=KycCheckResult(
        checks=[
            KycCheckStatusData(
                status=Status3.INVALID_DATA,
                mtype=Type2.PASSPORT_VERIFICATION,
                required_fields=[
                    'requiredFields0',
                    'requiredFields1'
                ],
                summary=KycCheckSummary(
                    kyc_check_code=128,
                    kyc_check_description='kycCheckDescription8',
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            KycCheckStatusData(
                status=Status3.INVALID_DATA,
                mtype=Type2.PASSPORT_VERIFICATION,
                required_fields=[
                    'requiredFields0',
                    'requiredFields1'
                ],
                summary=KycCheckSummary(
                    kyc_check_code=128,
                    kyc_check_description='kycCheckDescription8',
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            KycCheckStatusData(
                status=Status3.INVALID_DATA,
                mtype=Type2.PASSPORT_VERIFICATION,
                required_fields=[
                    'requiredFields0',
                    'requiredFields1'
                ],
                summary=KycCheckSummary(
                    kyc_check_code=128,
                    kyc_check_description='kycCheckDescription8',
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            )
        ],
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    legal_arrangements=[
        KycLegalArrangementCheckResult(
            checks=[
                KycCheckStatusData(
                    status=Status3.INVALID_DATA,
                    mtype=Type2.PASSPORT_VERIFICATION,
                    required_fields=[
                        'requiredFields0',
                        'requiredFields1'
                    ],
                    summary=KycCheckSummary(
                        kyc_check_code=128,
                        kyc_check_description='kycCheckDescription8',
                        additional_properties={
                            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                        }
                    ),
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                )
            ],
            legal_arrangement_code='legalArrangementCode2',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        KycLegalArrangementCheckResult(
            checks=[
                KycCheckStatusData(
                    status=Status3.INVALID_DATA,
                    mtype=Type2.PASSPORT_VERIFICATION,
                    required_fields=[
                        'requiredFields0',
                        'requiredFields1'
                    ],
                    summary=KycCheckSummary(
                        kyc_check_code=128,
                        kyc_check_description='kycCheckDescription8',
                        additional_properties={
                            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                        }
                    ),
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                )
            ],
            legal_arrangement_code='legalArrangementCode2',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    legal_arrangements_entities=[
        KycLegalArrangementEntityCheckResult(
            checks=[
                KycCheckStatusData(
                    status=Status3.INVALID_DATA,
                    mtype=Type2.PASSPORT_VERIFICATION,
                    required_fields=[
                        'requiredFields0',
                        'requiredFields1'
                    ],
                    summary=KycCheckSummary(
                        kyc_check_code=128,
                        kyc_check_description='kycCheckDescription8',
                        additional_properties={
                            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                        }
                    ),
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                )
            ],
            legal_arrangement_code='legalArrangementCode6',
            legal_arrangement_entity_code='legalArrangementEntityCode8',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        KycLegalArrangementEntityCheckResult(
            checks=[
                KycCheckStatusData(
                    status=Status3.INVALID_DATA,
                    mtype=Type2.PASSPORT_VERIFICATION,
                    required_fields=[
                        'requiredFields0',
                        'requiredFields1'
                    ],
                    summary=KycCheckSummary(
                        kyc_check_code=128,
                        kyc_check_description='kycCheckDescription8',
                        additional_properties={
                            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                        }
                    ),
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                )
            ],
            legal_arrangement_code='legalArrangementCode6',
            legal_arrangement_entity_code='legalArrangementEntityCode8',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    payout_methods=[
        KycPayoutMethodCheckResult(
            checks=[
                KycCheckStatusData(
                    status=Status3.INVALID_DATA,
                    mtype=Type2.PASSPORT_VERIFICATION,
                    required_fields=[
                        'requiredFields0',
                        'requiredFields1'
                    ],
                    summary=KycCheckSummary(
                        kyc_check_code=128,
                        kyc_check_description='kycCheckDescription8',
                        additional_properties={
                            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                        }
                    ),
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
                KycCheckStatusData(
                    status=Status3.INVALID_DATA,
                    mtype=Type2.PASSPORT_VERIFICATION,
                    required_fields=[
                        'requiredFields0',
                        'requiredFields1'
                    ],
                    summary=KycCheckSummary(
                        kyc_check_code=128,
                        kyc_check_description='kycCheckDescription8',
                        additional_properties={
                            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                        }
                    ),
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                )
            ],
            payout_method_code='payoutMethodCode8',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        KycPayoutMethodCheckResult(
            checks=[
                KycCheckStatusData(
                    status=Status3.INVALID_DATA,
                    mtype=Type2.PASSPORT_VERIFICATION,
                    required_fields=[
                        'requiredFields0',
                        'requiredFields1'
                    ],
                    summary=KycCheckSummary(
                        kyc_check_code=128,
                        kyc_check_description='kycCheckDescription8',
                        additional_properties={
                            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                        }
                    ),
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
                KycCheckStatusData(
                    status=Status3.INVALID_DATA,
                    mtype=Type2.PASSPORT_VERIFICATION,
                    required_fields=[
                        'requiredFields0',
                        'requiredFields1'
                    ],
                    summary=KycCheckSummary(
                        kyc_check_code=128,
                        kyc_check_description='kycCheckDescription8',
                        additional_properties={
                            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                        }
                    ),
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                )
            ],
            payout_method_code='payoutMethodCode8',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    shareholders=[
        KycShareholderCheckResult(
            checks=[
                KycCheckStatusData(
                    status=Status3.INVALID_DATA,
                    mtype=Type2.PASSPORT_VERIFICATION,
                    required_fields=[
                        'requiredFields0',
                        'requiredFields1'
                    ],
                    summary=KycCheckSummary(
                        kyc_check_code=128,
                        kyc_check_description='kycCheckDescription8',
                        additional_properties={
                            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                        }
                    ),
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                )
            ],
            legal_arrangement_code='legalArrangementCode0',
            legal_arrangement_entity_code='legalArrangementEntityCode2',
            shareholder_code='shareholderCode6',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        KycShareholderCheckResult(
            checks=[
                KycCheckStatusData(
                    status=Status3.INVALID_DATA,
                    mtype=Type2.PASSPORT_VERIFICATION,
                    required_fields=[
                        'requiredFields0',
                        'requiredFields1'
                    ],
                    summary=KycCheckSummary(
                        kyc_check_code=128,
                        kyc_check_description='kycCheckDescription8',
                        additional_properties={
                            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                        }
                    ),
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                )
            ],
            legal_arrangement_code='legalArrangementCode0',
            legal_arrangement_entity_code='legalArrangementEntityCode2',
            shareholder_code='shareholderCode6',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

