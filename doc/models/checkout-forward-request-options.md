
# Checkout Forward Request Options

*This model accepts additional fields of type Any.*

## Structure

`CheckoutForwardRequestOptions`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_update` | `bool` | Optional | Whether to check for a card account update (true) or not (false) |
| `dry_run` | `bool` | Optional | Set to **true** to receive a copy of the request Adyen is making to the third party in the response. Any sensitive information will be masked in the response you receive. This functionality is only available in the test environment. |
| `network_token` | [`CheckoutNetworkTokenOption`](../../doc/models/checkout-network-token-option.md) | Optional | - |
| `network_tx_reference_paths` | `List[str]` | Optional | Set in tokenize:true case when forwarding PAN. Addresses to the possible location(s) of networkTxReference in the incoming 3rd party response |
| `tokenize` | `bool` | Optional | Set to **true**, the payment details are [tokenized](https://docs.adyen.com/online-payments/tokenization). |
| `transaction_link_id_paths` | `List[str]` | Optional | Set in tokenize:true case when forwarding PAN. Addresses to the possible location(s) of transactionLinkId in the incoming 3rd party response |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.checkout_forward_request_options import CheckoutForwardRequestOptions
from adyen.models.checkout_network_token_option import CheckoutNetworkTokenOption

checkout_forward_request_options = CheckoutForwardRequestOptions(
    account_update=False,
    dry_run=False,
    network_token=CheckoutNetworkTokenOption(
        include_cryptogram=False,
        use_network_token=False,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    network_tx_reference_paths=[
        'networkTxReferencePaths3',
        'networkTxReferencePaths4'
    ],
    tokenize=False,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

