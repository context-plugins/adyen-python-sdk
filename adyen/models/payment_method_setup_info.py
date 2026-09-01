from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .accel_info1 import AccelInfo1, AccelInfo1Dict
from .affirm_info1 import AffirmInfo1, AffirmInfo1Dict
from .afterpay_touch_info1 import AfterpayTouchInfo1, AfterpayTouchInfo1Dict
from .alipay_plus_info1 import AlipayPlusInfo1, AlipayPlusInfo1Dict
from .amex_info1 import AmexInfo1, AmexInfo1Dict
from .apple_pay_info1 import ApplePayInfo1, ApplePayInfo1Dict
from .bcmc_info1 import BcmcInfo1, BcmcInfo1Dict
from .carnet_info1 import CarnetInfo1, CarnetInfo1Dict
from .cartes_bancaires_info1 import CartesBancairesInfo1, CartesBancairesInfo1Dict
from .clearpay_info1 import ClearpayInfo1, ClearpayInfo1Dict
from .diners_info1 import DinersInfo1, DinersInfo1Dict
from .enums.shopper_interaction1 import ShopperInteraction1OrStr
from .enums.type59 import Type59OrStr
from .generic_pm_with_tdi_info1 import GenericPmWithTdiInfo1, GenericPmWithTdiInfo1Dict
from .generic_pm_with_tdi_info2 import GenericPmWithTdiInfo2, GenericPmWithTdiInfo2Dict
from .generic_pm_with_tdi_info3 import GenericPmWithTdiInfo3, GenericPmWithTdiInfo3Dict
from .generic_pm_with_tdi_info4 import GenericPmWithTdiInfo4, GenericPmWithTdiInfo4Dict
from .generic_pm_with_tdi_info5 import GenericPmWithTdiInfo5, GenericPmWithTdiInfo5Dict
from .generic_pm_with_tdi_info6 import GenericPmWithTdiInfo6, GenericPmWithTdiInfo6Dict
from .generic_pm_with_tdi_info7 import GenericPmWithTdiInfo7, GenericPmWithTdiInfo7Dict
from .generic_pm_with_tdi_info8 import GenericPmWithTdiInfo8, GenericPmWithTdiInfo8Dict
from .generic_pm_with_tdi_info9 import GenericPmWithTdiInfo9, GenericPmWithTdiInfo9Dict
from .generic_pm_with_tdi_info10 import GenericPmWithTdiInfo10, GenericPmWithTdiInfo10Dict
from .generic_pm_with_tdi_info11 import GenericPmWithTdiInfo11, GenericPmWithTdiInfo11Dict
from .givex_info1 import GivexInfo1, GivexInfo1Dict
from .google_pay_info1 import GooglePayInfo1, GooglePayInfo1Dict
from .jcbinfo1 import Jcbinfo1, Jcbinfo1Dict
from .klarna_info1 import KlarnaInfo1, KlarnaInfo1Dict
from .meal_voucher_frinfo1 import MealVoucherFrinfo1, MealVoucherFrinfo1Dict
from .nyce_info1 import NyceInfo1, NyceInfo1Dict
from .pay_by_bank_plaid_info1 import PayByBankPlaidInfo1, PayByBankPlaidInfo1Dict
from .pay_me_info1 import PayMeInfo1, PayMeInfo1Dict
from .pay_pal_info1 import PayPalInfo1, PayPalInfo1Dict
from .pay_to_info1 import PayToInfo1, PayToInfo1Dict
from .pulse_info2 import PulseInfo2, PulseInfo2Dict
from .sepa_direct_debit_info2 import SepaDirectDebitInfo2, SepaDirectDebitInfo2Dict
from .sodexo_info2 import SodexoInfo2, SodexoInfo2Dict
from .sofort_info2 import SofortInfo2, SofortInfo2Dict
from .star_info2 import StarInfo2, StarInfo2Dict
from .svs_info2 import SvsInfo2, SvsInfo2Dict
from .swish_info2 import SwishInfo2, SwishInfo2Dict
from .ticket_info2 import TicketInfo2, TicketInfo2Dict
from .twint_info2 import TwintInfo2, TwintInfo2Dict
from .valuelink_info2 import ValuelinkInfo2, ValuelinkInfo2Dict
from .vipps_info2 import VippsInfo2, VippsInfo2Dict
from .we_chat_pay_info2 import WeChatPayInfo2, WeChatPayInfo2Dict
from .we_chat_pay_pos_info2 import WeChatPayPosInfo2, WeChatPayPosInfo2Dict


