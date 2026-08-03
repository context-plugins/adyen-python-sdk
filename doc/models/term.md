
# Term

*This model accepts additional fields of type Any.*

## Structure

`Term`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `estimated_days` | `int` | Required | The estimated term for repaying the grant, in days. |
| `maximum_days` | `int` | Optional | The maximum term for repaying the grant, in days. Only applies when `contractType` is **loan**. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.term import Term

term = Term(
    estimated_days=248,
    maximum_days=24,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

