
# Enable Service Request

It conveys the services that will be enabled for the POI Terminal without the request of the Sale System, and a possible invitation for the Customer to start the services.
Content of the Enable Service Request message.

*This model accepts additional fields of type Any.*

## Structure

`EnableServiceRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `transaction_action` | [`TransactionAction1`](../../doc/models/transaction-action-1.md) | Required | - |
| `services_enabled` | [`List[ServicesEnabled]`](../../doc/models/services-enabled.md) | Optional | Services which are enabled before the start-up of a transaction.<br>Mandatory if `TransactionAction` is `StartTransaction`, absent if not.<br>Possible values:<br><br>* **CardAcquisition**<br>* **Loyalty**<br>* **Payment** |
| `display_output` | [`DisplayOutput3`](../../doc/models/display-output-3.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.character_height_1 import CharacterHeight1
from adyen.models.character_width_1 import CharacterWidth1
from adyen.models.device_11 import Device11
from adyen.models.display_output_3 import DisplayOutput3
from adyen.models.enable_service_request import EnableServiceRequest
from adyen.models.info_qualify_1 import InfoQualify1
from adyen.models.menu_entry import MenuEntry
from adyen.models.menu_entry_tag_1 import MenuEntryTag1
from adyen.models.output_barcode import OutputBarcode
from adyen.models.output_content_2 import OutputContent2
from adyen.models.output_format_1 import OutputFormat1
from adyen.models.output_format_2 import OutputFormat2
from adyen.models.output_text import OutputText
from adyen.models.predefined_content_2 import PredefinedContent2
from adyen.models.services_enabled import ServicesEnabled
from adyen.models.transaction_action_1 import TransactionAction1

enable_service_request = EnableServiceRequest(
    transaction_action=TransactionAction1.STARTTRANSACTION,
    services_enabled=[
        ServicesEnabled.LOYALTY,
        ServicesEnabled.CARDACQUISITION
    ],
    display_output=DisplayOutput3(
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
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

