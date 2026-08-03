
# Event Notification 2

Content of the EventNotification message.

*This model accepts additional fields of type Any.*

## Structure

`EventNotification2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `time_stamp` | `datetime` | Required | Date and time of a transaction for the Sale System, the POI System or the Acquirer. |
| `event_to_notify` | [`EventToNotify1`](../../doc/models/event-to-notify-1.md) | Required | - |
| `event_details` | `str` | Optional | Information about the event the POI notifies to the Sale System.<br>If present, the Sale logs it for further examination.<br><br>**Constraints**: *Pattern*: `^.+$` |
| `rejected_message` | `str` | Optional | Message request rejected by the receiver.<br>Mandatory if EventToNotify is Reject, absent in other cases.<br><br>**Constraints**: *Pattern*: `^.+$` |
| `maintenance_required_flag` | `bool` | Optional | Indicates if the occurred event requires maintenance call or action.<br><br>**Default**: `False` |
| `display_output` | [`List[DisplayOutput]`](../../doc/models/display-output.md) | Optional | Information to display and the way to process the display.<br>To display an event message. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from adyen.models.character_height_1 import CharacterHeight1
from adyen.models.character_width_1 import CharacterWidth1
from adyen.models.device_11 import Device11
from adyen.models.display_output import DisplayOutput
from adyen.models.event_notification_2 import EventNotification2
from adyen.models.event_to_notify_1 import EventToNotify1
from adyen.models.info_qualify_1 import InfoQualify1
from adyen.models.menu_entry import MenuEntry
from adyen.models.menu_entry_tag_1 import MenuEntryTag1
from adyen.models.output_barcode import OutputBarcode
from adyen.models.output_content_2 import OutputContent2
from adyen.models.output_format_1 import OutputFormat1
from adyen.models.output_format_2 import OutputFormat2
from adyen.models.output_text import OutputText
from adyen.models.predefined_content_2 import PredefinedContent2

event_notification_2 = EventNotification2(
    time_stamp=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    event_to_notify=EventToNotify1.ABORT,
    event_details='EventDetails8',
    rejected_message='RejectedMessage6',
    maintenance_required_flag=False,
    display_output=[
        DisplayOutput(
            device=Device11.CASHIERDISPLAY,
            info_qualify=InfoQualify1.STATUS,
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
            response_required_flag=False,
            minimum_display_time=110,
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
                ),
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
            output_signature='OutputSignature4',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        DisplayOutput(
            device=Device11.CASHIERDISPLAY,
            info_qualify=InfoQualify1.STATUS,
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
            response_required_flag=False,
            minimum_display_time=110,
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
                ),
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
            output_signature='OutputSignature4',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

