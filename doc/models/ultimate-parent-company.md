
# Ultimate Parent Company

*This model accepts additional fields of type Any.*

## Structure

`UltimateParentCompany`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `address` | [`ViasAddress`](../../doc/models/vias-address.md) | Optional | - |
| `business_details` | [`UltimateParentCompanyBusinessDetails`](../../doc/models/ultimate-parent-company-business-details.md) | Optional | - |
| `ultimate_parent_company_code` | `str` | Optional | Adyen-generated unique alphanumeric identifier (UUID) for the entry, returned in the response when you create an ultimate parent company. Required when updating an existing entry in an `/updateAccountHolder` request. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.ultimate_parent_company import UltimateParentCompany
from adyen.models.ultimate_parent_company_business_details import UltimateParentCompanyBusinessDetails
from adyen.models.vias_address import ViasAddress

ultimate_parent_company = UltimateParentCompany(
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
```

