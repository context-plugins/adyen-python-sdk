
# Account Holder

## Structure

`AccountHolder`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `balance_platform` | `str` | Optional | The unique identifier of the [balance platform](https://docs.adyen.com/api-explorer/#/balanceplatform/latest/get/balancePlatforms/{id}__queryParam_id) to which the account holder belongs. Required in the request if your API credentials can be used for multiple balance platforms. |
| `capabilities` | [`Dict[str, AccountHolderCapability]`](../../doc/models/account-holder-capability.md) | Optional | Contains key-value pairs that specify the actions that an account holder can do in your platform. The key is a capability required for your integration. For example, **issueCard** for Issuing. The value is an object containing the settings for the capability. |
| `contact_details` | [`ContactDetails1`](../../doc/models/contact-details-1.md) | Optional | Contact details of the account holder. |
| `description` | `str` | Optional | Your description for the account holder.<br><br>**Constraints**: *Maximum Length*: `300` |
| `id` | `str` | Required, Read-only | The unique identifier of the account holder. |
| `legal_entity_id` | `str` | Required | The unique identifier of the [legal entity](https://docs.adyen.com/api-explorer/legalentity/latest/post/legalEntities#responses-200-id) associated with the account holder. Adyen performs a verification process against the legal entity of the account holder. |
| `metadata` | `Dict[str, str]` | Optional | A set of key and value pairs for general use.<br>The keys do not have specific names and may be used for storing miscellaneous data as desired.<br><br>> Note that during an update of metadata, the omission of existing key-value pairs will result in the deletion of those key-value pairs. |
| `migrated_account_holder_code` | `str` | Optional, Read-only | The unique identifier of the migrated account holder in the classic integration. |
| `primary_balance_account` | `str` | Optional | The ID of the account holder's primary balance account. By default, this is set to the first balance account that you create for the account holder. To assign a different balance account, send a PATCH request. |
| `reference` | `str` | Optional | Your reference for the account holder.<br><br>**Constraints**: *Maximum Length*: `150` |
| `status` | [`Status9Enum`](../../doc/models/status-9-enum.md) | Optional | The status of the account holder.<br><br>Possible values:<br><br>* **active**: The account holder is active and allowed to use its capabilities. This is the initial status for account holders and balance accounts. You can change this status to **suspended** or **closed**.<br><br>* **suspended**: The account holder is temporarily disabled and payouts are blocked. You can change this status to **active** or **closed**.<br><br>* **closed**: The account holder and all of its capabilities are permanently disabled. This is a final status and cannot be changed. |
| `time_zone` | `str` | Optional | The time zone of the account holder. For example, **Europe/Amsterdam**.<br>Defaults to the time zone of the balance platform if no time zone is set. For possible values, see the [list of time zone codes](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones). |
| `verification_deadlines` | [`List[VerificationDeadline]`](../../doc/models/verification-deadline.md) | Optional, Read-only | List of verification deadlines and the capabilities that will be disallowed if verification errors are not resolved. |

## Example

```python
from adyen.models.account_holder import AccountHolder
from adyen.models.account_holder_capability import AccountHolderCapability
from adyen.models.address import Address
from adyen.models.amount_17 import Amount17
from adyen.models.capability_settings_3 import CapabilitySettings3
from adyen.models.contact_details_1 import ContactDetails1
from adyen.models.funding_source_enum import FundingSourceEnum
from adyen.models.interval_enum import IntervalEnum
from adyen.models.phone_31 import Phone31
from adyen.models.type_410_enum import Type410Enum

account_holder = AccountHolder(
    id=None,
    legal_entity_id='legalEntityId4',
    balance_platform='balancePlatform2',
    capabilities={
        'key0': AccountHolderCapability(
            allowed_settings=CapabilitySettings3(
                amount_per_industry={
                    'key0': Amount17(
                        currency='currency8',
                        value=56
                    ),
                    'key1': Amount17(
                        currency='currency8',
                        value=56
                    )
                },
                authorized_card_users=False,
                funding_source=[
                    FundingSourceEnum.CREDIT,
                    FundingSourceEnum.DEBIT,
                    FundingSourceEnum.PREPAID
                ],
                interval=IntervalEnum.DAILY,
                max_amount=Amount17(
                    currency='currency4',
                    value=160
                )
            ),
            enabled=False
        ),
        'key1': AccountHolderCapability(
            allowed_settings=CapabilitySettings3(
                amount_per_industry={
                    'key0': Amount17(
                        currency='currency8',
                        value=56
                    ),
                    'key1': Amount17(
                        currency='currency8',
                        value=56
                    )
                },
                authorized_card_users=False,
                funding_source=[
                    FundingSourceEnum.CREDIT,
                    FundingSourceEnum.DEBIT,
                    FundingSourceEnum.PREPAID
                ],
                interval=IntervalEnum.DAILY,
                max_amount=Amount17(
                    currency='currency4',
                    value=160
                )
            ),
            enabled=False
        )
    },
    contact_details=ContactDetails1(
        address=Address(
            city='city6',
            country='country0',
            house_number_or_name='houseNumberOrName4',
            postal_code='postalCode8',
            street='street6',
            state_or_province='stateOrProvince4'
        ),
        email='email6',
        phone=Phone31(
            number='number8',
            mtype=Type410Enum.LANDLINE
        ),
        web_address='webAddress0'
    ),
    description='description0',
    metadata={
        'key0': 'metadata3'
    }
)
```

