from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .accel_response_info1 import AccelResponseInfo1, AccelResponseInfo1Dict
from .affirm_response_info1 import AffirmResponseInfo1, AffirmResponseInfo1Dict
from .afterpay_touch_response_info1 import AfterpayTouchResponseInfo1, AfterpayTouchResponseInfo1Dict
from .alipay_plus_response_info1 import AlipayPlusResponseInfo1, AlipayPlusResponseInfo1Dict
from .amex_response_info1 import AmexResponseInfo1, AmexResponseInfo1Dict
from .apple_pay_response_info1 import ApplePayResponseInfo1, ApplePayResponseInfo1Dict
from .associated_payment_method import AssociatedPaymentMethod, AssociatedPaymentMethodDict
from .bcmc_response_info1 import BcmcResponseInfo1, BcmcResponseInfo1Dict
from .carnet_response_info1 import CarnetResponseInfo1, CarnetResponseInfo1Dict
from .cartes_bancaires_response_info1 import CartesBancairesResponseInfo1, CartesBancairesResponseInfo1Dict
from .clearpay_response_info1 import ClearpayResponseInfo1, ClearpayResponseInfo1Dict
from .cup_response_info1 import CupResponseInfo1, CupResponseInfo1Dict
from .diners_response_info1 import DinersResponseInfo1, DinersResponseInfo1Dict
from .discover_response_info1 import DiscoverResponseInfo1, DiscoverResponseInfo1Dict
from .eft_pos_australia_response_info1 import EftPosAustraliaResponseInfo1, EftPosAustraliaResponseInfo1Dict
from .eftdirect_debit_caresponse_info1 import EftdirectDebitCaresponseInfo1, EftdirectDebitCaresponseInfo1Dict
from .enums.verification_status import VerificationStatusOrStr
from .girocard_response_info1 import GirocardResponseInfo1, GirocardResponseInfo1Dict
from .givex_response_info1 import GivexResponseInfo1, GivexResponseInfo1Dict
from .google_pay_response_info1 import GooglePayResponseInfo1, GooglePayResponseInfo1Dict
from .ideal_response_info1 import IdealResponseInfo1, IdealResponseInfo1Dict
from .interac_card_response_info1 import InteracCardResponseInfo1, InteracCardResponseInfo1Dict
from .jcbresponse_info1 import JcbresponseInfo1, JcbresponseInfo1Dict
from .klarna_response_info1 import KlarnaResponseInfo1, KlarnaResponseInfo1Dict
from .maestro_response_info1 import MaestroResponseInfo1, MaestroResponseInfo1Dict
from .maestro_usaresponse_info1 import MaestroUsaresponseInfo1, MaestroUsaresponseInfo1Dict
from .mcresponse_info1 import McresponseInfo1, McresponseInfo1Dict
from .meal_voucher_frresponse_info1 import MealVoucherFrresponseInfo1, MealVoucherFrresponseInfo1Dict
from .nyce_response_info1 import NyceResponseInfo1, NyceResponseInfo1Dict
from .pay_by_bank_plaid_response_info1 import PayByBankPlaidResponseInfo1, PayByBankPlaidResponseInfo1Dict
from .pay_me_response_info1 import PayMeResponseInfo1, PayMeResponseInfo1Dict
from .pay_pal_response_info1 import PayPalResponseInfo1, PayPalResponseInfo1Dict
from .pay_to_response_info1 import PayToResponseInfo1, PayToResponseInfo1Dict
from .pulse_response_info2 import PulseResponseInfo2, PulseResponseInfo2Dict
from .sepa_direct_debit_response_info2 import SepaDirectDebitResponseInfo2, SepaDirectDebitResponseInfo2Dict
from .sodexo_response_info2 import SodexoResponseInfo2, SodexoResponseInfo2Dict
from .sofort_response_info2 import SofortResponseInfo2, SofortResponseInfo2Dict
from .star_response_info2 import StarResponseInfo2, StarResponseInfo2Dict
from .svs_response_info2 import SvsResponseInfo2, SvsResponseInfo2Dict
from .swish_response_info2 import SwishResponseInfo2, SwishResponseInfo2Dict
from .ticket_response_info2 import TicketResponseInfo2, TicketResponseInfo2Dict
from .twint_response_info2 import TwintResponseInfo2, TwintResponseInfo2Dict
from .valuelink_response_info2 import ValuelinkResponseInfo2, ValuelinkResponseInfo2Dict
from .vipps_response_info2 import VippsResponseInfo2, VippsResponseInfo2Dict
from .visa_response_info2 import VisaResponseInfo2, VisaResponseInfo2Dict
from .we_chat_pay_pos_response_info2 import WeChatPayPosResponseInfo2, WeChatPayPosResponseInfo2Dict
from .we_chat_pay_response_info2 import WeChatPayResponseInfo2, WeChatPayResponseInfo2Dict


