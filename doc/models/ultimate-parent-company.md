
# Ultimate Parent Company

## Structure

`UltimateParentCompany`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `address` | [`ViasAddress1`](../../doc/models/vias-address-1.md) | Optional | Address of the ultimate parent company. |
| `business_details` | [`UltimateParentCompanyBusinessDetails2`](../../doc/models/ultimate-parent-company-business-details-2.md) | Optional | Details about the ultimate parent company's business. |
| `ultimate_parent_company_code` | `str` | Optional | Adyen-generated unique alphanumeric identifier (UUID) for the entry, returned in the response when you create an ultimate parent company. Required when updating an existing entry in an `/updateAccountHolder` request. |

## Example

```python
from adyen.models.ultimate_parent_company import UltimateParentCompany
from adyen.models.ultimate_parent_company_business_details_2 import UltimateParentCompanyBusinessDetails2
from adyen.models.vias_address_1 import ViasAddress1

ultimate_parent_company = UltimateParentCompany(
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
```

