
# Sound Content

## Structure

`SoundContent`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `sound_format` | [`SoundFormat1Enum`](../../doc/models/sound-format-1-enum.md) | Required | Possible values:<br><br>* **MessageRef**<br>* **SoundRef**<br>* **Text** |
| `language` | `str` | Optional | **Constraints**: *Pattern*: `^[a-z]{2,2}$` |
| `reference_id` | `str` | Optional | **Constraints**: *Pattern*: `^.+$` |
| `text` | `str` | Optional | **Constraints**: *Pattern*: `^.+$` |

## Example

```python
from adyen.models.sound_content import SoundContent
from adyen.models.sound_format_1_enum import SoundFormat1Enum

sound_content = SoundContent(
    sound_format=SoundFormat1Enum.SOUNDREF,
    language='Language0',
    reference_id='ReferenceID2',
    text='Text2'
)
```

