
# Abort Request 2

Content of the Abort Request message.

## Structure

`AbortRequest2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `message_reference` | [`MessageReference4`](../../doc/models/message-reference-4.md) | Required | Identification of a previous POI transaction. |
| `abort_reason` | `str` | Required | Reason of aborting a transaction.<br><br>**Constraints**: *Pattern*: `^.+$` |
| `display_output` | [`DisplayOutput1`](../../doc/models/display-output-1.md) | Optional | Information to display and the way to process the display.<br>To display an abort message to the Customer. |

## Example

```python
from adyen.models.abort_request_2 import AbortRequest2
from adyen.models.character_height_1_enum import CharacterHeight1Enum
from adyen.models.character_width_1_enum import CharacterWidth1Enum
from adyen.models.device_11_enum import Device11Enum
from adyen.models.display_output_1 import DisplayOutput1
from adyen.models.info_qualify_1_enum import InfoQualify1Enum
from adyen.models.menu_entry import MenuEntry
from adyen.models.menu_entry_tag_1_enum import MenuEntryTag1Enum
from adyen.models.message_category_2_enum import MessageCategory2Enum
from adyen.models.message_reference_4 import MessageReference4
from adyen.models.output_barcode_1 import OutputBarcode1
from adyen.models.output_content_1 import OutputContent1
from adyen.models.output_format_1_enum import OutputFormat1Enum
from adyen.models.output_format_2_enum import OutputFormat2Enum
from adyen.models.output_text import OutputText
from adyen.models.predefined_content import PredefinedContent
from adyen.models.predefined_content_1 import PredefinedContent1

abort_request_2 = AbortRequest2(
    message_reference=MessageReference4(
        message_category=MessageCategory2Enum.PAYMENT,
        service_id='ServiceID0',
        device_id='DeviceID2',
        sale_id='SaleID8',
        poiid='POIID2'
    ),
    abort_reason='AbortReason4',
    display_output=DisplayOutput1(
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

