
# Store 1

*This model accepts additional fields of type Any.*

## Structure

`Store1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `address` | [`Address7`](../../doc/models/address-7.md) | Optional | - |
| `description` | `str` | Optional | The description of the store. |
| `in_store_terminals` | `List[str]` | Optional | The list of terminals assigned to the store. |
| `merchant_account_code` | `str` | Optional | The code of the merchant account. |
| `status` | `str` | Optional | The status of the store:<br><br>- `PreActive`: the store has been created, but not yet activated.<br><br>- `Active`: the store has been activated. This means you can process payments for this store.<br><br>- `Inactive`: the store is currently not active.<br><br>- `InactiveWithModifications`: the store is currently not active, but payment modifications such as refunds are possible.<br><br>- `Closed`: the store has been closed. |
| `store` | `str` | Required | The code of the store. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.address_7 import Address7
from adyen.models.store_1 import Store1

store_1 = Store1(
    store='store6',
    address=Address7(
        city='city6',
        country_code='countryCode8',
        postal_code='postalCode8',
        state_or_province='stateOrProvince4',
        street_address='streetAddress6',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    description='description6',
    in_store_terminals=[
        'inStoreTerminals9',
        'inStoreTerminals0'
    ],
    merchant_account_code='merchantAccountCode8',
    status='status2',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

