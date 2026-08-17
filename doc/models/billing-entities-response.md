
# Billing Entities Response

## Structure

`BillingEntitiesResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `data` | [`List[BillingEntity]`](../../doc/models/billing-entity.md) | Optional | List of legal entities that can be used for the billing of orders. |

## Example

```python
from adyen.models.address_11 import Address11
from adyen.models.billing_entities_response import BillingEntitiesResponse
from adyen.models.billing_entity import BillingEntity

billing_entities_response = BillingEntitiesResponse(
    data=[
        BillingEntity(
            address=Address11(
                city='city6',
                company_name='companyName8',
                country='country0',
                postal_code='postalCode8',
                state_or_province='stateOrProvince4'
            ),
            email='email6',
            id='id0',
            name='name0',
            tax_id='taxId6'
        ),
        BillingEntity(
            address=Address11(
                city='city6',
                company_name='companyName8',
                country='country0',
                postal_code='postalCode8',
                state_or_province='stateOrProvince4'
            ),
            email='email6',
            id='id0',
            name='name0',
            tax_id='taxId6'
        ),
        BillingEntity(
            address=Address11(
                city='city6',
                company_name='companyName8',
                country='country0',
                postal_code='postalCode8',
                state_or_province='stateOrProvince4'
            ),
            email='email6',
            id='id0',
            name='name0',
            tax_id='taxId6'
        )
    ]
)
```

