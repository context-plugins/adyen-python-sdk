from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .cardholder_receipt1 import CardholderReceipt1, CardholderReceipt1Dict
from .connectivity1 import Connectivity1, Connectivity1Dict
from .dcc1 import Dcc1, Dcc1Dict
from .gratuity import Gratuity, GratuityDict
from .hardware1 import Hardware1, Hardware1Dict
from .home_screen_settings1 import HomeScreenSettings1, HomeScreenSettings1Dict
from .kiosk_mode_settings1 import KioskModeSettings1, KioskModeSettings1Dict
from .localization1 import Localization1, Localization1Dict
from .moto1 import Moto1, Moto1Dict
from .nexo1 import Nexo1, Nexo1Dict
from .offline_processing1 import OfflineProcessing1, OfflineProcessing1Dict
from .opi1 import Opi1, Opi1Dict
from .passcodes1 import Passcodes1, Passcodes1Dict
from .pay_at_table1 import PayAtTable1, PayAtTable1Dict
from .payment11 import Payment11, Payment11Dict
from .receipt_options1 import ReceiptOptions1, ReceiptOptions1Dict
from .receipt_printing1 import ReceiptPrinting1, ReceiptPrinting1Dict
from .refunds1 import Refunds1, Refunds1Dict
from .signature1 import Signature1, Signature1Dict
from .standalone1 import Standalone1, Standalone1Dict
from .store_and_forward1 import StoreAndForward1, StoreAndForward1Dict
from .surcharge21 import Surcharge21, Surcharge21Dict
from .tap_to_pay1 import TapToPay1, TapToPay1Dict
from .terminal_instructions1 import TerminalInstructions1, TerminalInstructions1Dict
from .timeouts2 import Timeouts2, Timeouts2Dict
from .wifi_profiles2 import WifiProfiles2, WifiProfiles2Dict


class TerminalSettings(SdkBaseModel):
    cardholder_receipt: Optional[CardholderReceipt1] = Field(default=UNSET, alias="cardholderReceipt")
    """Settings to define the header of the shopper receipt."""

    connectivity: Optional[Connectivity1] = UNSET
    """Settings for terminal connectivity features."""

    dcc: Optional[Dcc1] = UNSET
    """Settings for Dynamic Currency Conversion (DCC)."""

    gratuities: OptionalNullable[list[Gratuity]] = UNSET
    """Settings for tipping with or without predefined options to choose from. The maximum number of predefined options
    is four, or three plus the option to enter a custom tip."""

    hardware: Optional[Hardware1] = UNSET
    """Settings for terminal hardware features."""

    home_screen: Optional[HomeScreenSettings1] = Field(default=UNSET, alias="homeScreen")
    """Settings for the home screen."""

    kiosk_mode: Optional[KioskModeSettings1] = Field(default=UNSET, alias="kioskMode")
    """Settings for kiosk mode."""

    localization: Optional[Localization1] = UNSET
    """Settings for localization."""

    moto: Optional[Moto1] = UNSET
    """Settings for Mail Order/Telephone Order transactions."""

    nexo: Optional[Nexo1] = UNSET
    """Settings for a Terminal API integration."""

    offline_processing: Optional[OfflineProcessing1] = Field(default=UNSET, alias="offlineProcessing")
    """Settings for EMV `offline payment <https://docs.adyen.com/point-of-sale/offline-payments>`__ features."""

    opi: Optional[Opi1] = UNSET
    """Settings for an Oracle Payment Interface (OPI) integration."""

    passcodes: Optional[Passcodes1] = UNSET
    """Settings for `passcodes
    <https://docs.adyen.com/point-of-sale/managing-terminals/menu-access?tab=manage_passcodes_with_an_api_call_2#manage-passcodes>`__
    features."""

    pay_at_table: Optional[PayAtTable1] = Field(default=UNSET, alias="payAtTable")
    """Settings for `Pay-at-table <https://docs.adyen.com/point-of-sale/pay-at-x>`__ features."""

    payment: Optional[Payment11] = UNSET
    """Settings for payment features."""

    receipt_options: Optional[ReceiptOptions1] = Field(default=UNSET, alias="receiptOptions")
    """Generic receipt settings."""

    receipt_printing: Optional[ReceiptPrinting1] = Field(default=UNSET, alias="receiptPrinting")
    """Transaction outcomes that you want the terminal to print a merchant receipt or a shopper receipt for."""

    refunds: Optional[Refunds1] = UNSET
    """Settings for refunds."""

    signature: Optional[Signature1] = UNSET
    """Settings to skip signature, sign on display, or sign on receipt."""

    standalone: Optional[Standalone1] = UNSET
    """Settings for `standalone
    <https://docs.adyen.com/point-of-sale/standalone/standalone-build/set-up-standalone#set-up-standalone-using-an-api-call>`__
    features."""

    store_and_forward: Optional[StoreAndForward1] = Field(default=UNSET, alias="storeAndForward")
    """Settings for store-and-forward offline payments. The ``maxAmount``, ``maxPayments``, and ``supportedCardTypes``
    parameters must be configured, either in the request or inherited from a higher level in your account structure."""

    surcharge: Optional[Surcharge21] = UNSET
    """Settings for payment `surcharge <https://docs.adyen.com/point-of-sale/surcharge>`__ features."""

    tap_to_pay: Optional[TapToPay1] = Field(default=UNSET, alias="tapToPay")
    """Settings for Tap to Pay."""

    terminal_instructions: Optional[TerminalInstructions1] = Field(default=UNSET, alias="terminalInstructions")
    """Settings to define the behaviour of the payment terminal."""

    timeouts: Optional[Timeouts2] = UNSET
    """Settings for device `time-outs <https://docs.adyen.com/point-of-sale/pos-timeouts#device-time-out>`__."""

    wifi_profiles: Optional[WifiProfiles2] = Field(default=UNSET, alias="wifiProfiles")
    """Remote Wi-Fi profiles for WPA and WPA2 PSK and EAP Wi-Fi networks."""


class TerminalSettingsDict(TypedDict):
    cardholder_receipt: NotRequired[CardholderReceipt1Dict]
    connectivity: NotRequired[Connectivity1Dict]
    dcc: NotRequired[Dcc1Dict]
    gratuities: NotRequired[list[GratuityDict] | None]
    hardware: NotRequired[Hardware1Dict]
    home_screen: NotRequired[HomeScreenSettings1Dict]
    kiosk_mode: NotRequired[KioskModeSettings1Dict]
    localization: NotRequired[Localization1Dict]
    moto: NotRequired[Moto1Dict]
    nexo: NotRequired[Nexo1Dict]
    offline_processing: NotRequired[OfflineProcessing1Dict]
    opi: NotRequired[Opi1Dict]
    passcodes: NotRequired[Passcodes1Dict]
    pay_at_table: NotRequired[PayAtTable1Dict]
    payment: NotRequired[Payment11Dict]
    receipt_options: NotRequired[ReceiptOptions1Dict]
    receipt_printing: NotRequired[ReceiptPrinting1Dict]
    refunds: NotRequired[Refunds1Dict]
    signature: NotRequired[Signature1Dict]
    standalone: NotRequired[Standalone1Dict]
    store_and_forward: NotRequired[StoreAndForward1Dict]
    surcharge: NotRequired[Surcharge21Dict]
    tap_to_pay: NotRequired[TapToPay1Dict]
    terminal_instructions: NotRequired[TerminalInstructions1Dict]
    timeouts: NotRequired[Timeouts2Dict]
    wifi_profiles: NotRequired[WifiProfiles2Dict]
