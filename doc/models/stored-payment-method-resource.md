
# Stored Payment Method Resource

*This model accepts additional fields of type Any.*

## Structure

`StoredPaymentMethodResource`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `alias` | `str` | Optional | The alias of the credit card number.<br><br>Applies only to recurring contracts storing credit card details |
| `alias_type` | `str` | Optional | The alias type of the credit card number.<br><br>Applies only to recurring contracts storing credit card details. |
| `billing_address` | [`BillingAddress7`](../../doc/models/billing-address-7.md) | Optional | - |
| `brand` | `str` | Optional | The brand of the card. |
| `card_bin` | `str` | Optional | The bank identification number (BIN) of the card. |
| `created_at` | `datetime` | Optional | The date when the recurring details were created. |
| `expiry_month` | `str` | Optional | The month the card expires. |
| `expiry_year` | `str` | Optional | The last two digits of the year the card expires. For example, **22** for the year 2022. |
| `external_response_code` | `str` | Optional | The response code returned by an external system (for example after a provisioning operation). |
| `external_token_reference` | `str` | Optional | The token reference of a linked token in an external system (for example a network token reference). |
| `first_psp_reference` | `str` | Optional | The PSP reference of the first payment that created this recurring detail. |
| `holder_name` | `str` | Optional | The unique payment method code. |
| `iban` | `str` | Optional | The IBAN of the bank account. |
| `id` | `str` | Optional | A unique identifier of this stored payment method. |
| `issuer_name` | `str` | Optional | The name of the issuer of token or card. |
| `last_four` | `str` | Optional | The last four digits of the PAN. |
| `mandate` | [`TokenMandate`](../../doc/models/token-mandate.md) | Optional | - |
| `name` | `str` | Optional | The display name of the stored payment method. |
| `network_tx_reference` | `str` | Optional | Returned in the response if you are not tokenizing with Adyen and are using the Merchant-initiated transactions (MIT) framework from Mastercard or Visa.<br><br>This contains either the Mastercard Trace ID or the Visa Transaction ID. |
| `owner_name` | `str` | Optional | The name of the bank account holder. |
| `shopper_email` | `str` | Optional | The shopper’s email address. |
| `shopper_reference` | `str` | Optional | Your reference to uniquely identify this shopper, for example user ID or account ID. The value is case-sensitive and must be at least three characters.<br><br>> Your reference must not include personally identifiable information (PII) such as name or email address.<br><br>**Constraints**: *Minimum Length*: `3`, *Maximum Length*: `256` |
| `supported_recurring_processing_models` | `List[str]` | Optional | Defines a recurring payment type.<br>Allowed values:<br><br>* `Subscription` – A transaction for a fixed or variable amount, which follows a fixed schedule.<br>* `CardOnFile` – With a card-on-file (CoF) transaction, card details are stored to enable one-click or omnichannel journeys, or simply to streamline the checkout process. Any subscription not following a fixed schedule is also considered a card-on-file transaction.<br>* `UnscheduledCardOnFile` – An unscheduled card-on-file (UCoF) transaction is a transaction that occurs on a non-fixed schedule and/or have variable amounts. For example, automatic top-ups when a cardholder's balance drops below a certain amount. |
| `mtype` | `str` | Optional | The type of payment method. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.billing_address_7 import BillingAddress7
from adyen.models.stored_payment_method_resource import StoredPaymentMethodResource

stored_payment_method_resource = StoredPaymentMethodResource(
    alias='alias6',
    alias_type='aliasType4',
    billing_address=BillingAddress7(
        city='city8',
        country='country6',
        house_number_or_name='houseNumberOrName0',
        postal_code='postalCode6',
        street='street2',
        state_or_province='stateOrProvince0',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    brand='brand8',
    card_bin='cardBin0',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

