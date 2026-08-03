
# Payment 1

*This model accepts additional fields of type Any.*

## Structure

`Payment1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `contactless_currency` | `str` | Optional | The default currency for contactless payments on the payment terminal, in three-letter [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) currency code format.<br><br>Contact Adyen before you update this setting for the first time. To enable you to change the contactless currency, we first need to check if you meet the compliance requirements.<br><br>**Constraints**: *Minimum Length*: `3`, *Maximum Length*: `3` |
| `hide_minor_units_in_currencies` | `List[str]` | Optional | Hides the minor units for the listed [ISO currency codes](https://en.wikipedia.org/wiki/ISO_4217). |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.payment_1 import Payment1

payment_1 = Payment1(
    contactless_currency='contactlessCurrency2',
    hide_minor_units_in_currencies=[
        'hideMinorUnitsInCurrencies0'
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

