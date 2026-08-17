
# Countries Restriction 1

List of countries and the operation.

Supported operations: **anyMatch**, **noneMatch**.

## Structure

`CountriesRestriction1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `operation` | `str` | Required | Defines how the condition must be evaluated. |
| `value` | `List[str]` | Optional | List of two-character [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. |

## Example

```python
from adyen.models.countries_restriction_1 import CountriesRestriction1

countries_restriction_1 = CountriesRestriction1(
    operation='operation2',
    value=[
        'value6',
        'value7',
        'value8'
    ]
)
```

