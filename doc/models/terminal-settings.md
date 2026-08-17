
# Terminal Settings

## Structure

`TerminalSettings`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `cardholder_receipt` | [`CardholderReceipt1`](../../doc/models/cardholder-receipt-1.md) | Optional | Settings to define the header of the shopper receipt. |
| `connectivity` | [`Connectivity1`](../../doc/models/connectivity-1.md) | Optional | Settings for terminal connectivity features. |
| `dcc` | [`Dcc1`](../../doc/models/dcc-1.md) | Optional | Settings for Dynamic Currency Conversion (DCC). |
| `gratuities` | [`List[Gratuity]`](../../doc/models/gratuity.md) | Optional | Settings for tipping with or without predefined options to choose from. The maximum number of predefined options is four, or three plus the option to enter a custom tip. |
| `hardware` | [`Hardware1`](../../doc/models/hardware-1.md) | Optional | Settings for terminal hardware features. |
| `home_screen` | [`HomeScreenSettings1`](../../doc/models/home-screen-settings-1.md) | Optional | Settings for the home screen. |
| `kiosk_mode` | [`KioskModeSettings1`](../../doc/models/kiosk-mode-settings-1.md) | Optional | Settings for kiosk mode. |
| `localization` | [`Localization1`](../../doc/models/localization-1.md) | Optional | Settings for localization. |
| `moto` | [`Moto1`](../../doc/models/moto-1.md) | Optional | Settings for Mail Order/Telephone Order transactions. |
| `nexo` | [`Nexo1`](../../doc/models/nexo-1.md) | Optional | Settings for a Terminal API integration. |
| `offline_processing` | [`OfflineProcessing1`](../../doc/models/offline-processing-1.md) | Optional | Settings for EMV [offline payment](https://docs.adyen.com/point-of-sale/offline-payments) features. |
| `opi` | [`Opi1`](../../doc/models/opi-1.md) | Optional | Settings for an Oracle Payment Interface (OPI) integration. |
| `passcodes` | [`Passcodes1`](../../doc/models/passcodes-1.md) | Optional | Settings for [passcodes](https://docs.adyen.com/point-of-sale/managing-terminals/menu-access?tab=manage_passcodes_with_an_api_call_2#manage-passcodes) features. |
| `pay_at_table` | [`PayAtTable1`](../../doc/models/pay-at-table-1.md) | Optional | Settings for [Pay-at-table](https://docs.adyen.com/point-of-sale/pay-at-x) features. |
| `payment` | [`Payment11`](../../doc/models/payment-11.md) | Optional | Settings for payment features. |
| `receipt_options` | [`ReceiptOptions1`](../../doc/models/receipt-options-1.md) | Optional | Generic receipt settings. |
| `receipt_printing` | [`ReceiptPrinting1`](../../doc/models/receipt-printing-1.md) | Optional | Transaction outcomes that you want the terminal to print a merchant receipt or a shopper receipt for. |
| `refunds` | [`Refunds1`](../../doc/models/refunds-1.md) | Optional | Settings for refunds. |
| `signature` | [`Signature1`](../../doc/models/signature-1.md) | Optional | Settings to skip signature, sign on display, or sign on receipt. |
| `standalone` | [`Standalone1`](../../doc/models/standalone-1.md) | Optional | Settings for [standalone](https://docs.adyen.com/point-of-sale/standalone/standalone-build/set-up-standalone#set-up-standalone-using-an-api-call) features. |
| `store_and_forward` | [`StoreAndForward1`](../../doc/models/store-and-forward-1.md) | Optional | Settings for store-and-forward offline payments. The `maxAmount`, `maxPayments`, and `supportedCardTypes` parameters must be configured, either in the request or inherited from a higher level in your account structure. |
| `surcharge` | [`Surcharge21`](../../doc/models/surcharge-21.md) | Optional | Settings for payment [surcharge](https://docs.adyen.com/point-of-sale/surcharge) features. |
| `tap_to_pay` | [`TapToPay1`](../../doc/models/tap-to-pay-1.md) | Optional | Settings for Tap to Pay. |
| `terminal_instructions` | [`TerminalInstructions1`](../../doc/models/terminal-instructions-1.md) | Optional | Settings to define the behaviour of the payment terminal. |
| `timeouts` | [`Timeouts2`](../../doc/models/timeouts-2.md) | Optional | Settings for device [time-outs](https://docs.adyen.com/point-of-sale/pos-timeouts#device-time-out). |
| `wifi_profiles` | [`WifiProfiles2`](../../doc/models/wifi-profiles-2.md) | Optional | Remote Wi-Fi profiles for WPA and WPA2 PSK and EAP Wi-Fi networks. |

## Example

```python
from adyen.models.cardholder_receipt_1 import CardholderReceipt1
from adyen.models.connectivity_1 import Connectivity1
from adyen.models.dcc_1 import Dcc1
from adyen.models.event_url_3 import EventUrl3
from adyen.models.gratuity import Gratuity
from adyen.models.hardware_1 import Hardware1
from adyen.models.simcard_status_enum import SimcardStatusEnum
from adyen.models.terminal_settings import TerminalSettings
from adyen.models.url import Url

terminal_settings = TerminalSettings(
    cardholder_receipt=CardholderReceipt1(
        header_for_authorized_receipt='headerForAuthorizedReceipt8'
    ),
    connectivity=Connectivity1(
        simcard_status=SimcardStatusEnum.ACTIVATED,
        terminal_ip_address_url=EventUrl3(
            event_local_urls=[
                Url(
                    encrypted=False,
                    password='password4',
                    url='url4',
                    username='username0'
                )
            ],
            event_public_urls=[
                Url(
                    encrypted=False,
                    password='password8',
                    url='url8',
                    username='username4'
                ),
                Url(
                    encrypted=False,
                    password='password8',
                    url='url8',
                    username='username4'
                )
            ]
        )
    ),
    dcc=Dcc1(
        enable_dcc=False
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
            use_predefined_tip_entries=False
        ),
        Gratuity(
            allow_custom_amount=False,
            currency='currency0',
            predefined_tip_entries=[
                'predefinedTipEntries0',
                'predefinedTipEntries1',
                'predefinedTipEntries2'
            ],
            use_predefined_tip_entries=False
        ),
        Gratuity(
            allow_custom_amount=False,
            currency='currency0',
            predefined_tip_entries=[
                'predefinedTipEntries0',
                'predefinedTipEntries1',
                'predefinedTipEntries2'
            ],
            use_predefined_tip_entries=False
        )
    ],
    hardware=Hardware1(
        display_maximum_back_light=142,
        reset_totals_hour=132,
        restart_hour=110
    )
)
```

