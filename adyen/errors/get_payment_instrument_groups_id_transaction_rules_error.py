from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.rest_service_error import RestServiceError

GetPaymentInstrumentGroupsIdTransactionRulesErrorBody: TypeAlias = RestServiceError | RawError


@dataclass(frozen=True, slots=True)
class _GetPaymentInstrumentGroupsIdTransactionRulesError:
    def map(self, status_code: int, content: bytes) -> GetPaymentInstrumentGroupsIdTransactionRulesErrorBody:
        match status_code:
            case 400 | 401 | 403 | 422 | 500:
                return decode_json[RestServiceError](content)
            case _:
                return RawError(status_code, content)


get_payment_instrument_groups_id_transaction_rules_error_mapper: Final[
    ErrorMapper[GetPaymentInstrumentGroupsIdTransactionRulesErrorBody]
] = _GetPaymentInstrumentGroupsIdTransactionRulesError()
