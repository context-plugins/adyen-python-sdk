
# Input Request 2

Content of the Input Request message.

## Structure

`InputRequest2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `display_output` | [`DisplayOutput2`](../../doc/models/display-output-2.md) | Optional | Information to display and the way to process the display. |
| `input_data` | [`InputData2`](../../doc/models/input-data-2.md) | Required | Information related to an Input request. It conveys the target input logical device, the type of input command, and possible minimum and maximum length of the input. In addition, if the requestor might require to receive an Event Notification if a card is inserted in a card reader, with the `NotifyCardInputFlag`. |

## Example

```python
from adyen.models.character_height_1_enum import CharacterHeight1Enum
from adyen.models.character_width_1_enum import CharacterWidth1Enum
from adyen.models.device_11_enum import Device11Enum
from adyen.models.device_2_enum import Device2Enum
from adyen.models.display_output_2 import DisplayOutput2
from adyen.models.info_qualify_1_enum import InfoQualify1Enum
from adyen.models.info_qualify_2_enum import InfoQualify2Enum
from adyen.models.input_command_1_enum import InputCommand1Enum
from adyen.models.input_data_2 import InputData2
from adyen.models.input_request_2 import InputRequest2
from adyen.models.menu_entry import MenuEntry
from adyen.models.menu_entry_tag_1_enum import MenuEntryTag1Enum
from adyen.models.output_barcode_1 import OutputBarcode1
from adyen.models.output_content_1 import OutputContent1
from adyen.models.output_format_1_enum import OutputFormat1Enum
from adyen.models.output_format_2_enum import OutputFormat2Enum
from adyen.models.output_text import OutputText
from adyen.models.predefined_content import PredefinedContent
from adyen.models.predefined_content_1 import PredefinedContent1

input_request_2 = InputRequest2(
    input_data=InputData2(
        device=Device2Enum.CASHIERDISPLAY,
        info_qualify=InfoQualify2Enum.CUSTOMERASSISTANCE,
        input_command=InputCommand1Enum.GETANYKEY,
        notify_card_input_flag=False,
        max_input_time=154,
        immediate_response_flag=False,
        min_length=242,
        max_length=246,
        wait_user_validation_flag=True,
        from_right_to_left_flag=False,
        mask_characters_flag=False,
        beep_key_flag=False,
        global_correction_flag=False,
        disable_cancel_flag=False,
        disable_correct_flag=False,
        disable_valid_flag=False,
        menu_back_flag=False
    ),
    display_output=DisplayOutput2(
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
        response_required_flag=False,
        minimum_display_time=110,
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
)
```

