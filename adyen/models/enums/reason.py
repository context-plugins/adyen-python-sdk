from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Reason(str, Enum):
    """The reason for disabling the sweep."""

    ACCOUNT_HIERARCHY_NOT_ACTIVE = "accountHierarchyNotActive"
    AMOUNT_LIMIT_EXCEEDED = "amountLimitExceeded"
    APPROVED = "approved"
    COUNTERPARTY_ACCOUNT_BLOCKED = "counterpartyAccountBlocked"
    COUNTERPARTY_ACCOUNT_CLOSED = "counterpartyAccountClosed"
    COUNTERPARTY_ACCOUNT_NOT_FOUND = "counterpartyAccountNotFound"
    COUNTERPARTY_ADDRESS_REQUIRED = "counterpartyAddressRequired"
    COUNTERPARTY_BANK_TIMED_OUT = "counterpartyBankTimedOut"
    COUNTERPARTY_BANK_UNAVAILABLE = "counterpartyBankUnavailable"
    DIRECT_DEBIT_NOT_SUPPORTED = "directDebitNotSupported"
    ERROR = "error"
    NOT_ENOUGH_BALANCE = "notEnoughBalance"
    REFUSED_BY_COUNTERPARTY_BANK = "refusedByCounterpartyBank"
    ROUTE_NOT_FOUND = "routeNotFound"
    TRANSFER_INSTRUMENT_DOES_NOT_EXIST = "transferInstrumentDoesNotExist"
    UNKNOWN = "unknown"

    __str__ = str.__str__


ReasonOrStr: TypeAlias = Annotated[Reason | str, open_enum_validator(Reason)]
