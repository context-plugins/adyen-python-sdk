
# Get Stores Under Account Response

## Structure

`GetStoresUnderAccountResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `stores` | [`List[Store1]`](../../doc/models/store-1.md) | Optional | Array that returns a list of all stores for the specified merchant account, or for all merchant accounts under the company account. |

## Example

```python
from adyen.models.address_14 import Address14
from adyen.models.get_stores_under_account_response import GetStoresUnderAccountResponse
from adyen.models.store_1 import Store1

get_stores_under_account_response = GetStoresUnderAccountResponse(
    stores=[
        Store1(
            store='store8',
            address=Address14(
                city='city6',
                country_code='countryCode8',
                postal_code='postalCode8',
                state_or_province='stateOrProvince4',
                street_address='streetAddress6'
            ),
            description='description8',
            in_store_terminals=[
                'inStoreTerminals3',
                'inStoreTerminals2',
                'inStoreTerminals1'
            ],
            merchant_account_code='merchantAccountCode0',
            status='status0'
        ),
        Store1(
            store='store8',
            address=Address14(
                city='city6',
                country_code='countryCode8',
                postal_code='postalCode8',
                state_or_province='stateOrProvince4',
                street_address='streetAddress6'
            ),
            description='description8',
            in_store_terminals=[
                'inStoreTerminals3',
                'inStoreTerminals2',
                'inStoreTerminals1'
            ],
            merchant_account_code='merchantAccountCode0',
            status='status0'
        ),
        Store1(
            store='store8',
            address=Address14(
                city='city6',
                country_code='countryCode8',
                postal_code='postalCode8',
                state_or_province='stateOrProvince4',
                street_address='streetAddress6'
            ),
            description='description8',
            in_store_terminals=[
                'inStoreTerminals3',
                'inStoreTerminals2',
                'inStoreTerminals1'
            ],
            merchant_account_code='merchantAccountCode0',
            status='status0'
        )
    ]
)
```

