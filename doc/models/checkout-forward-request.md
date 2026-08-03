
# Checkout Forward Request

*This model accepts additional fields of type Any.*

## Structure

`CheckoutForwardRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount` | [`Amount16`](../../doc/models/amount-16.md) | Optional | - |
| `base_url` | `str` | Required | The base URL of the third party API, where Adyen will send the request to forward the payment details. |
| `merchant_account` | `str` | Required | Your merchant account. |
| `merchant_reference` | `str` | Optional | Merchant defined payment reference. |
| `options` | [`CheckoutForwardRequestOptions`](../../doc/models/checkout-forward-request-options.md) | Optional | - |
| `payment_method` | [`CheckoutForwardRequestCard`](../../doc/models/checkout-forward-request-card.md) | Optional | - |
| `request` | [`CheckoutOutgoingForwardRequest`](../../doc/models/checkout-outgoing-forward-request.md) | Required | - |
| `shopper_reference` | `str` | Required | Your reference to uniquely identify this shopper, for example user ID or account ID. The value is case-sensitive and must be at least three characters.<br><br>> Your reference must not include personally identifiable information (PII) such as name or email address. |
| `stored_payment_method_id` | `str` | Optional | The unique identifier of the token that you want to forward to the third party. This is the `storedPaymentMethodId` you received in the webhook after you created the token. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.amount_16 import Amount16
from adyen.models.checkout_forward_request import CheckoutForwardRequest
from adyen.models.checkout_forward_request_card import CheckoutForwardRequestCard
from adyen.models.checkout_forward_request_options import CheckoutForwardRequestOptions
from adyen.models.checkout_network_token_option import CheckoutNetworkTokenOption
from adyen.models.checkout_outgoing_forward_request import CheckoutOutgoingForwardRequest
from adyen.models.http_method import HttpMethod

checkout_forward_request = CheckoutForwardRequest(
    base_url='baseUrl8',
    merchant_account='merchantAccount2',
    request=CheckoutOutgoingForwardRequest(
        body='body2',
        http_method=HttpMethod.POST,
        credentials='credentials0',
        headers={
            'key0': 'headers9'
        },
        url_suffix='urlSuffix2',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    shopper_reference='shopperReference8',
    amount=Amount16(
        currency='currency2',
        value=110,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    merchant_reference='merchantReference4',
    options=CheckoutForwardRequestOptions(
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
            'networkTxReferencePaths7'
        ],
        tokenize=False,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    payment_method=CheckoutForwardRequestCard(
        cvc='cvc6',
        encrypted_card_number='encryptedCardNumber0',
        encrypted_expiry_month='encryptedExpiryMonth2',
        encrypted_expiry_year='encryptedExpiryYear2',
        encrypted_security_code='encryptedSecurityCode2',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    stored_payment_method_id='storedPaymentMethodId4',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

