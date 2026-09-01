from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, SdkBaseModel
from .enums.instalment_type import InstalmentTypeOrStr
from .enums.period_unit1 import PeriodUnit1OrStr


class Instalment1(SdkBaseModel):
    """Information related an instalment transaction. To request an instalment to the issuer, or to make individual
    instalments of a payment transaction."""

    instalment_type: Optional[InstalmentTypeOrStr] = Field(default=UNSET, alias="InstalmentType")
    """Type of instalment transaction. For requesting an instalment payment transaction. Possible values:
    * **DeferredInstalments**
    * **EqualInstalments**
    * **InequalInstalments**"""

    sequence_number: Optional[int] = Field(default=UNSET, alias="SequenceNumber")
    """Sequence number of the instalment. For an instalment payment transaction, number of the payment, from 1 to
    TotalNbOfPayments."""

    plan_id: Optional[str] = Field(default=UNSET, alias="PlanID")
    """Identification of an instalment plan."""

    period: Optional[int] = Field(default=UNSET, alias="Period")
    """Period of time with defined unit of time. A period between 2 payment instalments."""

    period_unit: Optional[PeriodUnit1OrStr] = Field(default=UNSET, alias="PeriodUnit")
    """Type of instalment transaction. Possible values:
    * **Annual**
    * **Daily**
    * **Monthly**
    * **Weekly**"""

    first_payment_date: Optional[Date] = Field(default=UNSET, alias="FirstPaymentDate")
    """First date of a payment. For instalment, the date of the first payments, if not immediate."""

    total_nb_of_payments: Optional[int] = Field(default=UNSET, alias="TotalNbOfPayments")
    """Total number of payments. For instalment, the number of payments, including the first one."""

    cumulative_amount: Optional[float] = Field(default=UNSET, alias="CumulativeAmount")
    """Sum of a collection of amounts. Total amount of the payment instalments."""

    first_amount: Optional[float] = Field(default=UNSET, alias="FirstAmount")
    """First amount of the payment instalments."""

    charges: Optional[float] = Field(default=UNSET, alias="Charges")
    """Charges related to a transaction. Charge related to the payment instalments."""


class Instalment1Dict(TypedDict):
    instalment_type: NotRequired[InstalmentTypeOrStr]
    sequence_number: NotRequired[int]
    plan_id: NotRequired[str]
    period: NotRequired[int]
    period_unit: NotRequired[PeriodUnit1OrStr]
    first_payment_date: NotRequired[Date]
    total_nb_of_payments: NotRequired[int]
    cumulative_amount: NotRequired[float]
    first_amount: NotRequired[float]
    charges: NotRequired[float]
