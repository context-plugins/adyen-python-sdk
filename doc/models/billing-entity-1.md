
# Billing Entity 1

The details of the entity that the order is billed to.

## Structure

`BillingEntity1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `address` | [`Address11`](../../doc/models/address-11.md) | Optional | The address details of the billing entity. |
| `email` | `str` | Optional | The email address of the billing entity. |
| `id` | `str` | Optional | The unique identifier of the billing entity, for use as `billingEntityId` when creating an order. |
| `name` | `str` | Optional | The unique name of the billing entity. |
| `tax_id` | `str` | Optional | The tax number of the billing entity. |

## Example

```python
from adyen.models.address_11 import Address11
from adyen.models.billing_entity_1 import BillingEntity1

billing_entity_1 = BillingEntity1(
    address=Address11(
        city='city6',
        company_name='companyName8',
        country='country0',
        postal_code='postalCode8',
        state_or_province='stateOrProvince4'
    ),
    email='email8',
    id='id4',
    name='name4',
    tax_id='taxId0'
)
```

