
# Offline Processing

*This model accepts additional fields of type Any.*

## Structure

`OfflineProcessing`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `chip_floor_limit` | `int` | Optional | The maximum offline transaction amount for chip cards, in the processing currency and specified in [minor units](https://docs.adyen.com/development-resources/currency-codes). |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.offline_processing import OfflineProcessing

offline_processing = OfflineProcessing(
    chip_floor_limit=10,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