class PaymentMethodSetupInfo(SdkBaseModel):
    accel: Optional[AccelInfo1] = UNSET
    """Details to provide if ``type`` is **accel**."""

    affirm: Optional[AffirmInfo1] = UNSET
    """Details to provide if ``type`` is **affirm**."""

    afterpay_touch: Optional[AfterpayTouchInfo1] = Field(default=UNSET, alias="afterpayTouch")
    """Details to provide if ``type`` is **afterpaytouch**."""

    alipay_plus: Optional[AlipayPlusInfo1] = Field(default=UNSET, alias="alipayPlus")
    """Details to provide if ``type`` is **alipay_plus**."""

    amex: Optional[AmexInfo1] = UNSET
    """Details to provide if ``type`` is **amex**. For merchants operating in Australia, New Zealand & Canada, JCB and
    American Express are automatically requested together."""

    apple_pay: Optional[ApplePayInfo1] = Field(default=UNSET, alias="applePay")
    """Details to provide if ``type`` is **applepay**."""

    bcmc: Optional[BcmcInfo1] = UNSET
    """Details to provide if ``type`` is **bcmc** (Bancontact)."""

    business_line_id: Optional[str] = Field(default=UNSET, alias="businessLineId")
    """The unique identifier of the business line. Required if you are a `platform model
    <https://docs.adyen.com/platforms>`__."""

    carnet: Optional[CarnetInfo1] = UNSET
    """Details to provide if ``type`` is **carnet**."""

    cartes_bancaires: Optional[CartesBancairesInfo1] = Field(default=UNSET, alias="cartesBancaires")
    """Details to provide if ``type`` is **cartebancaire**."""

    clearpay: Optional[ClearpayInfo1] = UNSET
    """Details to provide if ``type`` is **clearpay**."""

    countries: Optional[list[str]] = UNSET
    """The list of countries where a payment method is available. By default, all countries supported by the payment
    method."""

    cup: Optional[GenericPmWithTdiInfo1] = UNSET
    """Details to provide if ``type`` is **cup** (China Union Pay)."""

    currencies: Optional[list[str]] = UNSET
    """The list of currencies that a payment method supports. By default, all currencies supported by the payment
    method."""

    custom_routing_flags: Optional[list[str]] = Field(default=UNSET, alias="customRoutingFlags")
    """The list of custom routing flags to route payment to the intended acquirer."""

    diners: Optional[DinersInfo1] = UNSET
    """Details to provide if ``type`` is **diners**. For merchants operating in Japan, Diners payments are processed
    through the JCB network. This means that you must include `JCB-specific fields
    <https://docs.adyen.com/api-explorer/Management/latest/post/merchants/(merchantId>`__/paymentMethodSettings/(paymentMethodId)#request-jcb)
    in this object."""

    discover: Optional[GenericPmWithTdiInfo2] = UNSET
    """Details to provide if ``type`` is **discover**. For merchants operating in Japan, request `Diners
    <https://docs.adyen.com/api-explorer/Management/latest/post/merchants/(merchantId>`__/paymentMethodSettings/(paymentMethodId)#request-diners)
    payment method instead. Discover is automatically requested, together with Diners."""

    eft_directdebit_ca: Optional[GenericPmWithTdiInfo3] = Field(default=UNSET, alias="eft_directdebit_CA")
    """Details to provide if ``type`` is **eft_directdebit_CA** (EFT PAD)."""

    eftpos_australia: Optional[GenericPmWithTdiInfo4] = UNSET
    """Details to provide if ``type`` is **eftpos_australia**."""

    girocard: Optional[GenericPmWithTdiInfo5] = UNSET
    """Details to provide if ``type`` is **girocard**."""

    givex: Optional[GivexInfo1] = UNSET
    """Details to provide if ``type`` is **givex**."""

    google_pay: Optional[GooglePayInfo1] = Field(default=UNSET, alias="googlePay")
    """Details to provide if ``type`` is **googlepay**."""

    ideal: Optional[GenericPmWithTdiInfo6] = UNSET
    """Details to provide if ``type`` is **ideal**."""

    interac_card: Optional[GenericPmWithTdiInfo7] = UNSET
    """Details to provide if ``type`` is **interac_card**."""

    jcb: Optional[Jcbinfo1] = UNSET
    """Details to provide if ``type`` is **jcb**. For merchants operating in Japan, ``midNumber``, ``reuseMidNumber``,
    and ``serviceLevel`` fields are required. For merchants operating outside of Japan, these fields are not required.
    For merchants operating in Australia, New Zealand & Canada, JCB and American Express are automatically requested
    together."""

    klarna: Optional[KlarnaInfo1] = UNSET
    """Details to provide if ``type`` is **klarna** or its variant.

    You can use the following payment method ``type`` values for Klarna:
    * **klarna**: Klarna Pay Later
    * **klarna_account**: Klarna Pay over time
    * **klarna_paynow**: Klarna Pay now
    * **klarna_b2b**: `Billie via Klarna <https://docs.adyen.com/payment-methods/klarna/billie>`__"""

    maestro: Optional[GenericPmWithTdiInfo8] = UNSET
    """Details to provide if ``type`` is **maestro**. In the US, ``maestro`` is not supported; use ``maestro_usa``
    instead."""

    maestro_usa: Optional[GenericPmWithTdiInfo9] = UNSET
    """Details to provide if ``type`` is **maestro_usa**. Only for Maestro USA, otherwise use ``maestro``."""

    mc: Optional[GenericPmWithTdiInfo10] = UNSET
    """Details to provide if ``type`` is **mc**."""

    meal_voucher_fr: Optional[MealVoucherFrinfo1] = Field(default=UNSET, alias="mealVoucher_FR")
    """Details to provide if ``type`` is **mealVoucher_FR**."""

    nyce: Optional[NyceInfo1] = UNSET
    """Details to provide if ``type`` is **nyce**."""

    paybybank_plaid: Optional[PayByBankPlaidInfo1] = UNSET
    """Details to provide if ``type`` is **paybybank_plaid**."""

    payme: Optional[PayMeInfo1] = UNSET
    """Details to provide if ``type`` is **payme**."""

    paypal: Optional[PayPalInfo1] = UNSET
    """Details to provide if ``type`` is **paypal**."""

    payto: Optional[PayToInfo1] = UNSET
    """Details to provide if ``type`` is **payto**."""

    pulse: Optional[PulseInfo2] = UNSET
    """Details to provide if ``type`` is **pulse**."""

    reference: Optional[str] = UNSET
    """Your reference for the payment method. Supported characters a-z, A-Z, 0-9."""

    sepadirectdebit: Optional[SepaDirectDebitInfo2] = UNSET
    """Details to provide if ``type`` is **sepadirectdebit**."""

    shopper_interaction: Optional[ShopperInteraction1OrStr] = Field(default=UNSET, alias="shopperInteraction")
    """The sales channel. Required if:
    - The merchant account does not have a sales channel.
    - ``type`` is **alipay**.

    When you provide this field, it overrides the default sales channel set on the merchant account.

    Possible values: **eCommerce**, **pos**, **contAuth**, and **moto**."""

    sodexo: Optional[SodexoInfo2] = UNSET
    """Details to provide if ``type`` is **sodexo**."""

    sofort: Optional[SofortInfo2] = UNSET
    """Sofort details."""

    star: Optional[StarInfo2] = UNSET
    """Details to provide if ``type`` is **star**."""

    store_ids: Optional[list[str]] = Field(default=UNSET, alias="storeIds")
    """The unique identifier of the store for which to configure the payment method, if any."""

    svs: Optional[SvsInfo2] = UNSET
    """Details to provide if ``type`` is **svs**."""

    swish: Optional[SwishInfo2] = UNSET
    """Details to provide if ``type`` is **swish**.
     - This field is required only if you have a contract with Swish. Swish handles settlement directly with you (not
            through Adyen).
     - If not specified then it's assumed that you are using Adyen's contract with Swish.You don't have a direct
            relationship with Swish."""

    ticket: Optional[TicketInfo2] = UNSET
    """Details to provide if ``type`` is **ticket** (Edenred Brazil)."""

    twint: Optional[TwintInfo2] = UNSET
    """Details to provide if ``type`` is **twint**."""

    type_: Type59OrStr = Field(alias="type")
    """Payment method `variant <https://docs.adyen.com/development-resources/paymentmethodvariant#management-api>`__."""

    valuelink: Optional[ValuelinkInfo2] = UNSET
    """Details to provide if ``type`` is **valuelink**."""

    vipps: Optional[VippsInfo2] = UNSET
    """Details to provide if ``type`` is **vipps**."""

    visa: Optional[GenericPmWithTdiInfo11] = UNSET
    """Details to provide if ``type`` is **visa**."""

    wechatpay: Optional[WeChatPayInfo2] = UNSET
    """Details to provide if ``type`` is **wechatpay**."""

    wechatpay_pos: Optional[WeChatPayPosInfo2] = UNSET
    """Details to provide if ``type`` is **wechatpay_pos**."""


