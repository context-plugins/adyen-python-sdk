from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .accel_update_info1 import AccelUpdateInfo1, AccelUpdateInfo1Dict
from .affirm_update_info1 import AffirmUpdateInfo1, AffirmUpdateInfo1Dict
from .bcmc_update_info1 import BcmcUpdateInfo1, BcmcUpdateInfo1Dict
from .cartes_bancaires_update_info1 import CartesBancairesUpdateInfo1, CartesBancairesUpdateInfo1Dict
from .cash_app_update_info1 import CashAppUpdateInfo1, CashAppUpdateInfo1Dict
from .generic_pm_with_tdi_update_info1 import GenericPmWithTdiUpdateInfo1, GenericPmWithTdiUpdateInfo1Dict
from .generic_pm_with_tdi_update_info2 import GenericPmWithTdiUpdateInfo2, GenericPmWithTdiUpdateInfo2Dict
from .generic_pm_with_tdi_update_info3 import GenericPmWithTdiUpdateInfo3, GenericPmWithTdiUpdateInfo3Dict
from .generic_pm_with_tdi_update_info4 import GenericPmWithTdiUpdateInfo4, GenericPmWithTdiUpdateInfo4Dict
from .generic_pm_with_tdi_update_info5 import GenericPmWithTdiUpdateInfo5, GenericPmWithTdiUpdateInfo5Dict
from .generic_pm_with_tdi_update_info6 import GenericPmWithTdiUpdateInfo6, GenericPmWithTdiUpdateInfo6Dict
from .generic_pm_with_tdi_update_info7 import GenericPmWithTdiUpdateInfo7, GenericPmWithTdiUpdateInfo7Dict
from .generic_pm_with_tdi_update_info8 import GenericPmWithTdiUpdateInfo8, GenericPmWithTdiUpdateInfo8Dict
from .generic_pm_with_tdi_update_info9 import GenericPmWithTdiUpdateInfo9, GenericPmWithTdiUpdateInfo9Dict
from .generic_pm_with_tdi_update_info10 import GenericPmWithTdiUpdateInfo10, GenericPmWithTdiUpdateInfo10Dict
from .generic_pm_with_tdi_update_info11 import GenericPmWithTdiUpdateInfo11, GenericPmWithTdiUpdateInfo11Dict
from .generic_pm_with_tdi_update_info12 import GenericPmWithTdiUpdateInfo12, GenericPmWithTdiUpdateInfo12Dict
from .generic_pm_with_tdi_update_info13 import GenericPmWithTdiUpdateInfo13, GenericPmWithTdiUpdateInfo13Dict
from .generic_pm_with_tdi_update_info14 import GenericPmWithTdiUpdateInfo14, GenericPmWithTdiUpdateInfo14Dict
from .nyce_update_info1 import NyceUpdateInfo1, NyceUpdateInfo1Dict
from .pay_by_bank_plaid_update_info1 import PayByBankPlaidUpdateInfo1, PayByBankPlaidUpdateInfo1Dict
from .pulse_update_info1 import PulseUpdateInfo1, PulseUpdateInfo1Dict
from .sepa_direct_debit_update_info1 import SepaDirectDebitUpdateInfo1, SepaDirectDebitUpdateInfo1Dict
from .star_update_info1 import StarUpdateInfo1, StarUpdateInfo1Dict


