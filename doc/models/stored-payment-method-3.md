
# Stored Payment Method 3

*This model accepts additional fields of type Any.*

## Structure

`StoredPaymentMethod3`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `bank_account_number` | `str` | Optional | The bank account number (without separators). |
| `bank_location_id` | `str` | Optional | The location id of the bank. The field value is `nil` in most cases. |
| `brand` | `str` | Optional | The brand of the card. |
| `cashtag` | `str` | Optional | The shopper’s Cash App Pay Cashtag. |
| `expiry_month` | `str` | Optional | The two-digit month when the card expires |
| `expiry_year` | `str` | Optional | The last two digits of the year the card expires. For example, **22** for the year 2022. |
| `external_token` | `str` | Optional | The token issued by an external tokenization service representing the shopper's payment method |
| `holder_name` | `str` | Optional | The name of the payment method holder. |
| `iban` | `str` | Optional | The IBAN of the bank account. |
| `id` | `str` | Optional | A unique identifier of this stored payment method. |
| `label` | `str` | Optional | The shopper’s issuer account label |
| `last_four` | `str` | Optional | The last four digits of the PAN. |
| `name` | `str` | Optional | The display name of the stored payment method. |
| `network_tx_reference` | `str` | Optional | Returned in the response if you are not tokenizing with Adyen and are using the Merchant-initiated transactions (MIT) framework from Mastercard or Visa.<br><br>This contains either the Mastercard Trace ID or the Visa Transaction ID. |
| `owner_name` | `str` | Optional | The name of the bank account holder. |
| `shopper_email` | `str` | Optional | The shopper’s email address. |
| `supported_recurring_processing_models` | `List[str]` | Optional | The supported recurring processing models for this stored payment method. |
| `supported_shopper_interactions` | `List[str]` | Optional | The supported shopper interactions for this stored payment method. |
| `mtype` | `str` | Optional | The type of payment method. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.stored_payment_method_3 import StoredPaymentMethod3

stored_payment_method_3 = StoredPaymentMethod3(
    bank_account_number='bankAccountNumber8',
    bank_location_id='bankLocationId2',
    brand='brand2',
    cashtag='cashtag4',
    expiry_month='expiryMonth2',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

