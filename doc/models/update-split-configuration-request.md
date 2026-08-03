
# Update Split Configuration Request

*This model accepts additional fields of type Any.*

## Structure

`UpdateSplitConfigurationRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `description` | `str` | Required | Your description for the split configuration.<br><br>**Constraints**: *Maximum Length*: `300` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.update_split_configuration_request import UpdateSplitConfigurationRequest

update_split_configuration_request = UpdateSplitConfigurationRequest(
    description='description8',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

