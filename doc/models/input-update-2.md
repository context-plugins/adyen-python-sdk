
# Input Update 2

Content of the Input Update message.

*This model accepts additional fields of type Any.*

## Structure

`InputUpdate2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `message_reference` | [`MessageReference1`](../../doc/models/message-reference-1.md) | Required | - |
| `output_content` | [`OutputContent2`](../../doc/models/output-content-2.md) | Required | - |
| `menu_entry` | [`List[MenuEntry]`](../../doc/models/menu-entry.md) | Optional | - |
| `output_signature` | `str` | Optional | **Constraints**: *Pattern*: `^.+$` |
| `min_length` | `int` | Optional | - |
| `max_length` | `int` | Optional | - |
| `max_decimal_length` | `int` | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.character_height_1 import CharacterHeight1
from adyen.models.character_width_1 import CharacterWidth1
from adyen.models.input_update_2 import InputUpdate2
from adyen.models.menu_entry import MenuEntry
from adyen.models.menu_entry_tag_1 import MenuEntryTag1
from adyen.models.message_category_2 import MessageCategory2
from adyen.models.message_reference_1 import MessageReference1
from adyen.models.output_barcode import OutputBarcode
from adyen.models.output_content_2 import OutputContent2
from adyen.models.output_format_1 import OutputFormat1
from adyen.models.output_format_2 import OutputFormat2
from adyen.models.output_text import OutputText
from adyen.models.predefined_content_2 import PredefinedContent2

input_update_2 = InputUpdate2(
    message_reference=MessageReference1(
        message_category=MessageCategory2.PAYMENT,
        service_id='ServiceID0',
        device_id='DeviceID2',
        sale_id='SaleID8',
        poiid='POIID2',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    output_content=OutputContent2(
        output_format=OutputFormat1.XHTML,
        predefined_content=PredefinedContent2(
            reference_id='ReferenceID0',
            language='Language2',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        output_text=[
            OutputText(
                text='Text6',
                character_set=194,
                start_row=74,
                start_column=220,
                character_width=CharacterWidth1.SINGLEWIDTH,
                character_height=CharacterHeight1.SINGLEHEIGHT,
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            )
        ],
        output_xhtml='OutputXHTML2',
        output_barcode=OutputBarcode(
            barcode_value='BarcodeValue2',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    menu_entry=[
        MenuEntry(
            output_format=OutputFormat2.XHTML,
            menu_entry_tag=MenuEntryTag1.SUBMENU,
            default_selected_flag=False,
            predefined_content=PredefinedContent2(
                reference_id='ReferenceID0',
                language='Language2',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            output_text=[
                OutputText(
                    text='Text6',
                    character_set=194,
                    start_row=74,
                    start_column=220,
                    character_width=CharacterWidth1.SINGLEWIDTH,
                    character_height=CharacterHeight1.SINGLEHEIGHT,
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
                OutputText(
                    text='Text6',
                    character_set=194,
                    start_row=74,
                    start_column=220,
                    character_width=CharacterWidth1.SINGLEWIDTH,
                    character_height=CharacterHeight1.SINGLEHEIGHT,
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                )
            ],
            output_xhtml='OutputXHTML8',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    output_signature='OutputSignature2',
    min_length=132,
    max_length=100,
    max_decimal_length=164,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

