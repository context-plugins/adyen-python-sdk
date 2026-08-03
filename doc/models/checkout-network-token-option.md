
# Checkout Network Token Option

*This model accepts additional fields of type Any.*

## Structure

`CheckoutNetworkTokenOption`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `include_cryptogram` | `bool` | Optional | Set to **true** to enable forwarding network token cryptograms. |
| `use_network_token` | `bool` | Optional | Set to **true** to forward the network token for a card. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.checkout_network_token_option import CheckoutNetworkTokenOption

checkout_network_token_option = CheckoutNetworkTokenOption(
    include_cryptogram=False,
    use_network_token=False,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

