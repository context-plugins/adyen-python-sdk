from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.outcome_type import OutcomeTypeOrStr
from .enums.purpose import PurposeOrStr
from .enums.request_type import RequestTypeOrStr
from .enums.status6 import Status6OrStr
from .enums.type141 import Type141OrStr
from .transaction_rule_entity_key2 import TransactionRuleEntityKey2, TransactionRuleEntityKey2Dict
from .transaction_rule_interval1 import TransactionRuleInterval1, TransactionRuleInterval1Dict
from .transaction_rule_restrictions1 import TransactionRuleRestrictions1, TransactionRuleRestrictions1Dict


class TransactionRule1(SdkBaseModel):
    """The transaction rule."""

    aggregation_level: Optional[str] = Field(default=UNSET, alias="aggregationLevel")
    """The level at which data must be accumulated, used in rules with ``type`` **velocity** or **maxUsage**. The level
    must be the `same or lower in hierarchy <https://docs.adyen.com/issuing/transaction-rules#accumulate-data>`__ than
    the ``entityKey``.

    If not provided, by default, the rule will accumulate data at the **paymentInstrument** level.

    Possible values: **paymentInstrument**, **paymentInstrumentGroup**, **balanceAccount**, **accountHolder**,
    **balancePlatform**."""

    description: str
    """Your description for the transaction rule."""

    end_date: Optional[str] = Field(default=UNSET, alias="endDate")
    """The date when the rule will stop being evaluated, in ISO 8601 extended offset date-time format. For example,
    **2025-03-19T10:15:30+01:00**.

    If not provided, the rule will be evaluated until the rule status is set to **inactive**."""

    entity_key: TransactionRuleEntityKey2 = Field(alias="entityKey")
    """The type and unique identifier of the resource to which the rule applies."""

    id: Optional[str] = UNSET
    """The unique identifier of the transaction rule."""

    interval: TransactionRuleInterval1
    """The `time interval <https://docs.adyen.com/issuing/transaction-rules#time-intervals>`__ when the rule conditions
    apply."""

    outcome_type: Optional[OutcomeTypeOrStr] = Field(default=UNSET, alias="outcomeType")
    """The `outcome <https://docs.adyen.com/issuing/transaction-rules#outcome>`__ that will be applied when a
    transaction meets the conditions of the rule.

    Possible values:
    * **hardBlock** (default): the transaction is declined.
    * **scoreBased**: the transaction is assigned the ``score`` you specified. Adyen calculates the total score and if
        it exceeds 100, the transaction is declined. This value is not allowed when ``requestType`` is **bankTransfer**.

    * **enforceSCA**: your user is prompted to verify their identity using `3D Secure authentication
        <https://docs.adyen.com/issuing/3d-secure/>`__. If the authentication fails or times out, the transaction is
        declined. This value is only allowed when ``requestType`` is **authentication**."""

    overrides_rule: Optional[str] = Field(default=UNSET, alias="overridesRule")
    """The ``id`` of the transaction rule you want to override or skip for the specified ``entityKey``."""

    purpose: Optional[PurposeOrStr] = UNSET
    """Specifies the reason for creating the rule.

    Possible values:
    * **fraud**: the rule is created to regulate fraudulent activity.
    * **policy**: the rule is created to ensure that the transaction adheres to your business' policies. For example, if
        your business has policies about the Merchant Category Codes (MCCs) allowed on a transaction, you can create a
        rule to block transactions that have specific MCCs."""

    reference: str
    """Your reference for the transaction rule."""

    request_type: Optional[RequestTypeOrStr] = Field(default=UNSET, alias="requestType")
    """Indicates the type of request to which the rule applies. If not provided, by default, this is set to
    **authorization**.

    Possible values: **authorization**, **authentication**, **tokenization**, **bankTransfer**."""

    rule_restrictions: TransactionRuleRestrictions1 = Field(alias="ruleRestrictions")
    """Contains one or more objects that define the `rule conditions
    <https://docs.adyen.com/issuing/transaction-rules#conditions>`__. Each object must have a value and an operation
    which determines how the values must be evaluated.

    For example, a ``countries`` object can have a list of country codes **["US", "CA"]** in the ``value`` field and
    **anyMatch** in the ``operation`` field."""

    score: Optional[int] = UNSET
    """A positive or negative score applied to the transaction if it meets the conditions of the rule. Required when
    ``outcomeType`` is **scoreBased**. The value must be between **-100** and **100**."""

    start_date: Optional[str] = Field(default=UNSET, alias="startDate")
    """The date when the rule will start to be evaluated, in ISO 8601 extended offset date-time format. For example,
    **2025-03-19T10:15:30+01:00**.

    If not provided when creating a transaction rule, the ``startDate`` is set to the date when the rule status is set
    to **active**."""

    status: Optional[Status6OrStr] = UNSET
    """The status of the transaction rule. If you provide a ``startDate`` in the request, the rule is automatically
    created with an **active** status.

    Possible values: **active**, **inactive**."""

    type_: Type141OrStr = Field(alias="type")
    """The `type of rule <https://docs.adyen.com/issuing/transaction-rules#rule-types>`__, which defines if a rule
    blocks transactions based on individual characteristics or accumulates data.

    Possible values:
     * **blockList**: decline a transaction when the conditions are met.
     * **maxUsage**: add the amount or number of transactions for the lifetime of a payment instrument, and then decline
            a transaction when the specified limits are met.
     * **velocity**: add the amount or number of transactions based on a specified time interval, and then decline a
            transaction when the specified limits are met.
     * **bypass**: bypass or skip a rule for the specified ``entityKey``. Transactions processed to that entity are no
            longer evaluated by the bypassed rule. You must provide the ``id`` of the rule to bypass in
            ``overridesRule`` and leave the ``ruleRestrictions`` object empty."""


class TransactionRule1Dict(TypedDict):
    aggregation_level: NotRequired[str]
    description: str
    end_date: NotRequired[str]
    entity_key: TransactionRuleEntityKey2Dict
    id: NotRequired[str]
    interval: TransactionRuleInterval1Dict
    outcome_type: NotRequired[OutcomeTypeOrStr]
    overrides_rule: NotRequired[str]
    purpose: NotRequired[PurposeOrStr]
    reference: str
    request_type: NotRequired[RequestTypeOrStr]
    rule_restrictions: TransactionRuleRestrictions1Dict
    score: NotRequired[int]
    start_date: NotRequired[str]
    status: NotRequired[Status6OrStr]
    type_: Type141OrStr
