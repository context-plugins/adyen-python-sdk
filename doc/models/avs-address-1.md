
# Avs Address 1

Contains the billing address of the card holder. The address details need to be AVS-compliant, which means that you need to provide at least street address.

*This model accepts additional fields of type Any.*

## Structure

`AvsAddress1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `street_address` | `str` | Required | The street and house number of the address.<br><br>Example: 1 Infinite Loop, Cupertino. |
| `zip` | `str` | Optional | The zip or post code of the address.<br><br>Example: CA 95014 |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.avs_address_1 import AvsAddress1

avs_address_1 = AvsAddress1(
    street_address='streetAddress4',
    zip='zip8',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

