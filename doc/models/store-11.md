
# Store 11

The store that the terminal is assigned to.

*This model accepts additional fields of type Any.*

## Structure

`Store11`

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
from adyen.models.store_11 import Store11

store_11 = Store11(
    store='store2',
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
    description='description2',
    in_store_terminals=[
        'inStoreTerminals3',
        'inStoreTerminals2'
    ],
    merchant_account_code='merchantAccountCode4',
    status='status4',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

