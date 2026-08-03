
# Checkout Network Token Option 2

The object that contains the details for forwarding a network token.

*This model accepts additional fields of type Any.*

## Structure

`CheckoutNetworkTokenOption2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `include_cryptogram` | `bool` | Optional | Set to **true** to enable forwarding network token cryptograms. |
| `use_network_token` | `bool` | Optional | Set to **true** to forward the network token for a card. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.checkout_network_token_option_2 import CheckoutNetworkTokenOption2

checkout_network_token_option_2 = CheckoutNetworkTokenOption2(
    include_cryptogram=False,
    use_network_token=False,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

