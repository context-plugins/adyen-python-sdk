from __future__ import annotations

from typing import Annotated, TypeAlias

from pydantic import Tag

from ...core import WireDiscriminator
from ..additional_bank_identification_requirement import (
    AdditionalBankIdentificationRequirement,
    AdditionalBankIdentificationRequirementDict,
)
from ..address_requirement import AddressRequirement, AddressRequirementDict
from ..amount_min_max_requirement import AmountMinMaxRequirement, AmountMinMaxRequirementDict
from ..amount_non_zero_decimals_requirement import (
    AmountNonZeroDecimalsRequirement,
    AmountNonZeroDecimalsRequirementDict,
)
from ..bank_account_identification_type_requirement import (
    BankAccountIdentificationTypeRequirement,
    BankAccountIdentificationTypeRequirementDict,
)
from ..iban_account_identification_requirement import (
    IbanAccountIdentificationRequirement,
    IbanAccountIdentificationRequirementDict,
)
from ..payment_instrument_requirement import PaymentInstrumentRequirement, PaymentInstrumentRequirementDict
from ..usinstant_payout_address_requirement import (
    UsinstantPayoutAddressRequirement,
    UsinstantPayoutAddressRequirementDict,
)
from ..usinternational_ach_address_requirement import (
    UsinternationalAchAddressRequirement,
    UsinternationalAchAddressRequirementDict,
)
from ..usinternational_ach_priority_requirement import (
    UsinternationalAchPriorityRequirement,
    UsinternationalAchPriorityRequirementDict,
)

Requirement: TypeAlias = Annotated[
    (
        Annotated[AdditionalBankIdentificationRequirement, Tag("additionalBankIdentificationRequirement")]
        | Annotated[AddressRequirement, Tag("addressRequirement")]
        | Annotated[AmountMinMaxRequirement, Tag("amountMinMaxRequirement")]
        | Annotated[AmountNonZeroDecimalsRequirement, Tag("amountNonZeroDecimalsRequirement")]
        | Annotated[BankAccountIdentificationTypeRequirement, Tag("bankAccountIdentificationTypeRequirement")]
        | Annotated[IbanAccountIdentificationRequirement, Tag("ibanAccountIdentificationRequirement")]
        | Annotated[PaymentInstrumentRequirement, Tag("paymentInstrumentRequirement")]
        | Annotated[UsinstantPayoutAddressRequirement, Tag("usInstantPayoutAddressRequirement")]
        | Annotated[UsinternationalAchAddressRequirement, Tag("usInternationalAchAddressRequirement")]
        | Annotated[UsinternationalAchPriorityRequirement, Tag("usInternationalAchPriorityRequirement")]
    ),
    WireDiscriminator("type"),
]

RequirementDict: TypeAlias = (
    AdditionalBankIdentificationRequirementDict
    | AddressRequirementDict
    | AmountMinMaxRequirementDict
    | AmountNonZeroDecimalsRequirementDict
    | BankAccountIdentificationTypeRequirementDict
    | IbanAccountIdentificationRequirementDict
    | PaymentInstrumentRequirementDict
    | UsinstantPayoutAddressRequirementDict
    | UsinternationalAchAddressRequirementDict
    | UsinternationalAchPriorityRequirementDict
)
