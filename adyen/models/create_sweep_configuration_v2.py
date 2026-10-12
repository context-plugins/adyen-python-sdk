from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .amount17 import Amount17, Amount17Dict
from .enums.category1 import Category1OrStr
from .enums.priority1 import Priority1OrStr
from .enums.reason import ReasonOrStr
from .enums.status6 import Status6OrStr
from .enums.type72 import Type72, Type72OrStr
from .sweep_counterparty1 import SweepCounterparty1, SweepCounterparty1Dict
from .sweep_schedule1 import SweepSchedule1, SweepSchedule1Dict


class CreateSweepConfigurationV2(SdkBaseModel):
    category: Optional[Category1OrStr] = UNSET
    """The type of transfer that results from the sweep.

    Possible values:

     - **bank**: Sweep to a `transfer instrument
            <https://docs.adyen.com/api-explorer/#/legalentity/latest/post/transferInstruments__resParam_id>`__.

    - **internal**: Transfer to another `balance account
        <https://docs.adyen.com/api-explorer/#/balanceplatform/latest/post/balanceAccounts__resParam_id>`__ within your
        platform.

    Required when setting ``priorities``."""

    counterparty: SweepCounterparty1
    """The destination or the source of the funds, depending on the sweep ``type``.

    Either a ``balanceAccountId``, ``transferInstrumentId``, or ``merchantAccount`` is required."""

    currency: str
    """The three-character `ISO currency code <https://docs.adyen.com/development-resources/currency-codes>`__ in
    uppercase. For example, **EUR**.

    The sweep currency must match any of the `balances currencies
    <https://docs.adyen.com/api-explorer/#/balanceplatform/latest/get/balanceAccounts/{id}__resParam_balances>`__."""

    description: Optional[str] = UNSET
    """The message that will be used in the sweep transfer's description body with a maximum length of 140 characters.

    If the message is longer after replacing placeholders, the message will be cut off at 140 characters."""

    priorities: Optional[list[Priority1OrStr]] = UNSET
    """The list of priorities for the bank transfer. This sets the speed at which the transfer is sent and the fees that
    you have to pay. You can provide multiple priorities, ordered by your preference. Adyen will try to pay out using
    the priorities in the given order. If the first priority is not currently supported or enabled for your platform,
    the system will try the next one, and so on.

    The request will be accepted as long as **at least one** of the provided priorities is valid (i.e., supported by
    Adyen and activated for your platform). For example, if you provide ``["wire","regular"]``, and ``wire`` is not
    supported but ``regular`` is, the request will still be accepted and processed.

    Possible values:

    * **regular**: For normal, low-value transactions.

    * **fast**: A faster way to transfer funds, but the fees are higher. Recommended for high-priority, low-value
        transactions.

    * **wire**: The fastest way to transfer funds, but this has the highest fees. Recommended for high-priority,
        high-value transactions.

    * **instant**: For instant funds transfers within the United States and in `SEPA locations
        <https://www.ecb.europa.eu/paym/integration/retail/sepa/html/index.en.html>`__.

    * **crossBorder**: For high-value transfers to a recipient in a different country.

    * **internal**: For transfers to an Adyen-issued business bank account (by bank account number/IBAN).

    Set ``category`` to **bank**. For more details, see optional priorities setup for `marketplaces
    <https://docs.adyen.com/marketplaces/payout-to-users/scheduled-payouts#optional-priorities-setup>`__ or `platforms
    <https://docs.adyen.com/platforms/payout-to-users/scheduled-payouts#optional-priorities-setup>`__."""

    reason: Optional[ReasonOrStr] = UNSET
    """The reason for disabling the sweep."""

    reason_detail: Optional[str] = Field(default=UNSET, alias="reasonDetail")
    """The human readable reason for disabling the sweep."""

    reference: Optional[str] = UNSET
    """Your reference for the sweep configuration."""

    reference_for_beneficiary: Optional[str] = Field(default=UNSET, alias="referenceForBeneficiary")
    """The reference sent to or received from the counterparty. Only alphanumeric characters are allowed."""

    schedule: SweepSchedule1
    """The schedule when the ``triggerAmount`` is evaluated. If the balance meets the threshold, funds are pushed out of
    or pulled in to the balance account."""

    status: Optional[Status6OrStr] = UNSET
    """The status of the sweep. If not provided, by default, this is set to **active**.

    Possible values:

     * **active**: the sweep is enabled and funds will be pulled in or pushed out based on the defined configuration.

     * **inactive**: the sweep is disabled and cannot be triggered."""

    sweep_amount: Optional[Amount17] = Field(default=UNSET, alias="sweepAmount")
    """The amount that must be pushed out or pulled in. You can configure either ``sweepAmount`` or ``targetAmount``,
    not both."""

    target_amount: Optional[Amount17] = Field(default=UNSET, alias="targetAmount")
    """The amount that must be available in the balance account after the sweep. You can configure either
    ``sweepAmount`` or ``targetAmount``, not both."""

    trigger_amount: Optional[Amount17] = Field(default=UNSET, alias="triggerAmount")
    """The threshold amount that triggers the sweep. If not provided, by default, the amount is set to zero. The
    ``triggerAmount`` is evaluated according to the specified ``schedule.type``.

    * For ``type`` **pull**, if the balance is less than or equal to the ``triggerAmount``, funds are pulled in to the
        balance account.

    * For ``type`` **push**, if the balance is more than or equal to the ``triggerAmount``, funds are pushed out of the
        balance account."""

    type_: Type72OrStr = Field(default=Type72.PUSH, alias="type")
    """The direction of sweep, whether pushing out or pulling in funds to the balance account. If not provided, by
    default, this is set to **push**.

    Possible values:

     * **push**: _push out funds_ to a destination balance account or transfer instrument.

     * **pull**: _pull in funds_ from a source merchant account, transfer instrument, or balance account."""


class CreateSweepConfigurationV2Dict(TypedDict):
    category: NotRequired[Category1OrStr]
    counterparty: SweepCounterparty1Dict
    currency: str
    description: NotRequired[str]
    priorities: NotRequired[list[Priority1OrStr]]
    reason: NotRequired[ReasonOrStr]
    reason_detail: NotRequired[str]
    reference: NotRequired[str]
    reference_for_beneficiary: NotRequired[str]
    schedule: SweepSchedule1Dict
    status: NotRequired[Status6OrStr]
    sweep_amount: NotRequired[Amount17Dict]
    target_amount: NotRequired[Amount17Dict]
    trigger_amount: NotRequired[Amount17Dict]
    type_: NotRequired[Type72OrStr]
