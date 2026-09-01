from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ResponseAdditionalDataSepa(SdkBaseModel):
    sepadirectdebit_date_of_signature: Optional[str] = Field(default=UNSET, alias="sepadirectdebit.dateOfSignature")
    """The transaction signature date.

    Format: yyyy-MM-dd"""

    sepadirectdebit_mandate_id: Optional[str] = Field(default=UNSET, alias="sepadirectdebit.mandateId")
    """Its value corresponds to the pspReference value of the transaction."""

    sepadirectdebit_sepadirectdebit_due_date: Optional[str] = Field(
        default=UNSET, alias="sepadirectdebit.sepadirectdebit.dueDate"
    )
    """The date that the the shopper's bank account is charged."""

    sepadirectdebit_sequence_type: Optional[str] = Field(default=UNSET, alias="sepadirectdebit.sequenceType")
    """This field can take one of the following values:
    * OneOff: (OOFF) Direct debit instruction to initiate exactly one direct debit transaction.

    * First: (FRST) Initial/first collection in a series of direct debit instructions.
    * Recurring: (RCUR) Direct debit instruction to carry out regular direct debit transactions initiated by the
        creditor.
    * Final: (FNAL) Last/final collection in a series of direct debit instructions.

    Example: OOFF"""


class ResponseAdditionalDataSepaDict(TypedDict):
    sepadirectdebit_date_of_signature: NotRequired[str]
    sepadirectdebit_mandate_id: NotRequired[str]
    sepadirectdebit_sepadirectdebit_due_date: NotRequired[str]
    sepadirectdebit_sequence_type: NotRequired[str]
