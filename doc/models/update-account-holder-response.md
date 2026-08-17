
# Update Account Holder Response

## Structure

`UpdateAccountHolderResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_holder_code` | `str` | Optional | The code of the account holder. |
| `account_holder_details` | [`AccountHolderDetails3`](../../doc/models/account-holder-details-3.md) | Optional | Details of the account holder. |
| `account_holder_status` | [`AccountHolderStatus7`](../../doc/models/account-holder-status-7.md) | Optional | The new status of the account holder. |
| `description` | `str` | Optional | The description of the account holder. |
| `invalid_fields` | [`List[ErrorFieldType]`](../../doc/models/error-field-type.md) | Optional | in case the account holder has not been updated, contains account holder fields, that did not pass the validation. |
| `legal_entity` | [`LegalEntity2Enum`](../../doc/models/legal-entity-2-enum.md) | Optional | The legal entity of the account holder. |
| `primary_currency` | `str` | Optional | The three-character [ISO currency code](https://docs.adyen.com/development-resources/currency-codes), with which the prospective account holder primarily deals. |
| `psp_reference` | `str` | Optional | The reference of a request. Can be used to uniquely identify the request. |
| `result_code` | `str` | Optional | The result code. |
| `verification` | [`KYCVerificationResult1`](../../doc/models/kyc-verification-result-1.md) | Optional | The details of KYC Verification of the account holder. |
| `verification_profile` | `str` | Optional | The identifier of the profile that applies to this entity. |

## Example

```python
import dateutil.parser

from adyen.models.account_event import AccountEvent
from adyen.models.account_holder_details_3 import AccountHolderDetails3
from adyen.models.account_holder_status_7 import AccountHolderStatus7
from adyen.models.account_payout_state_2 import AccountPayoutState2
from adyen.models.account_processing_state_2 import AccountProcessingState2
from adyen.models.amount import Amount
from adyen.models.bank_account_detail import BankAccountDetail
from adyen.models.business_details_3 import BusinessDetails3
from adyen.models.error_field_type import ErrorFieldType
from adyen.models.event_enum import EventEnum
from adyen.models.field_name_enum import FieldNameEnum
from adyen.models.field_type import FieldType
from adyen.models.gender_enum import GenderEnum
from adyen.models.shareholder_contact import ShareholderContact
from adyen.models.status_12_enum import Status12Enum
from adyen.models.ultimate_parent_company import UltimateParentCompany
from adyen.models.ultimate_parent_company_business_details_2 import UltimateParentCompanyBusinessDetails2
from adyen.models.update_account_holder_response import UpdateAccountHolderResponse
from adyen.models.vias_address_1 import ViasAddress1
from adyen.models.vias_address_2 import ViasAddress2
from adyen.models.vias_address_9 import ViasAddress9
from adyen.models.vias_name_1 import ViasName1

update_account_holder_response = UpdateAccountHolderResponse(
    account_holder_code='accountHolderCode4',
    account_holder_details=AccountHolderDetails3(
        address=ViasAddress9(
            country='country0',
            city='city6',
            house_number_or_name='houseNumberOrName4',
            postal_code='postalCode8',
            state_or_province='stateOrProvince4',
            street='street6'
        ),
        bank_account_details=[
            BankAccountDetail(
                account_number='accountNumber8',
                account_type='accountType4',
                bank_account_name='bankAccountName4',
                bank_account_reference='bankAccountReference4',
                bank_account_uuid='bankAccountUUID0'
            ),
            BankAccountDetail(
                account_number='accountNumber8',
                account_type='accountType4',
                bank_account_name='bankAccountName4',
                bank_account_reference='bankAccountReference4',
                bank_account_uuid='bankAccountUUID0'
            ),
            BankAccountDetail(
                account_number='accountNumber8',
                account_type='accountType4',
                bank_account_name='bankAccountName4',
                bank_account_reference='bankAccountReference4',
                bank_account_uuid='bankAccountUUID0'
            )
        ],
        bank_aggregator_data_reference='bankAggregatorDataReference6',
        business_details=BusinessDetails3(
            doing_business_as='doingBusinessAs6',
            legal_business_name='legalBusinessName8',
            listed_ultimate_parent_company=[
                UltimateParentCompany(
                    address=ViasAddress1(
                        country='country0',
                        city='city6',
                        house_number_or_name='houseNumberOrName4',
                        postal_code='postalCode8',
                        state_or_province='stateOrProvince4',
                        street='street6'
                    ),
                    business_details=UltimateParentCompanyBusinessDetails2(
                        legal_business_name='legalBusinessName8',
                        registration_number='registrationNumber6',
                        stock_exchange='stockExchange4',
                        stock_number='stockNumber6',
                        stock_ticker='stockTicker6'
                    ),
                    ultimate_parent_company_code='ultimateParentCompanyCode2'
                ),
                UltimateParentCompany(
                    address=ViasAddress1(
                        country='country0',
                        city='city6',
                        house_number_or_name='houseNumberOrName4',
                        postal_code='postalCode8',
                        state_or_province='stateOrProvince4',
                        street='street6'
                    ),
                    business_details=UltimateParentCompanyBusinessDetails2(
                        legal_business_name='legalBusinessName8',
                        registration_number='registrationNumber6',
                        stock_exchange='stockExchange4',
                        stock_number='stockNumber6',
                        stock_ticker='stockTicker6'
                    ),
                    ultimate_parent_company_code='ultimateParentCompanyCode2'
                )
            ],
            registration_number='registrationNumber6',
            shareholders=[
                ShareholderContact(
                    address=ViasAddress2(
                        country='country0',
                        city='city6',
                        house_number_or_name='houseNumberOrName4',
                        postal_code='postalCode8',
                        state_or_province='stateOrProvince4',
                        street='street6'
                    ),
                    email='email8',
                    full_phone_number='fullPhoneNumber2',
                    job_title='jobTitle2',
                    name=ViasName1(
                        first_name='firstName4',
                        gender=GenderEnum.MALE,
                        infix='infix4',
                        last_name='lastName4'
                    )
                ),
                ShareholderContact(
                    address=ViasAddress2(
                        country='country0',
                        city='city6',
                        house_number_or_name='houseNumberOrName4',
                        postal_code='postalCode8',
                        state_or_province='stateOrProvince4',
                        street='street6'
                    ),
                    email='email8',
                    full_phone_number='fullPhoneNumber2',
                    job_title='jobTitle2',
                    name=ViasName1(
                        first_name='firstName4',
                        gender=GenderEnum.MALE,
                        infix='infix4',
                        last_name='lastName4'
                    )
                )
            ]
        ),
        email='email2',
        full_phone_number='fullPhoneNumber8'
    ),
    account_holder_status=AccountHolderStatus7(
        status=Status12Enum.INACTIVE,
        events=[
            AccountEvent(
                event=EventEnum.INACTIVATEACCOUNT,
                execution_date=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
                reason='reason6'
            )
        ],
        payout_state=AccountPayoutState2(
            allow_payout=False,
            disable_reason='disableReason2',
            disabled=False,
            not_allowed_reason='notAllowedReason4',
            payout_limit=Amount(
                currency='currency8',
                value=88
            )
        ),
        processing_state=AccountProcessingState2(
            disable_reason='disableReason2',
            disabled=False,
            processed_from=Amount(
                currency='currency4',
                value=148
            ),
            processed_to=Amount(
                currency='currency2',
                value=54
            ),
            tier_number=156
        ),
        status_reason='statusReason8'
    ),
    description='description8',
    invalid_fields=[
        ErrorFieldType(
            error_code=78,
            error_description='errorDescription6',
            field_type=FieldType(
                field='field6',
                field_name=FieldNameEnum.DRIVINGLICENCEFRONT,
                shareholder_code='shareholderCode0'
            )
        ),
        ErrorFieldType(
            error_code=78,
            error_description='errorDescription6',
            field_type=FieldType(
                field='field6',
                field_name=FieldNameEnum.DRIVINGLICENCEFRONT,
                shareholder_code='shareholderCode0'
            )
        ),
        ErrorFieldType(
            error_code=78,
            error_description='errorDescription6',
            field_type=FieldType(
                field='field6',
                field_name=FieldNameEnum.DRIVINGLICENCEFRONT,
                shareholder_code='shareholderCode0'
            )
        )
    ]
)
```

