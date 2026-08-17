
# List Stored Payment Methods Response

## Structure

`ListStoredPaymentMethodsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `merchant_account` | `str` | Optional | Your merchant account. |
| `shopper_reference` | `str` | Optional | Your reference to uniquely identify this shopper, for example user ID or account ID. Minimum length: 3 characters.<br><br>> Your reference must not include personally identifiable information (PII), for example name or email address. |
| `stored_payment_methods` | [`List[StoredPaymentMethodResource]`](../../doc/models/stored-payment-method-resource.md) | Optional | List of all stored payment methods. |

## Example

```python
from adyen.models.address_5 import Address5
from adyen.models.list_stored_payment_methods_response import ListStoredPaymentMethodsResponse
from adyen.models.stored_payment_method_resource import StoredPaymentMethodResource

list_stored_payment_methods_response = ListStoredPaymentMethodsResponse(
    merchant_account='merchantAccount4',
    shopper_reference='shopperReference2',
    stored_payment_methods=[
        StoredPaymentMethodResource(
            alias='alias4',
            alias_type='aliasType6',
            billing_address=Address5(
                city='city8',
                country='country6',
                house_number_or_name='houseNumberOrName0',
                postal_code='postalCode6',
                street='street2',
                state_or_province='stateOrProvince0'
            ),
            brand='brand6',
            card_bin='cardBin8'
        ),
        StoredPaymentMethodResource(
            alias='alias4',
            alias_type='aliasType6',
            billing_address=Address5(
                city='city8',
                country='country6',
                house_number_or_name='houseNumberOrName0',
                postal_code='postalCode6',
                street='street2',
                state_or_province='stateOrProvince0'
            ),
            brand='brand6',
            card_bin='cardBin8'
        )
    ]
)
```

