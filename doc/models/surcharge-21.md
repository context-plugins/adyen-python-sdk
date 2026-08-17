
# Surcharge 21

Settings for payment [surcharge](https://docs.adyen.com/point-of-sale/surcharge) features.

## Structure

`Surcharge21`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `ask_confirmation` | `bool` | Optional | Show the surcharge details on the terminal, so the shopper can confirm. |
| `configurations` | [`List[Configuration]`](../../doc/models/configuration.md) | Optional | Surcharge fees or percentages for specific cards, funding sources (credit or debit), and currencies. |
| `disclosure_on_present_card` | `bool` | Optional | Show the maximum surcharge rate to the shopper on the present card screen before they tap. |
| `exclude_gratuity_from_surcharge` | `bool` | Optional | Exclude the tip amount from the surcharge calculation. |

## Example

```python
from adyen.models.configuration import Configuration
from adyen.models.currency import Currency
from adyen.models.surcharge_21 import Surcharge21

surcharge_21 = Surcharge21(
    ask_confirmation=False,
    configurations=[
        Configuration(
            brand='brand4',
            currencies=[
                Currency(
                    currency_code='currencyCode6',
                    amount=208,
                    max_amount=98,
                    percentage=191.04
                ),
                Currency(
                    currency_code='currencyCode6',
                    amount=208,
                    max_amount=98,
                    percentage=191.04
                ),
                Currency(
                    currency_code='currencyCode6',
                    amount=208,
                    max_amount=98,
                    percentage=191.04
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
            ]
        ),
        Configuration(
            brand='brand4',
            currencies=[
                Currency(
                    currency_code='currencyCode6',
                    amount=208,
                    max_amount=98,
                    percentage=191.04
                ),
                Currency(
                    currency_code='currencyCode6',
                    amount=208,
                    max_amount=98,
                    percentage=191.04
                ),
                Currency(
                    currency_code='currencyCode6',
                    amount=208,
                    max_amount=98,
                    percentage=191.04
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
            ]
        ),
        Configuration(
            brand='brand4',
            currencies=[
                Currency(
                    currency_code='currencyCode6',
                    amount=208,
                    max_amount=98,
                    percentage=191.04
                ),
                Currency(
                    currency_code='currencyCode6',
                    amount=208,
                    max_amount=98,
                    percentage=191.04
                ),
                Currency(
                    currency_code='currencyCode6',
                    amount=208,
                    max_amount=98,
                    percentage=191.04
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
            ]
        )
    ],
    disclosure_on_present_card=False,
    exclude_gratuity_from_surcharge=False
)
```

