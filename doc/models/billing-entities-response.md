
# Billing Entities Response

*This model accepts additional fields of type Any.*

## Structure

`BillingEntitiesResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `data` | [`List[BillingEntity]`](../../doc/models/billing-entity.md) | Optional | List of legal entities that can be used for the billing of orders. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.address_6 import Address6
from adyen.models.billing_entities_response import BillingEntitiesResponse
from adyen.models.billing_entity import BillingEntity

billing_entities_response = BillingEntitiesResponse(
    data=[
        BillingEntity(
            address=Address6(
                city='city6',
                company_name='companyName8',
                country='country0',
                postal_code='postalCode8',
                state_or_province='stateOrProvince4',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            email='email6',
            id='id0',
            name='name0',
            tax_id='taxId6',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        BillingEntity(
            address=Address6(
                city='city6',
                company_name='companyName8',
                country='country0',
                postal_code='postalCode8',
                state_or_province='stateOrProvince4',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            email='email6',
            id='id0',
            name='name0',
            tax_id='taxId6',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        BillingEntity(
            address=Address6(
                city='city6',
                company_name='companyName8',
                country='country0',
                postal_code='postalCode8',
                state_or_province='stateOrProvince4',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            email='email6',
            id='id0',
            name='name0',
            tax_id='taxId6',
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

