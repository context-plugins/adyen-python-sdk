
# Countries Restriction

## Structure

`CountriesRestriction`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `operation` | `str` | Required | Defines how the condition must be evaluated. |
| `value` | `List[str]` | Optional | List of two-character [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. |

## Example

```python
from adyen.models.countries_restriction import CountriesRestriction

countries_restriction = CountriesRestriction(
    operation='operation8',
    value=[
        'value2',
        'value3'
    ]
)
```

