
# Checkout Forward Request

## Structure

`CheckoutForwardRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount` | [`Amount11`](../../doc/models/amount-11.md) | Optional | The amount of the forwarded payment. |
| `base_url` | `str` | Required | The base URL of the third party API, where Adyen will send the request to forward the payment details. |
| `merchant_account` | `str` | Required | Your merchant account. |
| `merchant_reference` | `str` | Optional | Merchant defined payment reference. |
| `options` | [`CheckoutForwardRequestOptions2`](../../doc/models/checkout-forward-request-options-2.md) | Optional | The customizations that can be applied when making a forward request. |
| `payment_method` | [`CheckoutForwardRequestCard2`](../../doc/models/checkout-forward-request-card-2.md) | Optional | The card details. |
| `request` | [`CheckoutOutgoingForwardRequest2`](../../doc/models/checkout-outgoing-forward-request-2.md) | Required | The [details of the request](https://docs.adyen.com/online-payments/tokenization/forward-payment-details#request-to-adyen-card) that you want to forward to the third-party. |
| `shopper_reference` | `str` | Required | Your reference to uniquely identify this shopper, for example user ID or account ID. The value is case-sensitive and must be at least three characters.<br><br>> Your reference must not include personally identifiable information (PII) such as name or email address. |
| `stored_payment_method_id` | `str` | Optional | The unique identifier of the token that you want to forward to the third party. This is the `storedPaymentMethodId` you received in the webhook after you created the token. |

## Example

```python
from adyen.models.amount_11 import Amount11
from adyen.models.checkout_forward_request import CheckoutForwardRequest
from adyen.models.checkout_forward_request_card_2 import CheckoutForwardRequestCard2
from adyen.models.checkout_forward_request_options_2 import CheckoutForwardRequestOptions2
from adyen.models.checkout_network_token_option_2 import CheckoutNetworkTokenOption2
from adyen.models.checkout_outgoing_forward_request_2 import CheckoutOutgoingForwardRequest2
from adyen.models.http_method_enum import HttpMethodEnum

checkout_forward_request = CheckoutForwardRequest(
    base_url='baseUrl8',
    merchant_account='merchantAccount2',
    request=CheckoutOutgoingForwardRequest2(
        body='body2',
        http_method=HttpMethodEnum.POST,
        credentials='credentials0',
        headers={
            'key0': 'headers9'
        },
        url_suffix='urlSuffix2'
    ),
    shopper_reference='shopperReference8',
    amount=Amount11(
        currency='currency2',
        value=110
    ),
    merchant_reference='merchantReference4',
    options=CheckoutForwardRequestOptions2(
        account_update=False,
        dry_run=False,
        network_token=CheckoutNetworkTokenOption2(
            include_cryptogram=False,
            use_network_token=False
        ),
        network_tx_reference_paths=[
            'networkTxReferencePaths7'
        ],
        tokenize=False
    ),
    payment_method=CheckoutForwardRequestCard2(
        cvc='cvc6',
        encrypted_card_number='encryptedCardNumber0',
        encrypted_expiry_month='encryptedExpiryMonth2',
        encrypted_expiry_year='encryptedExpiryYear2',
        encrypted_security_code='encryptedSecurityCode2'
    ),
    stored_payment_method_id='storedPaymentMethodId4'
)
```

