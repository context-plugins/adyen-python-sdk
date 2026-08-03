
# Configuration

*This model accepts additional fields of type Any.*

## Structure

`Configuration`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `brand` | `str` | Required | Payment method, like **eftpos_australia** or **mc**. See the [possible values](https://docs.adyen.com/development-resources/paymentmethodvariant#management-api). |
| `commercial` | `bool` | Optional | Set to **true** to apply surcharges only to commercial/business cards. |
| `country` | `List[str]` | Optional | The country/region of the card issuer. If used, the surcharge settings only apply to the card issued in that country/region. |
| `currencies` | [`List[Currency]`](../../doc/models/currency.md) | Required | Currency and percentage or amount of the surcharge. |
| `sources` | `List[str]` | Optional | Funding source. Possible values:<br><br>* **Credit**<br>* **Debit** |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.configuration import Configuration
from adyen.models.currency import Currency

configuration = Configuration(
    brand='brand0',
    currencies=[
        Currency(
            currency_code='currencyCode6',
            amount=208,
            max_amount=98,
            percentage=191.04,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    commercial=False,
    country=[
        'country7',
        'country8',
        'country9'
    ],
    sources=[
        'sources8'
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

