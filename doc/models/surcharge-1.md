
# Surcharge 1

*This model accepts additional fields of type Any.*

## Structure

`Surcharge1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `ask_confirmation` | `bool` | Optional | Show the surcharge details on the terminal, so the shopper can confirm. |
| `configurations` | [`List[Configuration]`](../../doc/models/configuration.md) | Optional | Surcharge fees or percentages for specific cards, funding sources (credit or debit), and currencies. |
| `disclosure_on_present_card` | `bool` | Optional | Show the maximum surcharge rate to the shopper on the present card screen before they tap. |
| `exclude_gratuity_from_surcharge` | `bool` | Optional | Exclude the tip amount from the surcharge calculation. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.configuration import Configuration
from adyen.models.currency import Currency
from adyen.models.surcharge_1 import Surcharge1

surcharge_1 = Surcharge1(
    ask_confirmation=False,
    configurations=[
        Configuration(
            brand='brand4',
            currencies=[
                Currency(
                    currency_code='currencyCode6',
                    amount=208,
                    max_amount=98,
                    percentage=191.04,
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
                Currency(
                    currency_code='currencyCode6',
                    amount=208,
                    max_amount=98,
                    percentage=191.04,
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
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
                'country1',
                'country2'
            ],
            sources=[
                'sources8',
                'sources9'
            ],
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        Configuration(
            brand='brand4',
            currencies=[
                Currency(
                    currency_code='currencyCode6',
                    amount=208,
                    max_amount=98,
                    percentage=191.04,
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
                Currency(
                    currency_code='currencyCode6',
                    amount=208,
                    max_amount=98,
                    percentage=191.04,
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
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
                'country1',
                'country2'
            ],
            sources=[
                'sources8',
                'sources9'
            ],
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        Configuration(
            brand='brand4',
            currencies=[
                Currency(
                    currency_code='currencyCode6',
                    amount=208,
                    max_amount=98,
                    percentage=191.04,
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
                Currency(
                    currency_code='currencyCode6',
                    amount=208,
                    max_amount=98,
                    percentage=191.04,
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
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
                'country1',
                'country2'
            ],
            sources=[
                'sources8',
                'sources9'
            ],
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    disclosure_on_present_card=False,
    exclude_gratuity_from_surcharge=False,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

