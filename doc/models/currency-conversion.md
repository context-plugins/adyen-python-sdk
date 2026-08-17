
# Currency Conversion

Information related to a currency conversion.
A currency conversion occurred in the payment, and the merchant needs to know information related to this conversion (e.g. to print on the sale receipt).

## Structure

`CurrencyConversion`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `customer_approved_flag` | `bool` | Optional | Notify if the customer has approved something. Indicates if the customer has accepted a currency conversion.<br><br>**Default**: `True` |
| `converted_amount` | [`ConvertedAmount1`](../../doc/models/converted-amount-1.md) | Required | Amount after a currency conversion. |
| `rate` | `float` | Optional | Rate of currency conversion. |
| `markup` | `float` | Optional | Markup of a currency conversion amount as a percentage. |
| `commission` | `float` | Optional | Commission for a currency conversion.<br><br>**Constraints**: `>= 0`, `<= 99999999.999999` |
| `declaration` | `str` | Optional | Declaration to present to the customer or the cashier for validation.<br>If a declaration has to be presented to the customer.<br><br>**Constraints**: *Pattern*: `^.+$` |

## Example

```python
from adyen.models.converted_amount_1 import ConvertedAmount1
from adyen.models.currency_conversion import CurrencyConversion

currency_conversion = CurrencyConversion(
    converted_amount=ConvertedAmount1(
        amount_value=81.82,
        currency='Currency0'
    ),
    customer_approved_flag=True,
    rate=3.48,
    markup=24.14,
    commission=18.5,
    declaration='Declaration2'
)
```

