from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.card_region import CardRegionOrStr
from .enums.funding_source1 import FundingSource1OrStr
from .enums.shopper_interaction11 import ShopperInteraction11OrStr
from .split_configuration_logic2 import SplitConfigurationLogic2, SplitConfigurationLogic2Dict


class SplitConfigurationRule(SdkBaseModel):
    card_region: Optional[CardRegionOrStr] = Field(default=UNSET, alias="cardRegion")
    """The card region condition that determines whether the `split logic
    <https://docs.adyen.com/api-explorer/Management/latest/post/merchants/(merchantId>`__/splitConfigurations#request-rules-splitLogic)
    applies to the transaction.

    > This condition is in pilot phase, and not yet available for all platforms.

    Possible values:
    * **domestic**: The card issuer and the store where the transaction is processed are registered in the same country.
    * **international**: The card issuer and the store where the transaction is processed are registered in different
        countries or regions. Includes all **interRegional** and **intraRegional** transactions.
    * **interRegional**: The card issuer and the store where the transaction is processed are registered in different
        regions.
    * **intraRegional**: The card issuer and the store where the transaction is processed are registered in different
        countries, but in the same region.
    * **intraEEA**: The card issuer and the store where the transaction is processed are registered in different
        countries, but in the European Economic Area (EEA).
    * **ANY**: Applies to all transactions, regardless of the processing and issuing country/region."""

    currency: str
    """The currency condition that defines whether the split logic applies. Its value must be a three-character `ISO
    currency code <https://en.wikipedia.org/wiki/ISO_4217>`__."""

    funding_source: FundingSource1OrStr = Field(alias="fundingSource")
    """The funding source of the payment method.

    Possible values:
    * **credit**
    * **debit**
    * **prepaid**
    * **deferred_debit**
    * **charged**
    * **ANY**"""

    payment_method: str = Field(alias="paymentMethod")
    """The payment method condition that defines whether the split logic applies.

    Possible values:
    * `Payment method variant <https://docs.adyen.com/development-resources/paymentmethodvariant>`__: Apply the split
        logic for a specific payment method.
    * **ANY**: Apply the split logic for all available payment methods."""

    rule_id: Optional[str] = Field(default=UNSET, alias="ruleId")
    """The unique identifier of the split configuration rule."""

    shopper_interaction: ShopperInteraction11OrStr = Field(alias="shopperInteraction")
    """The sales channel condition that defines whether the split logic applies.

    Possible values:
    * **Ecommerce**: Online transactions where the cardholder is present.
    * **ContAuth**: Card on file and/or subscription transactions, where the cardholder is known to the merchant
        (returning customer).
    * **Moto**: Mail-order and telephone-order transactions where the customer is in contact with the merchant via email
        or telephone.
    * **POS**: Point-of-sale transactions where the customer is physically present to make a payment using a secure
        payment terminal.
    * **ANY**: All sales channels."""

    split_logic: SplitConfigurationLogic2 = Field(alias="splitLogic")
    """Contains the split logic that is applied if the rule conditions are met."""


class SplitConfigurationRuleDict(TypedDict):
    card_region: NotRequired[CardRegionOrStr]
    currency: str
    funding_source: FundingSource1OrStr
    payment_method: str
    rule_id: NotRequired[str]
    shopper_interaction: ShopperInteraction11OrStr
    split_logic: SplitConfigurationLogic2 | SplitConfigurationLogic2Dict
