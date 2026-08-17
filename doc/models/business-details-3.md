
# Business Details 3

Details about the business or nonprofit account holder.
Required when creating an account holder with `legalEntity` **Business** or **NonProfit**.

## Structure

`BusinessDetails3`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `doing_business_as` | `str` | Optional | The registered name of the company (if it differs from the legal name of the company). |
| `legal_business_name` | `str` | Optional | The legal name of the company. |
| `listed_ultimate_parent_company` | [`List[UltimateParentCompany]`](../../doc/models/ultimate-parent-company.md) | Optional | Information about the parent public company. Required if the account holder is 100% owned by a publicly listed company. |
| `registration_number` | `str` | Optional | The registration number of the company. |
| `shareholders` | [`List[ShareholderContact]`](../../doc/models/shareholder-contact.md) | Optional | Array containing information about individuals associated with the account holder either through ownership or control. For details about how you can identify them, refer to [our verification guide](https://docs.adyen.com/classic-platforms/verification-process#identify-ubos). |
| `signatories` | [`List[SignatoryContact]`](../../doc/models/signatory-contact.md) | Optional | Signatories associated with the company.<br>Each array entry should represent one signatory. |
| `stock_exchange` | `str` | Optional | Market Identifier Code (MIC). |
| `stock_number` | `str` | Optional | International Securities Identification Number (ISIN). |
| `stock_ticker` | `str` | Optional | Stock Ticker symbol. |
| `tax_id` | `str` | Optional | The tax ID of the company. |

## Example

```python
from adyen.models.business_details_3 import BusinessDetails3
from adyen.models.gender_enum import GenderEnum
from adyen.models.shareholder_contact import ShareholderContact
from adyen.models.ultimate_parent_company import UltimateParentCompany
from adyen.models.ultimate_parent_company_business_details_2 import UltimateParentCompanyBusinessDetails2
from adyen.models.vias_address_1 import ViasAddress1
from adyen.models.vias_address_2 import ViasAddress2
from adyen.models.vias_name_1 import ViasName1

business_details_3 = BusinessDetails3(
    doing_business_as='doingBusinessAs2',
    legal_business_name='legalBusinessName4',
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
        )
    ],
    registration_number='registrationNumber8',
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
        )
    ]
)
```

