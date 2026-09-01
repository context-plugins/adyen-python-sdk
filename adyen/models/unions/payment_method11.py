from __future__ import annotations

from typing import Annotated, TypeAlias

from pydantic import Field

from ..ach_direct_debit import AchDirectDebit, AchDirectDebitDict
from ..affirm import Affirm, AffirmDict
from ..afterpay import Afterpay, AfterpayDict
from ..alma import Alma, AlmaDict
from ..amazon_pay import AmazonPay, AmazonPayDict
from ..ancv import Ancv, AncvDict
from ..android_pay import AndroidPay, AndroidPayDict
from ..apple_pay_details import ApplePayDetails, ApplePayDetailsDict
from ..au_pay import AuPay, AuPayDict
from ..bacs_direct_debit import BacsDirectDebit, BacsDirectDebitDict
from ..bill_desk import BillDesk, BillDeskDict
from ..blik import Blik, BlikDict
from ..card_details import CardDetails, CardDetailsDict
from ..cellulant import Cellulant, CellulantDict
from ..dbarai import Dbarai, DbaraiDict
from ..details_of_tokens_that_are_not_stored_with_adyen import (
    DetailsOfTokensThatAreNotStoredWithAdyen,
    DetailsOfTokensThatAreNotStoredWithAdyenDict,
)
from ..direct_debit_au import DirectDebitAu, DirectDebitAuDict
from ..doku import Doku, DokuDict
from ..dragonpay import Dragonpay, DragonpayDict
from ..e_banking_finland import EBankingFinland, EBankingFinlandDict
from ..eft_direct_debit import EftDirectDebit, EftDirectDebitDict
from ..fastlane import Fastlane, FastlaneDict
from ..google_pay_details import GooglePayDetails, GooglePayDetailsDict
from ..ideal_details import IdealDetails, IdealDetailsDict
from ..klarna import Klarna, KlarnaDict
from ..klarna_network import KlarnaNetwork, KlarnaNetworkDict
from ..masterpass import Masterpass, MasterpassDict
from ..mbway import Mbway, MbwayDict
from ..mobile_pay import MobilePay, MobilePayDict
from ..molpay import Molpay, MolpayDict
from ..open_invoice import OpenInvoice, OpenInvoiceDict
from ..pay_by_bank import PayByBank, PayByBankDict
from ..pay_by_bank_ais_direct_debit import PayByBankAisDirectDebit, PayByBankAisDirectDebitDict
from ..pay_pal import PayPal, PayPalDict
from ..pay_pay import PayPay, PayPayDict
from ..pay_to import PayTo, PayToDict
from ..pay_u import PayU, PayUDict
from ..pay_with_google_details import PayWithGoogleDetails, PayWithGoogleDetailsDict
from ..payment_details import PaymentDetails, PaymentDetailsDict
from ..pse_latam import PseLatam, PseLatamDict
from ..rakuten_pay import RakutenPay, RakutenPayDict
from ..ratepay import Ratepay, RatepayDict
from ..riverty import Riverty, RivertyDict
from ..samsung_pay import SamsungPay, SamsungPayDict
from ..sepa_direct_debit import SepaDirectDebit, SepaDirectDebitDict
from ..stored_payment_method import StoredPaymentMethod, StoredPaymentMethodDict
from ..stored_payment_method2 import StoredPaymentMethod2, StoredPaymentMethod2Dict
from ..stored_payment_method4 import StoredPaymentMethod4, StoredPaymentMethod4Dict
from ..stored_payment_method5 import StoredPaymentMethod5, StoredPaymentMethod5Dict
from ..stored_payment_method6 import StoredPaymentMethod6, StoredPaymentMethod6Dict
from ..twint import Twint, TwintDict
from ..upi_collect import UpiCollect, UpiCollectDict
from ..upi_intent import UpiIntent, UpiIntentDict
from ..upi_qr import UpiQr, UpiQrDict
from ..vipps import Vipps, VippsDict
from ..visa_checkout import VisaCheckout, VisaCheckoutDict
from ..voucher import Voucher, VoucherDict
from ..we_chat_pay import WeChatPay, WeChatPayDict
from ..we_chat_pay_mini_program import WeChatPayMiniProgram, WeChatPayMiniProgramDict
from ..zip import Zip, ZipDict

PaymentMethod11: TypeAlias = Annotated[
    (
        AchDirectDebit
        | Affirm
        | Afterpay
        | Alma
        | AmazonPay
        | Ancv
        | AndroidPay
        | ApplePayDetails
        | AuPay
        | BacsDirectDebit
        | BillDesk
        | Blik
        | CardDetails
        | StoredPaymentMethod
        | Cellulant
        | Dbarai
        | DirectDebitAu
        | Doku
        | Dragonpay
        | EBankingFinland
        | Voucher
        | EftDirectDebit
        | DetailsOfTokensThatAreNotStoredWithAdyen
        | Fastlane
        | StoredPaymentMethod2
        | GooglePayDetails
        | IdealDetails
        | Klarna
        | KlarnaNetwork
        | Masterpass
        | Mbway
        | MobilePay
        | Molpay
        | OpenInvoice
        | PayByBankAisDirectDebit
        | PayByBank
        | PayPal
        | PayPay
        | PayTo
        | PayU
        | PayWithGoogleDetails
        | PaymentDetails
        | StoredPaymentMethod4
        | StoredPaymentMethod5
        | PseLatam
        | RakutenPay
        | Ratepay
        | Riverty
        | SamsungPay
        | SepaDirectDebit
        | StoredPaymentMethod6
        | Twint
        | UpiCollect
        | UpiIntent
        | UpiQr
        | Vipps
        | VisaCheckout
        | WeChatPay
        | WeChatPayMiniProgram
        | Zip
    ),
    Field(discriminator="type_"),
]
"""The type and required details of a payment method to use."""

PaymentMethod11Dict: TypeAlias = (
    AchDirectDebitDict
    | AffirmDict
    | AfterpayDict
    | AlmaDict
    | AmazonPayDict
    | AncvDict
    | AndroidPayDict
    | ApplePayDetailsDict
    | AuPayDict
    | BacsDirectDebitDict
    | BillDeskDict
    | BlikDict
    | CardDetailsDict
    | StoredPaymentMethodDict
    | CellulantDict
    | DbaraiDict
    | DirectDebitAuDict
    | DokuDict
    | DragonpayDict
    | EBankingFinlandDict
    | VoucherDict
    | EftDirectDebitDict
    | DetailsOfTokensThatAreNotStoredWithAdyenDict
    | FastlaneDict
    | StoredPaymentMethod2Dict
    | GooglePayDetailsDict
    | IdealDetailsDict
    | KlarnaDict
    | KlarnaNetworkDict
    | MasterpassDict
    | MbwayDict
    | MobilePayDict
    | MolpayDict
    | OpenInvoiceDict
    | PayByBankAisDirectDebitDict
    | PayByBankDict
    | PayPalDict
    | PayPayDict
    | PayToDict
    | PayUDict
    | PayWithGoogleDetailsDict
    | PaymentDetailsDict
    | StoredPaymentMethod4Dict
    | StoredPaymentMethod5Dict
    | PseLatamDict
    | RakutenPayDict
    | RatepayDict
    | RivertyDict
    | SamsungPayDict
    | SepaDirectDebitDict
    | StoredPaymentMethod6Dict
    | TwintDict
    | UpiCollectDict
    | UpiIntentDict
    | UpiQrDict
    | VippsDict
    | VisaCheckoutDict
    | WeChatPayDict
    | WeChatPayMiniProgramDict
    | ZipDict
)
