
# Terminal Settings

*This model accepts additional fields of type Any.*

## Structure

`TerminalSettings`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `cardholder_receipt` | [`CardholderReceipt`](../../doc/models/cardholder-receipt.md) | Optional | - |
| `connectivity` | [`Connectivity`](../../doc/models/connectivity.md) | Optional | - |
| `dcc` | [`Dcc`](../../doc/models/dcc.md) | Optional | - |
| `gratuities` | [`List[Gratuity]`](../../doc/models/gratuity.md) | Optional | Settings for tipping with or without predefined options to choose from. The maximum number of predefined options is four, or three plus the option to enter a custom tip. |
| `hardware` | [`Hardware`](../../doc/models/hardware.md) | Optional | - |
| `home_screen` | [`HomeScreenSettings`](../../doc/models/home-screen-settings.md) | Optional | - |
| `kiosk_mode` | [`KioskModeSettings`](../../doc/models/kiosk-mode-settings.md) | Optional | - |
| `localization` | [`Localization`](../../doc/models/localization.md) | Optional | - |
| `moto` | [`Moto`](../../doc/models/moto.md) | Optional | - |
| `nexo` | [`Nexo`](../../doc/models/nexo.md) | Optional | - |
| `offline_processing` | [`OfflineProcessing`](../../doc/models/offline-processing.md) | Optional | - |
| `opi` | [`Opi`](../../doc/models/opi.md) | Optional | - |
| `passcodes` | [`Passcodes`](../../doc/models/passcodes.md) | Optional | - |
| `pay_at_table` | [`PayAtTable`](../../doc/models/pay-at-table.md) | Optional | - |
| `payment` | [`Payment1`](../../doc/models/payment-1.md) | Optional | - |
| `receipt_options` | [`ReceiptOptions`](../../doc/models/receipt-options.md) | Optional | - |
| `receipt_printing` | [`ReceiptPrinting`](../../doc/models/receipt-printing.md) | Optional | - |
| `refunds` | [`Refunds`](../../doc/models/refunds.md) | Optional | - |
| `signature` | [`Signature`](../../doc/models/signature.md) | Optional | - |
| `standalone` | [`Standalone`](../../doc/models/standalone.md) | Optional | - |
| `store_and_forward` | [`StoreAndForward`](../../doc/models/store-and-forward.md) | Optional | - |
| `surcharge` | [`Surcharge1`](../../doc/models/surcharge-1.md) | Optional | - |
| `tap_to_pay` | [`TapToPay`](../../doc/models/tap-to-pay.md) | Optional | - |
| `terminal_instructions` | [`TerminalInstructions`](../../doc/models/terminal-instructions.md) | Optional | - |
| `timeouts` | [`Timeouts`](../../doc/models/timeouts.md) | Optional | - |
| `wifi_profiles` | [`WifiProfiles`](../../doc/models/wifi-profiles.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.cardholder_receipt import CardholderReceipt
from adyen.models.connectivity import Connectivity
from adyen.models.dcc import Dcc
from adyen.models.event_url import EventUrl
from adyen.models.gratuity import Gratuity
from adyen.models.hardware import Hardware
from adyen.models.simcard_status import SimcardStatus
from adyen.models.terminal_settings import TerminalSettings
from adyen.models.url import Url

terminal_settings = TerminalSettings(
    cardholder_receipt=CardholderReceipt(
        header_for_authorized_receipt='headerForAuthorizedReceipt8',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    connectivity=Connectivity(
        simcard_status=SimcardStatus.ACTIVATED,
        terminal_ip_address_url=EventUrl(
            event_local_urls=[
                Url(
                    encrypted=False,
                    password='password4',
                    url='url4',
                    username='username0',
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                )
            ],
            event_public_urls=[
                Url(
                    encrypted=False,
                    password='password8',
                    url='url8',
                    username='username4',
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
                Url(
                    encrypted=False,
                    password='password8',
                    url='url8',
                    username='username4',
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                )
            ],
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    dcc=Dcc(
        enable_dcc=False,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    gratuities=[
        Gratuity(
            allow_custom_amount=False,
            currency='currency0',
            predefined_tip_entries=[
                'predefinedTipEntries0',
                'predefinedTipEntries1',
                'predefinedTipEntries2'
            ],
            use_predefined_tip_entries=False,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        Gratuity(
            allow_custom_amount=False,
            currency='currency0',
            predefined_tip_entries=[
                'predefinedTipEntries0',
                'predefinedTipEntries1',
                'predefinedTipEntries2'
            ],
            use_predefined_tip_entries=False,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        Gratuity(
            allow_custom_amount=False,
            currency='currency0',
            predefined_tip_entries=[
                'predefinedTipEntries0',
                'predefinedTipEntries1',
                'predefinedTipEntries2'
            ],
            use_predefined_tip_entries=False,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    hardware=Hardware(
        display_maximum_back_light=142,
        reset_totals_hour=132,
        restart_hour=110,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

