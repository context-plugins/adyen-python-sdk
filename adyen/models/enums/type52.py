from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type52(str, Enum):
    """The payment method type."""

    ALIPAY_PLUS = "alipay_plus"
    ALIPAY_PLUS_ALIPAY_CN = "alipay_plus_alipay_cn"
    ALIPAY_PLUS_ALIPAY_HK = "alipay_plus_alipay_hk"
    ALIPAY_PLUS_DANA = "alipay_plus_dana"
    ALIPAY_PLUS_GCASH = "alipay_plus_gcash"
    ALIPAY_PLUS_KAKAOPAY = "alipay_plus_kakaopay"
    ALIPAY_PLUS_KPLUS = "alipay_plus_kplus"
    ALIPAY_PLUS_NAVERPAY = "alipay_plus_naverpay"
    ALIPAY_PLUS_RABBITLINEPAY = "alipay_plus_rabbitlinepay"
    ALIPAY_PLUS_TOSSPAY = "alipay_plus_tosspay"
    ALIPAY_PLUS_TOUCHNGO = "alipay_plus_touchngo"
    ALIPAY_PLUS_TRUEMONEY = "alipay_plus_truemoney"
    BCMC_MOBILE = "bcmc_mobile"
    BCMC_MOBILE_QR = "bcmc_mobile_QR"
    BCMC_MOBILE_APP = "bcmc_mobile_app"
    MOMO_WALLET = "momo_wallet"
    MOMO_WALLET_APP = "momo_wallet_app"
    PAYMAYA_WALLET = "paymaya_wallet"
    GRABPAY_SG = "grabpay_SG"
    GRABPAY_MY = "grabpay_MY"
    GRABPAY_TH = "grabpay_TH"
    GRABPAY_ID = "grabpay_ID"
    GRABPAY_VN = "grabpay_VN"
    GRABPAY_PH = "grabpay_PH"
    OXXO = "oxxo"
    GCASH = "gcash"
    DANA = "dana"
    KAKAOPAY = "kakaopay"
    TRUEMONEY = "truemoney"
    PAYSAFECARD = "paysafecard"
    GOPAY_WALLET = "gopay_wallet"

    __str__ = str.__str__


Type52OrStr: TypeAlias = Annotated[Type52 | str, open_enum_validator(Type52)]
