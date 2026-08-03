
# Sound Content

*This model accepts additional fields of type Any.*

## Structure

`SoundContent`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `sound_format` | [`SoundFormat1`](../../doc/models/sound-format-1.md) | Required | - |
| `language` | `str` | Optional | **Constraints**: *Pattern*: `^[a-z]{2,2}$` |
| `reference_id` | `str` | Optional | **Constraints**: *Pattern*: `^.+$` |
| `text` | `str` | Optional | **Constraints**: *Pattern*: `^.+$` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.sound_content import SoundContent
from adyen.models.sound_format_1 import SoundFormat1

sound_content = SoundContent(
    sound_format=SoundFormat1.SOUNDREF,
    language='Language0',
    reference_id='ReferenceID2',
    text='Text2',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

