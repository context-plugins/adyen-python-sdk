
# Get Terminals Under Account Response

*This model accepts additional fields of type Any.*

## Structure

`GetTerminalsUnderAccountResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `company_account` | `str` | Required | Your company account. |
| `inventory_terminals` | `List[str]` | Optional | Array that returns a list of all terminals that are in the inventory of the company account. |
| `merchant_accounts` | [`List[MerchantAccount]`](../../doc/models/merchant-account.md) | Optional | Array that returns a list of all merchant accounts belonging to the company account. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.address_7 import Address7
from adyen.models.get_terminals_under_account_response import GetTerminalsUnderAccountResponse
from adyen.models.merchant_account import MerchantAccount
from adyen.models.store_1 import Store1

get_terminals_under_account_response = GetTerminalsUnderAccountResponse(
    company_account='companyAccount2',
    inventory_terminals=[
        'inventoryTerminals2',
        'inventoryTerminals3',
        'inventoryTerminals4'
    ],
    merchant_accounts=[
        MerchantAccount(
            merchant_account='merchantAccount2',
            in_store_terminals=[
                'inStoreTerminals5'
            ],
            inventory_terminals=[
                'inventoryTerminals4',
                'inventoryTerminals5'
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
                ),
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
                ),
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
        ),
        MerchantAccount(
            merchant_account='merchantAccount2',
            in_store_terminals=[
                'inStoreTerminals5'
            ],
            inventory_terminals=[
                'inventoryTerminals4',
                'inventoryTerminals5'
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
                ),
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
                ),
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
        ),
        MerchantAccount(
            merchant_account='merchantAccount2',
            in_store_terminals=[
                'inStoreTerminals5'
            ],
            inventory_terminals=[
                'inventoryTerminals4',
                'inventoryTerminals5'
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
                ),
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
                ),
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
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

