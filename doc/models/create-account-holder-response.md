
# Create Account Holder Response

*This model accepts additional fields of type Any.*

## Structure

`CreateAccountHolderResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_code` | `str` | Optional | The code of a new account created for the account holder. |
| `account_holder_code` | `str` | Optional | The code of the new account holder. |
| `account_holder_details` | [`AccountHolderDetails`](../../doc/models/account-holder-details.md) | Optional | - |
| `account_holder_status` | [`AccountHolderStatus`](../../doc/models/account-holder-status.md) | Optional | - |
| `description` | `str` | Optional | The description of the new account holder. |
| `invalid_fields` | [`List[ErrorFieldType]`](../../doc/models/error-field-type.md) | Optional | A list of fields that caused the `/createAccountHolder` request to fail. |
| `legal_entity` | [`LegalEntity1`](../../doc/models/legal-entity-1.md) | Optional | - |
| `primary_currency` | `str` | Optional | The three-character [ISO currency code](https://docs.adyen.com/development-resources/currency-codes), with which the prospective account holder primarily deals. |
| `psp_reference` | `str` | Optional | The reference of a request. Can be used to uniquely identify the request. |
| `result_code` | `str` | Optional | The result code. |
| `verification` | [`KycVerificationResult`](../../doc/models/kyc-verification-result.md) | Optional | - |
| `verification_profile` | `str` | Optional | The identifier of the profile that applies to this entity. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from adyen.models.account_event import AccountEvent
from adyen.models.account_holder_details import AccountHolderDetails
from adyen.models.account_holder_status import AccountHolderStatus
from adyen.models.account_payout_state import AccountPayoutState
from adyen.models.account_processing_state import AccountProcessingState
from adyen.models.bank_account_detail import BankAccountDetail
from adyen.models.business_details import BusinessDetails
from adyen.models.create_account_holder_response import CreateAccountHolderResponse
from adyen.models.event import Event
from adyen.models.gender import Gender
from adyen.models.payout_limit import PayoutLimit
from adyen.models.processed_from import ProcessedFrom
from adyen.models.processed_to import ProcessedTo
from adyen.models.shareholder_contact import ShareholderContact
from adyen.models.status_1 import Status1
from adyen.models.ultimate_parent_company import UltimateParentCompany
from adyen.models.ultimate_parent_company_business_details import UltimateParentCompanyBusinessDetails
from adyen.models.vias_address import ViasAddress
from adyen.models.vias_name import ViasName

create_account_holder_response = CreateAccountHolderResponse(
    account_code='accountCode0',
    account_holder_code='accountHolderCode6',
    account_holder_details=AccountHolderDetails(
        address=ViasAddress(
            country='country0',
            city='city6',
            house_number_or_name='houseNumberOrName4',
            postal_code='postalCode8',
            state_or_province='stateOrProvince4',
            street='street6',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        bank_account_details=[
            BankAccountDetail(
                account_number='accountNumber8',
                account_type='accountType4',
                bank_account_name='bankAccountName4',
                bank_account_reference='bankAccountReference4',
                bank_account_uuid='bankAccountUUID0',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            BankAccountDetail(
                account_number='accountNumber8',
                account_type='accountType4',
                bank_account_name='bankAccountName4',
                bank_account_reference='bankAccountReference4',
                bank_account_uuid='bankAccountUUID0',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            BankAccountDetail(
                account_number='accountNumber8',
                account_type='accountType4',
                bank_account_name='bankAccountName4',
                bank_account_reference='bankAccountReference4',
                bank_account_uuid='bankAccountUUID0',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            )
        ],
        bank_aggregator_data_reference='bankAggregatorDataReference6',
        business_details=BusinessDetails(
            doing_business_as='doingBusinessAs6',
            legal_business_name='legalBusinessName8',
            listed_ultimate_parent_company=[
                UltimateParentCompany(
                    address=ViasAddress(
                        country='country0',
                        city='city6',
                        house_number_or_name='houseNumberOrName4',
                        postal_code='postalCode8',
                        state_or_province='stateOrProvince4',
                        street='street6',
                        additional_properties={
                            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                        }
                    ),
                    business_details=UltimateParentCompanyBusinessDetails(
                        legal_business_name='legalBusinessName8',
                        registration_number='registrationNumber6',
                        stock_exchange='stockExchange4',
                        stock_number='stockNumber6',
                        stock_ticker='stockTicker6',
                        additional_properties={
                            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                        }
                    ),
                    ultimate_parent_company_code='ultimateParentCompanyCode2',
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
                UltimateParentCompany(
                    address=ViasAddress(
                        country='country0',
                        city='city6',
                        house_number_or_name='houseNumberOrName4',
                        postal_code='postalCode8',
                        state_or_province='stateOrProvince4',
                        street='street6',
                        additional_properties={
                            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                        }
                    ),
                    business_details=UltimateParentCompanyBusinessDetails(
                        legal_business_name='legalBusinessName8',
                        registration_number='registrationNumber6',
                        stock_exchange='stockExchange4',
                        stock_number='stockNumber6',
                        stock_ticker='stockTicker6',
                        additional_properties={
                            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                        }
                    ),
                    ultimate_parent_company_code='ultimateParentCompanyCode2',
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                )
            ],
            registration_number='registrationNumber6',
            shareholders=[
                ShareholderContact(
                    address=ViasAddress(
                        country='country0',
                        city='city6',
                        house_number_or_name='houseNumberOrName4',
                        postal_code='postalCode8',
                        state_or_province='stateOrProvince4',
                        street='street6',
                        additional_properties={
                            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                        }
                    ),
                    email='email8',
                    full_phone_number='fullPhoneNumber2',
                    job_title='jobTitle2',
                    name=ViasName(
                        first_name='firstName4',
                        gender=Gender.MALE,
                        infix='infix4',
                        last_name='lastName4',
                        additional_properties={
                            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                        }
                    ),
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
                ShareholderContact(
                    address=ViasAddress(
                        country='country0',
                        city='city6',
                        house_number_or_name='houseNumberOrName4',
                        postal_code='postalCode8',
                        state_or_province='stateOrProvince4',
                        street='street6',
                        additional_properties={
                            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                        }
                    ),
                    email='email8',
                    full_phone_number='fullPhoneNumber2',
                    job_title='jobTitle2',
                    name=ViasName(
                        first_name='firstName4',
                        gender=Gender.MALE,
                        infix='infix4',
                        last_name='lastName4',
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
        email='email2',
        full_phone_number='fullPhoneNumber8',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    account_holder_status=AccountHolderStatus(
        status=Status1.INACTIVE,
        events=[
            AccountEvent(
                event=Event.INACTIVATEACCOUNT,
                execution_date=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
                reason='reason6',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            )
        ],
        payout_state=AccountPayoutState(
            allow_payout=False,
            disable_reason='disableReason2',
            disabled=False,
            not_allowed_reason='notAllowedReason4',
            payout_limit=PayoutLimit(
                currency='currency8',
                value=88,
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        processing_state=AccountProcessingState(
            disable_reason='disableReason2',
            disabled=False,
            processed_from=ProcessedFrom(
                currency='currency4',
                value=148,
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            processed_to=ProcessedTo(
                currency='currency2',
                value=54,
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            tier_number=156,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        status_reason='statusReason8',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    description='description0',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

