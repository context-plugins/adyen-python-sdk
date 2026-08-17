
# Checkout Forward Request Options

## Structure

`CheckoutForwardRequestOptions`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_update` | `bool` | Optional | Whether to check for a card account update (true) or not (false) |
| `dry_run` | `bool` | Optional | Set to **true** to receive a copy of the request Adyen is making to the third party in the response. Any sensitive information will be masked in the response you receive. This functionality is only available in the test environment. |
| `network_token` | [`CheckoutNetworkTokenOption2`](../../doc/models/checkout-network-token-option-2.md) | Optional | The object that contains the details for forwarding a network token. |
| `network_tx_reference_paths` | `List[str]` | Optional | Set in tokenize:true case when forwarding PAN. Addresses to the possible location(s) of networkTxReference in the incoming 3rd party response |
| `tokenize` | `bool` | Optional | Set to **true**, the payment details are [tokenized](https://docs.adyen.com/online-payments/tokenization). |
| `transaction_link_id_paths` | `List[str]` | Optional | Set in tokenize:true case when forwarding PAN. Addresses to the possible location(s) of transactionLinkId in the incoming 3rd party response |

## Example

```python
from adyen.models.checkout_forward_request_options import CheckoutForwardRequestOptions
from adyen.models.checkout_network_token_option_2 import CheckoutNetworkTokenOption2

checkout_forward_request_options = CheckoutForwardRequestOptions(
    account_update=False,
    dry_run=False,
    network_token=CheckoutNetworkTokenOption2(
        include_cryptogram=False,
        use_network_token=False
    ),
    network_tx_reference_paths=[
        'networkTxReferencePaths3',
        'networkTxReferencePaths4'
    ],
    tokenize=False
)
```

