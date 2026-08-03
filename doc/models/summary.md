
# Summary

*This model accepts additional fields of type Any.*

## Structure

`Summary`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `legal_entity_id` | `str` | Required | The unique identifier of the legal entity. |
| `tax_years` | `List[int]` | Required | The tax years for which the legal entity has a tax form. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.summary import Summary

summary = Summary(
    legal_entity_id='legalEntityId2',
    tax_years=[
        111
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

