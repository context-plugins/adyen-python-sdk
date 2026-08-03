
# Ideal Auth Link Request

*This model accepts additional fields of type Any.*

## Structure

`IdealAuthLinkRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_holder_id` | `str` | Required | The unique identifier of the account holder.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `150` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.ideal_auth_link_request import IdealAuthLinkRequest

ideal_auth_link_request = IdealAuthLinkRequest(
    account_holder_id='AH00000000000000000000000',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

