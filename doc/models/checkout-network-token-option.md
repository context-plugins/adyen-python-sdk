
# Checkout Network Token Option

## Structure

`CheckoutNetworkTokenOption`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `include_cryptogram` | `bool` | Optional | Set to **true** to enable forwarding network token cryptograms. |
| `use_network_token` | `bool` | Optional | Set to **true** to forward the network token for a card. |

## Example

```python
from adyen.models.checkout_network_token_option import CheckoutNetworkTokenOption

checkout_network_token_option = CheckoutNetworkTokenOption(
    include_cryptogram=False,
    use_network_token=False
)
```

