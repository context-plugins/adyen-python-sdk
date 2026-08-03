
# Gratuity

*This model accepts additional fields of type Any.*

## Structure

`Gratuity`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `allow_custom_amount` | `bool` | Optional | Indicates whether one of the predefined tipping options is to let the shopper enter a custom tip. If **true**, only three of the other options defined in `predefinedTipEntries` are shown. |
| `currency` | `str` | Optional | The currency that the tipping settings apply to. |
| `predefined_tip_entries` | `List[str]` | Optional | Tipping options the shopper can choose from if `usePredefinedTipEntries` is **true**. The maximum number of predefined options is four, or three plus the option to enter a custom tip.<br>The options can be a mix of:<br><br>- A percentage of the transaction amount. Example: **5%**<br>- A tip amount in [minor units](https://docs.adyen.com/development-resources/currency-codes). Example: **500** for a EUR 5 tip. |
| `use_predefined_tip_entries` | `bool` | Optional | Indicates whether the terminal shows a prompt to enter a tip (**false**), or predefined tipping options to choose from (**true**). |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.gratuity import Gratuity

gratuity = Gratuity(
    allow_custom_amount=False,
    currency='currency4',
    predefined_tip_entries=[
        'predefinedTipEntries4',
        'predefinedTipEntries5',
        'predefinedTipEntries6'
    ],
    use_predefined_tip_entries=False,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

