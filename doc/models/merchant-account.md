
# Merchant Account

*This model accepts additional fields of type Any.*

## Structure

`MerchantAccount`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `in_store_terminals` | `List[str]` | Optional | List of terminals assigned to this merchant account as in-store terminals. This means that the terminal is ready to be boarded, or is already boarded. |
| `inventory_terminals` | `List[str]` | Optional | List of terminals assigned to the inventory of this merchant account. |
| `merchant_account` | `str` | Required | The merchant account. |
| `stores` | [`List[Store1]`](../../doc/models/store-1.md) | Optional | Array of stores under this merchant account. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.address_7 import Address7
from adyen.models.merchant_account import MerchantAccount
from adyen.models.store_1 import Store1

merchant_account = MerchantAccount(
    merchant_account='merchantAccount8',
    in_store_terminals=[
        'inStoreTerminals9',
        'inStoreTerminals0',
        'inStoreTerminals1'
    ],
    inventory_terminals=[
        'inventoryTerminals0',
        'inventoryTerminals1',
        'inventoryTerminals2'
    ],
    stores=[
        Store1(
            store='store8',
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
            description='description8',
            in_store_terminals=[
                'inStoreTerminals3',
                'inStoreTerminals2',
                'inStoreTerminals1'
            ],
            merchant_account_code='merchantAccountCode0',
            status='status0',
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

