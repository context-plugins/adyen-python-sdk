
# Disable Permit Result

*This model accepts additional fields of type Any.*

## Structure

`DisablePermitResult`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `psp_reference` | `str` | Optional | A unique reference associated with the request. This value is globally unique; quote it when communicating with us about this request. |
| `status` | `str` | Optional | Status of the disable request. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.disable_permit_result import DisablePermitResult

disable_permit_result = DisablePermitResult(
    psp_reference='pspReference2',
    status='status2',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

