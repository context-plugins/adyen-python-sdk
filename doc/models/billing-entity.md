
# Billing Entity

*This model accepts additional fields of type Any.*

## Structure

`BillingEntity`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `address` | [`Address6`](../../doc/models/address-6.md) | Optional | - |
| `email` | `str` | Optional | The email address of the billing entity. |
| `id` | `str` | Optional | The unique identifier of the billing entity, for use as `billingEntityId` when creating an order. |
| `name` | `str` | Optional | The unique name of the billing entity. |
| `tax_id` | `str` | Optional | The tax number of the billing entity. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.address_6 import Address6
from adyen.models.billing_entity import BillingEntity

billing_entity = BillingEntity(
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
    email='email2',
    id='id4',
    name='name4',
    tax_id='taxId0',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