class PaymentMethodSetupInfoDict(TypedDict):
    accel: NotRequired[AccelInfo1 | AccelInfo1Dict]
    affirm: NotRequired[AffirmInfo1 | AffirmInfo1Dict]
    afterpay_touch: NotRequired[AfterpayTouchInfo1 | AfterpayTouchInfo1Dict]
    alipay_plus: NotRequired[AlipayPlusInfo1 | AlipayPlusInfo1Dict]
    amex: NotRequired[AmexInfo1 | AmexInfo1Dict]
    apple_pay: NotRequired[ApplePayInfo1 | ApplePayInfo1Dict]
    bcmc: NotRequired[BcmcInfo1 | BcmcInfo1Dict]
    business_line_id: NotRequired[str]
    carnet: NotRequired[CarnetInfo1 | CarnetInfo1Dict]
    cartes_bancaires: NotRequired[CartesBancairesInfo1 | CartesBancairesInfo1Dict]
    clearpay: NotRequired[ClearpayInfo1 | ClearpayInfo1Dict]
    countries: NotRequired[list[str]]
    cup: NotRequired[GenericPmWithTdiInfo1 | GenericPmWithTdiInfo1Dict]
    currencies: NotRequired[list[str]]
    custom_routing_flags: NotRequired[list[str]]
    diners: NotRequired[DinersInfo1 | DinersInfo1Dict]
    discover: NotRequired[GenericPmWithTdiInfo2 | GenericPmWithTdiInfo2Dict]
    eft_directdebit_ca: NotRequired[GenericPmWithTdiInfo3 | GenericPmWithTdiInfo3Dict]
    eftpos_australia: NotRequired[GenericPmWithTdiInfo4 | GenericPmWithTdiInfo4Dict]
    girocard: NotRequired[GenericPmWithTdiInfo5 | GenericPmWithTdiInfo5Dict]
    givex: NotRequired[GivexInfo1 | GivexInfo1Dict]
    google_pay: NotRequired[GooglePayInfo1 | GooglePayInfo1Dict]
    ideal: NotRequired[GenericPmWithTdiInfo6 | GenericPmWithTdiInfo6Dict]
    interac_card: NotRequired[GenericPmWithTdiInfo7 | GenericPmWithTdiInfo7Dict]
    jcb: NotRequired[Jcbinfo1 | Jcbinfo1Dict]
    klarna: NotRequired[KlarnaInfo1 | KlarnaInfo1Dict]
    maestro: NotRequired[GenericPmWithTdiInfo8 | GenericPmWithTdiInfo8Dict]
    maestro_usa: NotRequired[GenericPmWithTdiInfo9 | GenericPmWithTdiInfo9Dict]
    mc: NotRequired[GenericPmWithTdiInfo10 | GenericPmWithTdiInfo10Dict]
    meal_voucher_fr: NotRequired[MealVoucherFrinfo1 | MealVoucherFrinfo1Dict]
    nyce: NotRequired[NyceInfo1 | NyceInfo1Dict]
    paybybank_plaid: NotRequired[PayByBankPlaidInfo1 | PayByBankPlaidInfo1Dict]
    payme: NotRequired[PayMeInfo1 | PayMeInfo1Dict]
    paypal: NotRequired[PayPalInfo1 | PayPalInfo1Dict]
    payto: NotRequired[PayToInfo1 | PayToInfo1Dict]
    pulse: NotRequired[PulseInfo2 | PulseInfo2Dict]
    reference: NotRequired[str]
    sepadirectdebit: NotRequired[SepaDirectDebitInfo2 | SepaDirectDebitInfo2Dict]
    shopper_interaction: NotRequired[ShopperInteraction1OrStr]
    sodexo: NotRequired[SodexoInfo2 | SodexoInfo2Dict]
    sofort: NotRequired[SofortInfo2 | SofortInfo2Dict]
    star: NotRequired[StarInfo2 | StarInfo2Dict]
    store_ids: NotRequired[list[str]]
    svs: NotRequired[SvsInfo2 | SvsInfo2Dict]
    swish: NotRequired[SwishInfo2 | SwishInfo2Dict]
    ticket: NotRequired[TicketInfo2 | TicketInfo2Dict]
    twint: NotRequired[TwintInfo2 | TwintInfo2Dict]
    type_: Type59OrStr
    valuelink: NotRequired[ValuelinkInfo2 | ValuelinkInfo2Dict]
    vipps: NotRequired[VippsInfo2 | VippsInfo2Dict]
    visa: NotRequired[GenericPmWithTdiInfo11 | GenericPmWithTdiInfo11Dict]
    wechatpay: NotRequired[WeChatPayInfo2 | WeChatPayInfo2Dict]
    wechatpay_pos: NotRequired[WeChatPayPosInfo2 | WeChatPayPosInfo2Dict]
