
# Reprocess Android App Response

*This model accepts additional fields of type Any.*

## Structure

`ReprocessAndroidAppResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `message` | `str` | Optional | The result of the reprocess. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.reprocess_android_app_response import ReprocessAndroidAppResponse

reprocess_android_app_response = ReprocessAndroidAppResponse(
    message='Message4',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

