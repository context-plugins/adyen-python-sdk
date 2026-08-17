
# Display Request 2

Content of the Display Request message.

## Structure

`DisplayRequest2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `display_output` | [`List[DisplayOutput]`](../../doc/models/display-output.md) | Required | Information to display and the way to process the display.<br>Complete display content for output devices. At most one DisplayOutput per Device/ InfoQualify pair. |

## Example

```python
from adyen.models.character_height_1_enum import CharacterHeight1Enum
from adyen.models.character_width_1_enum import CharacterWidth1Enum
from adyen.models.device_11_enum import Device11Enum
from adyen.models.display_output import DisplayOutput
from adyen.models.display_request_2 import DisplayRequest2
from adyen.models.info_qualify_1_enum import InfoQualify1Enum
from adyen.models.menu_entry import MenuEntry
from adyen.models.menu_entry_tag_1_enum import MenuEntryTag1Enum
from adyen.models.output_barcode_1 import OutputBarcode1
from adyen.models.output_content_1 import OutputContent1
from adyen.models.output_format_1_enum import OutputFormat1Enum
from adyen.models.output_format_2_enum import OutputFormat2Enum
from adyen.models.output_text import OutputText
from adyen.models.predefined_content import PredefinedContent
from adyen.models.predefined_content_1 import PredefinedContent1

display_request_2 = DisplayRequest2(
    display_output=[
        DisplayOutput(
            device=Device11Enum.CASHIERDISPLAY,
            info_qualify=InfoQualify1Enum.STATUS,
            output_content=OutputContent1(
                output_format=OutputFormat1Enum.XHTML,
                predefined_content=PredefinedContent1(
                    reference_id='ReferenceID0',
                    language='Language2'
                ),
                output_text=[
                    OutputText(
                        text='Text6',
                        character_set=194,
                        start_row=74,
                        start_column=220,
                        character_width=CharacterWidth1Enum.SINGLEWIDTH,
                        character_height=CharacterHeight1Enum.SINGLEHEIGHT
                    )
                ],
                output_xhtml='OutputXHTML2',
                output_barcode=OutputBarcode1(
                    barcode_value='BarcodeValue2'
                )
            ),
            response_required_flag=True,
            minimum_display_time=0,
            menu_entry=[
                MenuEntry(
                    output_format=OutputFormat2Enum.XHTML,
                    menu_entry_tag=MenuEntryTag1Enum.SUBMENU,
                    default_selected_flag=False,
                    predefined_content=PredefinedContent(
                        reference_id='ReferenceID0',
                        language='Language2'
                    ),
                    output_text=[
                        OutputText(
                            text='Text6',
                            character_set=194,
                            start_row=74,
                            start_column=220,
                            character_width=CharacterWidth1Enum.SINGLEWIDTH,
                            character_height=CharacterHeight1Enum.SINGLEHEIGHT
                        ),
                        OutputText(
                            text='Text6',
                            character_set=194,
                            start_row=74,
                            start_column=220,
                            character_width=CharacterWidth1Enum.SINGLEWIDTH,
                            character_height=CharacterHeight1Enum.SINGLEHEIGHT
                        )
                    ],
                    output_xhtml='OutputXHTML8'
                ),
                MenuEntry(
                    output_format=OutputFormat2Enum.XHTML,
                    menu_entry_tag=MenuEntryTag1Enum.SUBMENU,
                    default_selected_flag=False,
                    predefined_content=PredefinedContent(
                        reference_id='ReferenceID0',
                        language='Language2'
                    ),
                    output_text=[
                        OutputText(
                            text='Text6',
                            character_set=194,
                            start_row=74,
                            start_column=220,
                            character_width=CharacterWidth1Enum.SINGLEWIDTH,
                            character_height=CharacterHeight1Enum.SINGLEHEIGHT
                        ),
                        OutputText(
                            text='Text6',
                            character_set=194,
                            start_row=74,
                            start_column=220,
                            character_width=CharacterWidth1Enum.SINGLEWIDTH,
                            character_height=CharacterHeight1Enum.SINGLEHEIGHT
                        )
                    ],
                    output_xhtml='OutputXHTML8'
                )
            ],
            output_signature='OutputSignature4'
        )
    ]
)
```

