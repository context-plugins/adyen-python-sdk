
# Response Additional Data Billing Address

*This model accepts additional fields of type Any.*

## Structure

`ResponseAdditionalDataBillingAddress`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `billing_address_city` | `str` | Optional | The billing address city passed in the payment request. |
| `billing_address_country` | `str` | Optional | The billing address country passed in the payment request.<br><br>Example: NL |
| `billing_address_house_number_or_name` | `str` | Optional | The billing address house number or name passed in the payment request. |
| `billing_address_postal_code` | `str` | Optional | The billing address postal code passed in the payment request.<br><br>Example: 1011 DJ |
| `billing_address_state_or_province` | `str` | Optional | The billing address state or province passed in the payment request.<br><br>Example: NH |
| `billing_address_street` | `str` | Optional | The billing address street passed in the payment request. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.response_additional_data_billing_address import ResponseAdditionalDataBillingAddress

response_additional_data_billing_address = ResponseAdditionalDataBillingAddress(
    billing_address_city='billingAddress.city8',
    billing_address_country='billingAddress.country2',
    billing_address_house_number_or_name='billingAddress.houseNumberOrName4',
    billing_address_postal_code='billingAddress.postalCode6',
    billing_address_state_or_province='billingAddress.stateOrProvince4',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