class ManagementPaymentMethod(SdkBaseModel):
    accel: Optional[AccelResponseInfo1] = UNSET
    """**accel** details"""

    affirm: Optional[AffirmResponseInfo1] = UNSET
    """*affirm** details"""

    afterpay_touch: Optional[AfterpayTouchResponseInfo1] = Field(default=UNSET, alias="afterpayTouch")
    """**afterpaytouch** details"""

    alipay_plus: Optional[AlipayPlusResponseInfo1] = Field(default=UNSET, alias="alipayPlus")
    """**alipay_plus** details"""

    allowed: Optional[bool] = UNSET
    """Indicates whether receiving payments is allowed. This value is set to **true** by Adyen after screening your
    merchant account."""

    amex: Optional[AmexResponseInfo1] = UNSET
    """**amex** details"""

    apple_pay: Optional[ApplePayResponseInfo1] = Field(default=UNSET, alias="applePay")
    """**applepay** details"""

    associated_payment_methods: Optional[list[AssociatedPaymentMethod]] = Field(
        default=UNSET, alias="associatedPaymentMethods"
    )
    """Payment methods that were also updated as part of an associated transition."""

    bcmc: Optional[BcmcResponseInfo1] = UNSET
    """**bcmc** (Bancontact) details"""

    business_line_id: Optional[str] = Field(default=UNSET, alias="businessLineId")
    """The unique identifier of the business line. Required if you are a `platform model
    <https://docs.adyen.com/platforms>`__."""

    carnet: Optional[CarnetResponseInfo1] = UNSET
    """**carnet** details"""

    cartes_bancaires: Optional[CartesBancairesResponseInfo1] = Field(default=UNSET, alias="cartesBancaires")
    """**cartesbancaire** details"""

    clearpay: Optional[ClearpayResponseInfo1] = UNSET
    """**clearpay** details"""

    countries: Optional[list[str]] = UNSET
    """The list of countries where a payment method is available. By default, all countries supported by the payment
    method."""

    cup: Optional[CupResponseInfo1] = UNSET
    """**cup** (China Union Pay) details"""

    currencies: Optional[list[str]] = UNSET
    """The list of currencies that a payment method supports. By default, all currencies supported by the payment
    method."""

    custom_routing_flags: Optional[list[str]] = Field(default=UNSET, alias="customRoutingFlags")
    """The list of custom routing flags to route payment to the intended acquirer."""

    diners: Optional[DinersResponseInfo1] = UNSET
    """**diners** details"""

    discover: Optional[DiscoverResponseInfo1] = UNSET
    """**discover**. details"""

    eft_directdebit_ca: Optional[EftdirectDebitCaresponseInfo1] = Field(default=UNSET, alias="eft_directdebit_CA")
    """**eft_directdebit_CA** (EFT PAD) details"""

    eftpos_australia: Optional[EftPosAustraliaResponseInfo1] = UNSET
    """**eftpos_australia** details"""

    enabled: Optional[bool] = UNSET
    """Indicates whether the payment method is enabled (**true**) or disabled (**false**)."""

    girocard: Optional[GirocardResponseInfo1] = UNSET
    """**girocard** details"""

    givex: Optional[GivexResponseInfo1] = UNSET
    """**givex** details"""

    google_pay: Optional[GooglePayResponseInfo1] = Field(default=UNSET, alias="googlePay")
    """**googlepay** details"""

    id: str
    """The identifier of the resource."""

    ideal: Optional[IdealResponseInfo1] = UNSET
    """**ideal** details"""

    interac_card: Optional[InteracCardResponseInfo1] = UNSET
    """**interac_card** details"""

    jcb: Optional[JcbresponseInfo1] = UNSET
    """**jcb** details"""

    klarna: Optional[KlarnaResponseInfo1] = UNSET
    """**klarna** or its variant details"""

    maestro: Optional[MaestroResponseInfo1] = UNSET
    """**maestro** details"""

    maestro_usa: Optional[MaestroUsaresponseInfo1] = UNSET
    """Details to provide if ``type`` is **maestro_usa** details"""

    mc: Optional[McresponseInfo1] = UNSET
    """**mc** details"""

    meal_voucher_fr: Optional[MealVoucherFrresponseInfo1] = Field(default=UNSET, alias="mealVoucher_FR")
    """**mealVoucher_FR** details"""

    nyce: Optional[NyceResponseInfo1] = UNSET
    """**nyce** details"""

    paybybank_plaid: Optional[PayByBankPlaidResponseInfo1] = UNSET
    """**paybybank_plaid** details"""

    payme: Optional[PayMeResponseInfo1] = UNSET
    """**payme** details"""

    paypal: Optional[PayPalResponseInfo1] = UNSET
    """**paypal** details"""

    payto: Optional[PayToResponseInfo1] = UNSET
    """**payto** details"""

    pulse: Optional[PulseResponseInfo2] = UNSET
    """**pulse** details"""

    reference: Optional[str] = UNSET
    """Your reference for the payment method. Supported characters a-z, A-Z, 0-9."""

    sepadirectdebit: Optional[SepaDirectDebitResponseInfo2] = UNSET
    """**sepadirectdebit** details"""

    shopper_interaction: Optional[str] = Field(default=UNSET, alias="shopperInteraction")
    """The sales channel."""

    sodexo: Optional[SodexoResponseInfo2] = UNSET
    """**sodexo** details"""

    sofort: Optional[SofortResponseInfo2] = UNSET
    """Sofort details."""

    star: Optional[StarResponseInfo2] = UNSET
    """**star** details"""

    store_ids: Optional[list[str]] = Field(default=UNSET, alias="storeIds")
    """The unique identifier of the store for which to configure the payment method, if any."""

    svs: Optional[SvsResponseInfo2] = UNSET
    """**svs** details"""

    swish: Optional[SwishResponseInfo2] = UNSET
    """**swish** or its variant details"""

    ticket: Optional[TicketResponseInfo2] = UNSET
    """**ticket** (Edenred Brazil) details"""

    twint: Optional[TwintResponseInfo2] = UNSET
    """**twint** details"""

    type_: Optional[str] = Field(default=UNSET, alias="type")
    """Payment method `variant <https://docs.adyen.com/development-resources/paymentmethodvariant#management-api>`__."""

    valuelink: Optional[ValuelinkResponseInfo2] = UNSET
    """**valuelink** details"""

    verification_status: Optional[VerificationStatusOrStr] = Field(default=UNSET, alias="verificationStatus")
    """Payment method status. Possible values:
    * **valid**
    * **pending**
    * **invalid**
    * **rejected**"""

    vipps: Optional[VippsResponseInfo2] = UNSET
    """**vipps** details"""

    visa: Optional[VisaResponseInfo2] = UNSET
    """**visa** details"""

    wechatpay: Optional[WeChatPayResponseInfo2] = UNSET
    """**wechatpay** details"""

    wechatpay_pos: Optional[WeChatPayPosResponseInfo2] = UNSET
    """**wechatpay_pos** details"""


