
# Supporting Entity Capability

*This model accepts additional fields of type Any.*

## Structure

`SupportingEntityCapability`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `allowed` | `bool` | Optional, Read-only | Indicates whether the capability is allowed for the supporting entity.<br><br>If a capability is allowed for a supporting entity but not for the parent legal entity, this means the legal entity has other supporting entities that failed verification.<br><br>**You can use the allowed supporting entity** regardless of the verification status of other supporting entities. |
| `id` | `str` | Optional, Read-only | Supporting entity reference |
| `requested` | `bool` | Optional, Read-only | Indicates whether the supporting entity capability is requested. |
| `verification_status` | `str` | Optional, Read-only | The status of the verification checks for the capability of the supporting entity.<br><br>Possible values:<br><br>* **pending**: Adyen is running the verification.<br><br>* **invalid**: The verification failed. Check if the `errors` array contains more information.<br><br>* **valid**: The verification has been successfully completed.<br><br>* **rejected**: Adyen has verified the information, but found reasons to not allow the capability. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.supporting_entity_capability import SupportingEntityCapability

supporting_entity_capability = SupportingEntityCapability(
    allowed=False,
    id='id4',
    requested=False,
    verification_status='verificationStatus6',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

