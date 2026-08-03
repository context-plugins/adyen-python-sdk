
# Recurring Detail

*This model accepts additional fields of type Any.*

## Structure

`RecurringDetail`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `additional_data` | `Dict[str, str]` | Optional | This field contains additional data, which may be returned in a particular response.<br><br>The additionalData object consists of entries, each of which includes the key and value. |
| `alias` | `str` | Optional | The alias of the credit card number.<br><br>Applies only to recurring contracts storing credit card details |
| `alias_type` | `str` | Optional | The alias type of the credit card number.<br><br>Applies only to recurring contracts storing credit card details. |
| `bank` | [`Bank`](../../doc/models/bank.md) | Optional | - |
| `billing_address` | [`BillingAddress7`](../../doc/models/billing-address-7.md) | Optional | - |
| `card` | [`Card6`](../../doc/models/card-6.md) | Optional | - |
| `contract_types` | `List[str]` | Optional | Types of recurring contracts. |
| `creation_date` | `datetime` | Optional | The date when the recurring details were created. |
| `first_psp_reference` | `str` | Optional | The `pspReference` of the first recurring payment that created the recurring detail. |
| `name` | `str` | Optional | An optional descriptive name for this recurring detail. |
| `network_tx_reference` | `str` | Optional | Returned in the response if you are not tokenizing with Adyen and are using the Merchant-initiated transactions (MIT) framework from Mastercard or Visa.<br><br>This contains either the Mastercard Trace ID or the Visa Transaction ID. |
| `payment_method_variant` | `str` | Optional | The  type or sub-brand of a payment method used, e.g. Visa Debit, Visa Corporate, etc. For more information, refer to [PaymentMethodVariant](https://docs.adyen.com/development-resources/paymentmethodvariant). |
| `recurring_detail_reference` | `str` | Required | The reference that uniquely identifies the recurring detail. |
| `shopper_name` | [`ShopperName`](../../doc/models/shopper-name.md) | Optional | - |
| `social_security_number` | `str` | Optional | A shopper's social security number (only in countries where it is legal to collect). |
| `token_details` | [`TokenDetails`](../../doc/models/token-details.md) | Optional | - |
| `transaction_link_id` | `str` | Optional | The unique identifier for the transaction link, used for Mastercard recurring transactions. |
| `variant` | `str` | Required | The payment method, such as “mc", "visa", "ideal", "paypal". |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.bank import Bank
from adyen.models.billing_address_7 import BillingAddress7
from adyen.models.recurring_detail import RecurringDetail

recurring_detail = RecurringDetail(
    recurring_detail_reference='recurringDetailReference0',
    variant='variant4',
    additional_data={
        'key0': 'additionalData0',
        'key1': 'additionalData1',
        'key2': 'additionalData2'
    },
    alias='alias2',
    alias_type='aliasType8',
    bank=Bank(
        bank_account_number='bankAccountNumber8',
        bank_city='bankCity0',
        bank_location_id='bankLocationId2',
        bank_name='bankName4',
        bic='bic0',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
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
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

