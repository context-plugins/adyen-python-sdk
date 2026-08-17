
# Paginated Account Holders Response

## Structure

`PaginatedAccountHoldersResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_holders` | [`List[AccountHolder]`](../../doc/models/account-holder.md) | Required | List of account holders. |
| `has_next` | `bool` | Required | Indicates whether there are more items on the next page. |
| `has_previous` | `bool` | Required | Indicates whether there are more items on the previous page. |

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
from adyen.models.paginated_account_holders_response import PaginatedAccountHoldersResponse
from adyen.models.phone_31 import Phone31
from adyen.models.type_410_enum import Type410Enum

paginated_account_holders_response = PaginatedAccountHoldersResponse(
    account_holders=[
        AccountHolder(
            id=None,
            legal_entity_id='legalEntityId8',
            balance_platform='balancePlatform4',
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
            description='description2',
            metadata={
                'key0': 'metadata9',
                'key1': 'metadata8'
            }
        )
    ],
    has_next=False,
    has_previous=False
)
```