class ManagementPaymentMethodDict(TypedDict):
    accel: NotRequired[AccelResponseInfo1 | AccelResponseInfo1Dict]
    affirm: NotRequired[AffirmResponseInfo1 | AffirmResponseInfo1Dict]
    afterpay_touch: NotRequired[AfterpayTouchResponseInfo1 | AfterpayTouchResponseInfo1Dict]
    alipay_plus: NotRequired[AlipayPlusResponseInfo1 | AlipayPlusResponseInfo1Dict]
    allowed: NotRequired[bool]
    amex: NotRequired[AmexResponseInfo1 | AmexResponseInfo1Dict]
    apple_pay: NotRequired[ApplePayResponseInfo1 | ApplePayResponseInfo1Dict]
    associated_payment_methods: NotRequired[list[AssociatedPaymentMethod | AssociatedPaymentMethodDict]]
    bcmc: NotRequired[BcmcResponseInfo1 | BcmcResponseInfo1Dict]
    business_line_id: NotRequired[str]
    carnet: NotRequired[CarnetResponseInfo1 | CarnetResponseInfo1Dict]
    cartes_bancaires: NotRequired[CartesBancairesResponseInfo1 | CartesBancairesResponseInfo1Dict]
    clearpay: NotRequired[ClearpayResponseInfo1 | ClearpayResponseInfo1Dict]
    countries: NotRequired[list[str]]
    cup: NotRequired[CupResponseInfo1 | CupResponseInfo1Dict]
    currencies: NotRequired[list[str]]
    custom_routing_flags: NotRequired[list[str]]
    diners: NotRequired[DinersResponseInfo1 | DinersResponseInfo1Dict]
    discover: NotRequired[DiscoverResponseInfo1 | DiscoverResponseInfo1Dict]
    eft_directdebit_ca: NotRequired[EftdirectDebitCaresponseInfo1 | EftdirectDebitCaresponseInfo1Dict]
    eftpos_australia: NotRequired[EftPosAustraliaResponseInfo1 | EftPosAustraliaResponseInfo1Dict]
    enabled: NotRequired[bool]
    girocard: NotRequired[GirocardResponseInfo1 | GirocardResponseInfo1Dict]
    givex: NotRequired[GivexResponseInfo1 | GivexResponseInfo1Dict]
    google_pay: NotRequired[GooglePayResponseInfo1 | GooglePayResponseInfo1Dict]
    id: str
    ideal: NotRequired[IdealResponseInfo1 | IdealResponseInfo1Dict]
    interac_card: NotRequired[InteracCardResponseInfo1 | InteracCardResponseInfo1Dict]
    jcb: NotRequired[JcbresponseInfo1 | JcbresponseInfo1Dict]
    klarna: NotRequired[KlarnaResponseInfo1 | KlarnaResponseInfo1Dict]
    maestro: NotRequired[MaestroResponseInfo1 | MaestroResponseInfo1Dict]
    maestro_usa: NotRequired[MaestroUsaresponseInfo1 | MaestroUsaresponseInfo1Dict]
    mc: NotRequired[McresponseInfo1 | McresponseInfo1Dict]
    meal_voucher_fr: NotRequired[MealVoucherFrresponseInfo1 | MealVoucherFrresponseInfo1Dict]
    nyce: NotRequired[NyceResponseInfo1 | NyceResponseInfo1Dict]
    paybybank_plaid: NotRequired[PayByBankPlaidResponseInfo1 | PayByBankPlaidResponseInfo1Dict]
    payme: NotRequired[PayMeResponseInfo1 | PayMeResponseInfo1Dict]
    paypal: NotRequired[PayPalResponseInfo1 | PayPalResponseInfo1Dict]
    payto: NotRequired[PayToResponseInfo1 | PayToResponseInfo1Dict]
    pulse: NotRequired[PulseResponseInfo2 | PulseResponseInfo2Dict]
    reference: NotRequired[str]
    sepadirectdebit: NotRequired[SepaDirectDebitResponseInfo2 | SepaDirectDebitResponseInfo2Dict]
    shopper_interaction: NotRequired[str]
    sodexo: NotRequired[SodexoResponseInfo2 | SodexoResponseInfo2Dict]
    sofort: NotRequired[SofortResponseInfo2 | SofortResponseInfo2Dict]
    star: NotRequired[StarResponseInfo2 | StarResponseInfo2Dict]
    store_ids: NotRequired[list[str]]
    svs: NotRequired[SvsResponseInfo2 | SvsResponseInfo2Dict]
    swish: NotRequired[SwishResponseInfo2 | SwishResponseInfo2Dict]
    ticket: NotRequired[TicketResponseInfo2 | TicketResponseInfo2Dict]
    twint: NotRequired[TwintResponseInfo2 | TwintResponseInfo2Dict]
    type_: NotRequired[str]
    valuelink: NotRequired[ValuelinkResponseInfo2 | ValuelinkResponseInfo2Dict]
    verification_status: NotRequired[VerificationStatusOrStr]
    vipps: NotRequired[VippsResponseInfo2 | VippsResponseInfo2Dict]
    visa: NotRequired[VisaResponseInfo2 | VisaResponseInfo2Dict]
    wechatpay: NotRequired[WeChatPayResponseInfo2 | WeChatPayResponseInfo2Dict]
    wechatpay_pos: NotRequired[WeChatPayPosResponseInfo2 | WeChatPayPosResponseInfo2Dict]
