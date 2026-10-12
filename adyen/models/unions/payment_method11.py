from __future__ import annotations

from typing import Annotated, TypeAlias

from pydantic import Tag

from ...core import WireDiscriminator
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
        Annotated[AchDirectDebit, Tag("ach")]
        | Annotated[AchDirectDebit, Tag("ach_plaid")]
        | Annotated[Affirm, Tag("affirm")]
        | Annotated[Afterpay, Tag("afterpay_default")]
        | Annotated[Afterpay, Tag("afterpaytouch")]
        | Annotated[Afterpay, Tag("afterpaytouch_pos")]
        | Annotated[Afterpay, Tag("clearpay")]
        | Annotated[Afterpay, Tag("afterpay_b2b")]
        | Annotated[Alma, Tag("alma")]
        | Annotated[AmazonPay, Tag("amazonpay")]
        | Annotated[Ancv, Tag("ancv")]
        | Annotated[AndroidPay, Tag("androidpay")]
        | Annotated[ApplePayDetails, Tag("applepay")]
        | Annotated[AuPay, Tag("aupay")]
        | Annotated[BacsDirectDebit, Tag("directdebit_GB")]
        | Annotated[BillDesk, Tag("billdesk_online")]
        | Annotated[BillDesk, Tag("billdesk_wallet")]
        | Annotated[Blik, Tag("blik")]
        | Annotated[CardDetails, Tag("bcmc")]
        | Annotated[CardDetails, Tag("scheme")]
        | Annotated[CardDetails, Tag("networkToken")]
        | Annotated[CardDetails, Tag("altId")]
        | Annotated[CardDetails, Tag("giftcard")]
        | Annotated[CardDetails, Tag("alliancedata")]
        | Annotated[CardDetails, Tag("card")]
        | Annotated[StoredPaymentMethod, Tag("cashapp")]
        | Annotated[Cellulant, Tag("cellulant")]
        | Annotated[Dbarai, Tag("dbarai")]
        | Annotated[DirectDebitAu, Tag("directdebit_AU")]
        | Annotated[Doku, Tag("doku")]
        | Annotated[Doku, Tag("doku_wallet")]
        | Annotated[Doku, Tag("doku_ovo")]
        | Annotated[Doku, Tag("doku_permata_lite_atm")]
        | Annotated[Doku, Tag("doku_permata_atm")]
        | Annotated[Doku, Tag("doku_alfamart")]
        | Annotated[Doku, Tag("doku_indomaret")]
        | Annotated[Doku, Tag("doku_sinarmas_va")]
        | Annotated[Doku, Tag("doku_bca_va")]
        | Annotated[Doku, Tag("doku_mandiri_va")]
        | Annotated[Doku, Tag("doku_cimb_va")]
        | Annotated[Doku, Tag("doku_danamon_va")]
        | Annotated[Doku, Tag("doku_bri_va")]
        | Annotated[Doku, Tag("doku_bni_va")]
        | Annotated[Doku, Tag("doku_bni")]
        | Annotated[Doku, Tag("doku_paymentmethods")]
        | Annotated[Doku, Tag("doku_atm_mandiri_va")]
        | Annotated[Doku, Tag("doku_briepay")]
        | Annotated[Doku, Tag("doku_mandiri_multipayment_lite")]
        | Annotated[Doku, Tag("doku_card")]
        | Annotated[Doku, Tag("doku_atm_mandiri_va_lite")]
        | Annotated[Doku, Tag("doku_bca_klikpay")]
        | Annotated[Doku, Tag("doku_mandiri_multipayment")]
        | Annotated[Doku, Tag("doku_mandiri_clickpay")]
        | Annotated[Dragonpay, Tag("dragonpay_ebanking")]
        | Annotated[Dragonpay, Tag("dragonpay_otc_banking")]
        | Annotated[Dragonpay, Tag("dragonpay_otc_non_banking")]
        | Annotated[Dragonpay, Tag("dragonpay_otc_philippines")]
        | Annotated[EBankingFinland, Tag("ebanking_FI")]
        | Annotated[Voucher, Tag("econtext_seven_eleven")]
        | Annotated[Voucher, Tag("econtext_online")]
        | Annotated[Voucher, Tag("econtext")]
        | Annotated[Voucher, Tag("econtext_stores")]
        | Annotated[Voucher, Tag("econtext_atm")]
        | Annotated[EftDirectDebit, Tag("eft_directdebit_CA")]
        | Annotated[DetailsOfTokensThatAreNotStoredWithAdyen, Tag("externalToken")]
        | Annotated[Fastlane, Tag("fastlane")]
        | Annotated[StoredPaymentMethod2, Tag("onlineBanking_PL")]
        | Annotated[StoredPaymentMethod2, Tag("eps")]
        | Annotated[StoredPaymentMethod2, Tag("onlineBanking_SK")]
        | Annotated[StoredPaymentMethod2, Tag("onlineBanking_CZ")]
        | Annotated[StoredPaymentMethod2, Tag("onlinebanking_IN")]
        | Annotated[GooglePayDetails, Tag("googlepay")]
        | Annotated[IdealDetails, Tag("ideal")]
        | Annotated[Klarna, Tag("klarna")]
        | Annotated[Klarna, Tag("klarnapayments")]
        | Annotated[Klarna, Tag("klarnapayments_account")]
        | Annotated[Klarna, Tag("klarnapayments_b2b")]
        | Annotated[Klarna, Tag("klarna_paynow")]
        | Annotated[Klarna, Tag("klarna_account")]
        | Annotated[Klarna, Tag("klarna_b2b")]
        | Annotated[KlarnaNetwork, Tag("klarna_network")]
        | Annotated[Masterpass, Tag("masterpass")]
        | Annotated[Mbway, Tag("mbway")]
        | Annotated[MobilePay, Tag("mobilepay")]
        | Annotated[Molpay, Tag("molpay_ebanking_fpx_MY")]
        | Annotated[Molpay, Tag("molpay_ebanking_TH")]
        | Annotated[Molpay, Tag("molpay_krungsribank")]
        | Annotated[Molpay, Tag("molpay_krungthaibank")]
        | Annotated[Molpay, Tag("molpay_siamcommercialbank")]
        | Annotated[Molpay, Tag("molpay_bangkokbank")]
        | Annotated[Molpay, Tag("molpay_kbank")]
        | Annotated[OpenInvoice, Tag("openinvoice")]
        | Annotated[OpenInvoice, Tag("afterpay_directdebit")]
        | Annotated[OpenInvoice, Tag("atome_pos")]
        | Annotated[PayByBankAisDirectDebit, Tag("paybybank_AIS_DD")]
        | Annotated[PayByBank, Tag("paybybank")]
        | Annotated[PayPal, Tag("paypal")]
        | Annotated[PayPay, Tag("paypay")]
        | Annotated[PayTo, Tag("payto")]
        | Annotated[PayU, Tag("payu_IN_upi")]
        | Annotated[PayWithGoogleDetails, Tag("paywithgoogle")]
        | Annotated[PaymentDetails, Tag("alipay")]
        | Annotated[PaymentDetails, Tag("multibanco")]
        | Annotated[PaymentDetails, Tag("bankTransfer")]
        | Annotated[PaymentDetails, Tag("bankTransfer_IBAN")]
        | Annotated[PaymentDetails, Tag("paynow")]
        | Annotated[PaymentDetails, Tag("affirm_pos")]
        | Annotated[PaymentDetails, Tag("iris")]
        | Annotated[PaymentDetails, Tag("wero")]
        | Annotated[PaymentDetails, Tag("trustly")]
        | Annotated[PaymentDetails, Tag("trustlyvector")]
        | Annotated[PaymentDetails, Tag("oney")]
        | Annotated[PaymentDetails, Tag("facilypay")]
        | Annotated[PaymentDetails, Tag("facilypay_3x")]
        | Annotated[PaymentDetails, Tag("facilypay_4x")]
        | Annotated[PaymentDetails, Tag("facilypay_6x")]
        | Annotated[PaymentDetails, Tag("facilypay_10x")]
        | Annotated[PaymentDetails, Tag("facilypay_12x")]
        | Annotated[PaymentDetails, Tag("unionpay")]
        | Annotated[PaymentDetails, Tag("kcp_banktransfer")]
        | Annotated[PaymentDetails, Tag("kcp_payco")]
        | Annotated[PaymentDetails, Tag("kcp_creditcard")]
        | Annotated[PaymentDetails, Tag("wechatpaySDK")]
        | Annotated[PaymentDetails, Tag("wechatpayQR")]
        | Annotated[PaymentDetails, Tag("wechatpayWeb")]
        | Annotated[PaymentDetails, Tag("molpay_boost")]
        | Annotated[PaymentDetails, Tag("wallet_IN")]
        | Annotated[PaymentDetails, Tag("payu_IN_cashcard")]
        | Annotated[PaymentDetails, Tag("payu_IN_nb")]
        | Annotated[PaymentDetails, Tag("paytm")]
        | Annotated[PaymentDetails, Tag("molpay_ebanking_VN")]
        | Annotated[PaymentDetails, Tag("molpay_ebanking_MY")]
        | Annotated[PaymentDetails, Tag("molpay_ebanking_direct_MY")]
        | Annotated[PaymentDetails, Tag("swish")]
        | Annotated[PaymentDetails, Tag("bizum")]
        | Annotated[PaymentDetails, Tag("walley")]
        | Annotated[PaymentDetails, Tag("walley_b2b")]
        | Annotated[PaymentDetails, Tag("paypo")]
        | Annotated[PaymentDetails, Tag("scalapay")]
        | Annotated[PaymentDetails, Tag("scalapay_3x")]
        | Annotated[PaymentDetails, Tag("scalapay_4x")]
        | Annotated[PaymentDetails, Tag("molpay_fpx")]
        | Annotated[PaymentDetails, Tag("payme")]
        | Annotated[PaymentDetails, Tag("payme_pos")]
        | Annotated[PaymentDetails, Tag("konbini")]
        | Annotated[PaymentDetails, Tag("directEbanking")]
        | Annotated[PaymentDetails, Tag("boletobancario")]
        | Annotated[PaymentDetails, Tag("cashticket")]
        | Annotated[PaymentDetails, Tag("ikano")]
        | Annotated[PaymentDetails, Tag("karenmillen")]
        | Annotated[PaymentDetails, Tag("oasis")]
        | Annotated[PaymentDetails, Tag("warehouse")]
        | Annotated[PaymentDetails, Tag("primeiropay_boleto")]
        | Annotated[PaymentDetails, Tag("mada")]
        | Annotated[PaymentDetails, Tag("benefit")]
        | Annotated[PaymentDetails, Tag("knet")]
        | Annotated[PaymentDetails, Tag("omannet")]
        | Annotated[PaymentDetails, Tag("kcp_naverpay")]
        | Annotated[PaymentDetails, Tag("fawry")]
        | Annotated[PaymentDetails, Tag("atome")]
        | Annotated[PaymentDetails, Tag("naps")]
        | Annotated[PaymentDetails, Tag("nordea")]
        | Annotated[PaymentDetails, Tag("boletobancario_bradesco")]
        | Annotated[PaymentDetails, Tag("boletobancario_itau")]
        | Annotated[PaymentDetails, Tag("boletobancario_santander")]
        | Annotated[PaymentDetails, Tag("boletobancario_bancodobrasil")]
        | Annotated[PaymentDetails, Tag("boletobancario_hsbc")]
        | Annotated[PaymentDetails, Tag("molpay_maybank2u")]
        | Annotated[PaymentDetails, Tag("molpay_cimb")]
        | Annotated[PaymentDetails, Tag("molpay_rhb")]
        | Annotated[PaymentDetails, Tag("molpay_amb")]
        | Annotated[PaymentDetails, Tag("molpay_hlb")]
        | Annotated[PaymentDetails, Tag("molpay_affin_epg")]
        | Annotated[PaymentDetails, Tag("molpay_bankislam")]
        | Annotated[PaymentDetails, Tag("molpay_publicbank")]
        | Annotated[PaymentDetails, Tag("fpx_agrobank")]
        | Annotated[PaymentDetails, Tag("touchngo")]
        | Annotated[PaymentDetails, Tag("maybank2u_mae")]
        | Annotated[PaymentDetails, Tag("duitnow")]
        | Annotated[PaymentDetails, Tag("promptpay")]
        | Annotated[PaymentDetails, Tag("twint_pos")]
        | Annotated[PaymentDetails, Tag("alipay_hk")]
        | Annotated[PaymentDetails, Tag("alipay_hk_web")]
        | Annotated[PaymentDetails, Tag("alipay_hk_wap")]
        | Annotated[PaymentDetails, Tag("alipay_wap")]
        | Annotated[PaymentDetails, Tag("balanceplatform")]
        | Annotated[StoredPaymentMethod4, Tag("pix")]
        | Annotated[StoredPaymentMethod5, Tag("paybybank_pix")]
        | Annotated[PseLatam, Tag("pse_payulatam")]
        | Annotated[RakutenPay, Tag("rakutenpay")]
        | Annotated[Ratepay, Tag("ratepay")]
        | Annotated[Ratepay, Tag("ratepay_directdebit")]
        | Annotated[Riverty, Tag("riverty_account")]
        | Annotated[Riverty, Tag("riverty")]
        | Annotated[Riverty, Tag("riverty_installments")]
        | Annotated[Riverty, Tag("sepadirectdebit_riverty")]
        | Annotated[SamsungPay, Tag("samsungpay")]
        | Annotated[SepaDirectDebit, Tag("sepadirectdebit")]
        | Annotated[SepaDirectDebit, Tag("sepadirectdebit_amazonpay")]
        | Annotated[StoredPaymentMethod6, Tag("alipay_plus")]
        | Annotated[StoredPaymentMethod6, Tag("alipay_plus_alipay_cn")]
        | Annotated[StoredPaymentMethod6, Tag("alipay_plus_alipay_hk")]
        | Annotated[StoredPaymentMethod6, Tag("alipay_plus_dana")]
        | Annotated[StoredPaymentMethod6, Tag("alipay_plus_gcash")]
        | Annotated[StoredPaymentMethod6, Tag("alipay_plus_kakaopay")]
        | Annotated[StoredPaymentMethod6, Tag("alipay_plus_kplus")]
        | Annotated[StoredPaymentMethod6, Tag("alipay_plus_naverpay")]
        | Annotated[StoredPaymentMethod6, Tag("alipay_plus_rabbitlinepay")]
        | Annotated[StoredPaymentMethod6, Tag("alipay_plus_tosspay")]
        | Annotated[StoredPaymentMethod6, Tag("alipay_plus_touchngo")]
        | Annotated[StoredPaymentMethod6, Tag("alipay_plus_truemoney")]
        | Annotated[StoredPaymentMethod6, Tag("bcmc_mobile")]
        | Annotated[StoredPaymentMethod6, Tag("bcmc_mobile_QR")]
        | Annotated[StoredPaymentMethod6, Tag("bcmc_mobile_app")]
        | Annotated[StoredPaymentMethod6, Tag("momo_wallet")]
        | Annotated[StoredPaymentMethod6, Tag("momo_wallet_app")]
        | Annotated[StoredPaymentMethod6, Tag("paymaya_wallet")]
        | Annotated[StoredPaymentMethod6, Tag("grabpay_SG")]
        | Annotated[StoredPaymentMethod6, Tag("grabpay_MY")]
        | Annotated[StoredPaymentMethod6, Tag("grabpay_TH")]
        | Annotated[StoredPaymentMethod6, Tag("grabpay_ID")]
        | Annotated[StoredPaymentMethod6, Tag("grabpay_VN")]
        | Annotated[StoredPaymentMethod6, Tag("grabpay_PH")]
        | Annotated[StoredPaymentMethod6, Tag("oxxo")]
        | Annotated[StoredPaymentMethod6, Tag("gcash")]
        | Annotated[StoredPaymentMethod6, Tag("dana")]
        | Annotated[StoredPaymentMethod6, Tag("kakaopay")]
        | Annotated[StoredPaymentMethod6, Tag("truemoney")]
        | Annotated[StoredPaymentMethod6, Tag("paysafecard")]
        | Annotated[StoredPaymentMethod6, Tag("gopay_wallet")]
        | Annotated[Twint, Tag("twint")]
        | Annotated[UpiCollect, Tag("upi_collect")]
        | Annotated[UpiIntent, Tag("upi_intent")]
        | Annotated[UpiQr, Tag("upi_qr")]
        | Annotated[Vipps, Tag("vipps")]
        | Annotated[VisaCheckout, Tag("visacheckout")]
        | Annotated[WeChatPay, Tag("wechatpay")]
        | Annotated[WeChatPay, Tag("wechatpay_pos")]
        | Annotated[WeChatPayMiniProgram, Tag("wechatpayMiniProgram")]
        | Annotated[Zip, Tag("zip")]
        | Annotated[Zip, Tag("zip_pos")]
    ),
    WireDiscriminator("type"),
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
