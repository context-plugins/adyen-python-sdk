from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class StatusReason(str, Enum):
    """The reason for the status of the payment instrument.

    Possible values: **accountClosure**, **damaged**, **endOfLife**, **expired**, **lost**, **stolen**,
    **suspectedFraud**, **transactionRule**, **other**. If the reason is **other**, you must also send the
    ``statusComment`` parameter describing the status change."""

    ACCOUNT_CLOSURE = "accountClosure"
    DAMAGED = "damaged"
    END_OF_LIFE = "endOfLife"
    EXPIRED = "expired"
    LOST = "lost"
    OTHER = "other"
    STOLEN = "stolen"
    SUSPECTED_FRAUD = "suspectedFraud"
    TRANSACTION_RULE = "transactionRule"

    __str__ = str.__str__


StatusReasonOrStr: TypeAlias = Annotated[StatusReason | str, open_enum_validator(StatusReason)]