class UpdatePaymentMethodInfo(SdkBaseModel):
    accel: Optional[AccelUpdateInfo1] = UNSET
    """Details to provide if ``type`` is **accel**."""

    affirm: Optional[AffirmUpdateInfo1] = UNSET
    """Details to provide if ``type`` is **affirm**."""

    bcmc: Optional[BcmcUpdateInfo1] = UNSET
    """Details to provide if ``type`` is **bcmc** (Bancontact)."""

    carnet: Optional[GenericPmWithTdiUpdateInfo1] = UNSET
    """Details to provide if ``type`` is **carnet**."""

    cartes_bancaires: Optional[CartesBancairesUpdateInfo1] = Field(default=UNSET, alias="cartesBancaires")
    """Details to provide if ``type`` is **cartebancaire**."""

    cashapp: Optional[CashAppUpdateInfo1] = UNSET
    """Details to provide if ``type`` is **cashapp**."""

    countries: Optional[list[str]] = UNSET
    """The list of countries where a payment method is available. By default, all countries supported by the payment
    method."""

    cup: Optional[GenericPmWithTdiUpdateInfo2] = UNSET
    """Details to provide if ``type`` is **cup** (China Union Pay)."""

    currencies: Optional[list[str]] = UNSET
    """The list of currencies that a payment method supports. By default, all currencies supported by the payment
    method."""

    custom_routing_flags: Optional[list[str]] = Field(default=UNSET, alias="customRoutingFlags")
    """Custom routing flags for acquirer routing."""

    diners: Optional[GenericPmWithTdiUpdateInfo3] = UNSET
    """Details to provide if ``type`` is **diners**. For merchants operating in Japan, Diners payments are processed
    through the JCB network. This means that you must include `JCB-specific fields
    <https://docs.adyen.com/api-explorer/Management/latest/post/merchants/(merchantId>`__/paymentMethodSettings/(paymentMethodId)#request-jcb)
    in this object."""

    discover: Optional[GenericPmWithTdiUpdateInfo4] = UNSET
    """Details to provide if ``type`` is **discover**. For merchants operating in Japan, request `Diners
    <https://docs.adyen.com/api-explorer/Management/latest/post/merchants/(merchantId>`__/paymentMethodSettings/(paymentMethodId)#request-diners)
    payment method instead. Discover is automatically requested, together with Diners."""

    eft_directdebit_ca: Optional[GenericPmWithTdiUpdateInfo5] = Field(default=UNSET, alias="eft_directdebit_CA")
    """Details to provide if ``type`` is **eft_directdebit_CA** (EFT PAD)."""

    eftpos_australia: Optional[GenericPmWithTdiUpdateInfo6] = UNSET
    """Details to provide if ``type`` is **eftpos_australia**."""

    enabled: Optional[bool] = UNSET
    """Indicates whether the payment method is enabled (**true**) or disabled (**false**)."""

    girocard: Optional[GenericPmWithTdiUpdateInfo7] = UNSET
    """Details to provide if ``type`` is **girocard**."""

    ideal: Optional[GenericPmWithTdiUpdateInfo8] = UNSET
    """Details to provide if ``type`` is **ideal**."""

    interac_card: Optional[GenericPmWithTdiUpdateInfo9] = UNSET
    """Details to provide if ``type`` is **interac_card**."""

    jcb: Optional[GenericPmWithTdiUpdateInfo10] = UNSET
    """Details to provide if ``type`` is **jcb**. For merchants operating in Japan, ``midNumber``, ``reuseMidNumber``,
    and ``serviceLevel`` fields are required. For merchants operating outside of Japan, these fields are not
    required."""

    maestro: Optional[GenericPmWithTdiUpdateInfo11] = UNSET
    """Details to provide if ``type`` is **maestro**. In the US, ``maestro`` is not supported; use ``maestro_usa``
    instead."""

    maestro_usa: Optional[GenericPmWithTdiUpdateInfo12] = UNSET
    """Details to provide if ``type`` is **maestro_usa**. Only for Maestro USA, otherwise use ``maestro``."""

    mc: Optional[GenericPmWithTdiUpdateInfo13] = UNSET
    """Details to provide if ``type`` is **mc**."""

    nyce: Optional[NyceUpdateInfo1] = UNSET
    """Details to provide if ``type`` is **nyce**."""

    paybybank_plaid: Optional[PayByBankPlaidUpdateInfo1] = UNSET
    """Details to provide if ``type`` is **paybybank_plaid**."""

    pulse: Optional[PulseUpdateInfo1] = UNSET
    """Details to provide if ``type`` is **pulse**."""

    sepadirectdebit: Optional[SepaDirectDebitUpdateInfo1] = UNSET
    """Details to provide if ``type`` is **sepadirectdebit**."""

    star: Optional[StarUpdateInfo1] = UNSET
    """Details to provide if ``type`` is **star**."""

    store_id: Optional[str] = Field(default=UNSET, alias="storeId")
    """The store for this payment method"""

    store_ids: Optional[list[str]] = Field(default=UNSET, alias="storeIds")
    """The list of stores for this payment method"""

    visa: Optional[GenericPmWithTdiUpdateInfo14] = UNSET
    """Details to provide if ``type`` is **visa**."""


