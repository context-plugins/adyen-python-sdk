
# Store 11

The store that the terminal is assigned to.

## Structure

`Store11`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `address` | [`Address14`](../../doc/models/address-14.md) | Optional | The address of the store. |
| `description` | `str` | Optional | The description of the store. |
| `in_store_terminals` | `List[str]` | Optional | The list of terminals assigned to the store. |
| `merchant_account_code` | `str` | Optional | The code of the merchant account. |
| `status` | `str` | Optional | The status of the store:<br><br>- `PreActive`: the store has been created, but not yet activated.<br><br>- `Active`: the store has been activated. This means you can process payments for this store.<br><br>- `Inactive`: the store is currently not active.<br><br>- `InactiveWithModifications`: the store is currently not active, but payment modifications such as refunds are possible.<br><br>- `Closed`: the store has been closed. |
| `store` | `str` | Required | The code of the store. |

## Example

```python
from adyen.models.address_14 import Address14
from adyen.models.store_11 import Store11

store_11 = Store11(
    store='store2',
    address=Address14(
        city='city6',
        country_code='countryCode8',
        postal_code='postalCode8',
        state_or_province='stateOrProvince4',
        street_address='streetAddress6'
    ),
    description='description2',
    in_store_terminals=[
        'inStoreTerminals3',
        'inStoreTerminals2'
    ],
    merchant_account_code='merchantAccountCode4',
    status='status4'
)
```

