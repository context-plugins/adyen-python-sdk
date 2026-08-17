
# Folio

## Structure

`Folio`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `cash_advances` | `int` | Optional | The folio cash advances, in [minor units](https://docs.adyen.com/development-resources/currency-codes).<br><br>* For example, 2000 means USD 20.00.<br>* Encoding: Numeric<br>* Max value: 10000000000<br>* **additionalData key:** `lodging.folioCashAdvances` |
| `number` | `str` | Optional | The card acceptor's internal invoice or billing ID reference number.<br><br>* Format: Alphanumeric<br>* Must not start with a space<br>* Must not contain any special characters<br>* Must not be all zeros.<br>* **additionalData key:** `lodging.folioNumber` |

## Example

```python
from adyen.models.folio import Folio

folio = Folio(
    cash_advances=122,
    number='number8'
)
```