class UpdatePaymentMethodInfoDict(TypedDict):
    accel: NotRequired[AccelUpdateInfo1 | AccelUpdateInfo1Dict]
    affirm: NotRequired[AffirmUpdateInfo1 | AffirmUpdateInfo1Dict]
    bcmc: NotRequired[BcmcUpdateInfo1 | BcmcUpdateInfo1Dict]
    carnet: NotRequired[GenericPmWithTdiUpdateInfo1 | GenericPmWithTdiUpdateInfo1Dict]
    cartes_bancaires: NotRequired[CartesBancairesUpdateInfo1 | CartesBancairesUpdateInfo1Dict]
    cashapp: NotRequired[CashAppUpdateInfo1 | CashAppUpdateInfo1Dict]
    countries: NotRequired[list[str]]
    cup: NotRequired[GenericPmWithTdiUpdateInfo2 | GenericPmWithTdiUpdateInfo2Dict]
    currencies: NotRequired[list[str]]
    custom_routing_flags: NotRequired[list[str]]
    diners: NotRequired[GenericPmWithTdiUpdateInfo3 | GenericPmWithTdiUpdateInfo3Dict]
    discover: NotRequired[GenericPmWithTdiUpdateInfo4 | GenericPmWithTdiUpdateInfo4Dict]
    eft_directdebit_ca: NotRequired[GenericPmWithTdiUpdateInfo5 | GenericPmWithTdiUpdateInfo5Dict]
    eftpos_australia: NotRequired[GenericPmWithTdiUpdateInfo6 | GenericPmWithTdiUpdateInfo6Dict]
    enabled: NotRequired[bool]
    girocard: NotRequired[GenericPmWithTdiUpdateInfo7 | GenericPmWithTdiUpdateInfo7Dict]
    ideal: NotRequired[GenericPmWithTdiUpdateInfo8 | GenericPmWithTdiUpdateInfo8Dict]
    interac_card: NotRequired[GenericPmWithTdiUpdateInfo9 | GenericPmWithTdiUpdateInfo9Dict]
    jcb: NotRequired[GenericPmWithTdiUpdateInfo10 | GenericPmWithTdiUpdateInfo10Dict]
    maestro: NotRequired[GenericPmWithTdiUpdateInfo11 | GenericPmWithTdiUpdateInfo11Dict]
    maestro_usa: NotRequired[GenericPmWithTdiUpdateInfo12 | GenericPmWithTdiUpdateInfo12Dict]
    mc: NotRequired[GenericPmWithTdiUpdateInfo13 | GenericPmWithTdiUpdateInfo13Dict]
    nyce: NotRequired[NyceUpdateInfo1 | NyceUpdateInfo1Dict]
    paybybank_plaid: NotRequired[PayByBankPlaidUpdateInfo1 | PayByBankPlaidUpdateInfo1Dict]
    pulse: NotRequired[PulseUpdateInfo1 | PulseUpdateInfo1Dict]
    sepadirectdebit: NotRequired[SepaDirectDebitUpdateInfo1 | SepaDirectDebitUpdateInfo1Dict]
    star: NotRequired[StarUpdateInfo1 | StarUpdateInfo1Dict]
    store_id: NotRequired[str]
    store_ids: NotRequired[list[str]]
    visa: NotRequired[GenericPmWithTdiUpdateInfo14 | GenericPmWithTdiUpdateInfo14Dict]
