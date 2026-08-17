
# Enable Service Request 2

Content of the Enable Service Request message.

## Structure

`EnableServiceRequest2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `transaction_action` | [`TransactionAction1Enum`](../../doc/models/transaction-action-1-enum.md) | Required | Action to realise on a transaction. In an `EnableService` request message:<br><br>- Starts a transaction by a swipe-ahead mechanism, with the services which are enabled.<br>- Aborts a swipe-ahead transaction or started by a `CardAcquisition`, and not followed by a service request from the Sale System to complete the transaction.<br>  Possible values:<br><br>* **AbortTransaction**<br>* **StartTransaction** |
| `services_enabled` | [`List[ServicesEnabledEnum]`](../../doc/models/services-enabled-enum.md) | Optional | Services which are enabled before the start-up of a transaction.<br>Mandatory if `TransactionAction` is `StartTransaction`, absent if not.<br>Possible values:<br><br>* **CardAcquisition**<br>* **Loyalty**<br>* **Payment** |
| `display_output` | [`DisplayOutput2`](../../doc/models/display-output-2.md) | Optional | Information to display and the way to process the display. |

## Example

```python
from adyen.models.character_height_1_enum import CharacterHeight1Enum
from adyen.models.character_width_1_enum import CharacterWidth1Enum
from adyen.models.device_11_enum import Device11Enum
from adyen.models.display_output_2 import DisplayOutput2
from adyen.models.enable_service_request_2 import EnableServiceRequest2
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
from adyen.models.services_enabled_enum import ServicesEnabledEnum
from adyen.models.transaction_action_1_enum import TransactionAction1Enum

enable_service_request_2 = EnableServiceRequest2(
    transaction_action=TransactionAction1Enum.STARTTRANSACTION,
    services_enabled=[
        ServicesEnabledEnum.CARDACQUISITION,
        ServicesEnabledEnum.PAYMENT,
        ServicesEnabledEnum.LOYALTY
    ],
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

