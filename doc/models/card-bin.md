
# Card Bin

*This model accepts additional fields of type Any.*

## Structure

`CardBin`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `bin` | `str` | Optional | The first 6 digit of the card number. Enable this field via merchant account settings. |
| `commercial` | `bool` | Optional | If true, it indicates a commercial card. Enable this field via merchant account settings. |
| `funding_source` | `str` | Optional | The card funding source. Valid values are:<br><br>* CHARGE<br>* CREDIT<br>* DEBIT<br>* DEFERRED_DEBIT<br>* PREPAID<br>* PREPAID_RELOADABLE<br>* PREPAID_NONRELOADABLE<br><br>> Enable this field via merchant account settings. |
| `funds_availability` | `str` | Optional | Indicates availability of funds.<br><br>Visa:<br><br>* "I" (fast funds are supported)<br>* "N" (otherwise)<br><br>Mastercard:<br><br>* "I" (product type is Prepaid or Debit, or issuing country is in CEE/HGEM list)<br>* "N" (otherwise)<br><br>> Returned when you verify a card BIN or estimate costs, and only if `payoutEligible` is different from "N" or "U". |
| `issuer_bin` | `str` | Optional | The first 8 digit of the card number. Enable this field via merchant account settings. |
| `issuing_bank` | `str` | Optional | The issuing bank of the card. |
| `issuing_country` | `str` | Optional | The country where the card was issued from. |
| `issuing_currency` | `str` | Optional | The currency of the card. |
| `payment_method` | `str` | Optional | The payment method associated with the card (e.g. visa, mc, or amex). |
| `payout_eligible` | `str` | Optional | Indicates whether a payout is eligible or not for this card.<br><br>Visa:<br><br>* "Y"<br>* "N"<br><br>Mastercard:<br><br>* "Y" (domestic and cross-border)<br>* "D" (only domestic)<br>* "N" (no MoneySend)<br>* "U" (unknown)<br><br>> Returned when you verify a card BIN or estimate costs, and only if `payoutEligible` is different from "N" or "U". |
| `summary` | `str` | Optional | The last four digits of the card number. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.card_bin import CardBin

card_bin = CardBin(
    bin='bin6',
    commercial=False,
    funding_source='fundingSource0',
    funds_availability='fundsAvailability0',
    issuer_bin='issuerBin8',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

