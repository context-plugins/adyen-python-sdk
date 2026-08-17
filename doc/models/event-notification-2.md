
# Event Notification 2

Content of the EventNotification message.

## Structure

`EventNotification2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `time_stamp` | `datetime` | Required | Date and time of a transaction for the Sale System, the POI System or the Acquirer. |
| `event_to_notify` | [`EventToNotify1Enum`](../../doc/models/event-to-notify-1-enum.md) | Required | Event the POI notifies to the Sale System.<br>Possible values:<br><br>* **Abort**<br>* **BeginMaintenance**<br>* **CardInserted**<br>* **CardRemoved**<br>* **Completed**<br>* **CustomerLanguage**<br>* **EndMaintenance**<br>* **Initialised**<br>* **KeyPressed**<br>* **OutOfOrder**<br>* **Reject**<br>* **SaleAdmin**<br>* **SaleWakeUp**<br>* **ScanBarcodeResult**<br>* **SecurityAlarm**<br>* **Shutdown**<br>* **StopAssistance**<br>* **UseAnotherCardForPreauth** |
| `event_details` | `str` | Optional | Information about the event the POI notifies to the Sale System.<br>If present, the Sale logs it for further examination.<br><br>**Constraints**: *Pattern*: `^.+$` |
| `rejected_message` | `str` | Optional | Message request rejected by the receiver.<br>Mandatory if EventToNotify is Reject, absent in other cases.<br><br>**Constraints**: *Pattern*: `^.+$` |
| `maintenance_required_flag` | `bool` | Optional | Indicates if the occurred event requires maintenance call or action.<br><br>**Default**: `False` |
| `display_output` | [`List[DisplayOutput]`](../../doc/models/display-output.md) | Optional | Information to display and the way to process the display.<br>To display an event message. |

## Example

```python
import dateutil.parser

from adyen.models.character_height_1_enum import CharacterHeight1Enum
from adyen.models.character_width_1_enum import CharacterWidth1Enum
from adyen.models.device_11_enum import Device11Enum
from adyen.models.display_output import DisplayOutput
from adyen.models.event_notification_2 import EventNotification2
from adyen.models.event_to_notify_1_enum import EventToNotify1Enum
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

event_notification_2 = EventNotification2(
    time_stamp=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    event_to_notify=EventToNotify1Enum.ABORT,
    event_details='EventDetails8',
    rejected_message='RejectedMessage6',
    maintenance_required_flag=False,
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
        ),
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
    ]
)
```

