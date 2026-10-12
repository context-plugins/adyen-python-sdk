from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.rest_service_error import RestServiceError

GetTransactionRulesTransactionRuleIdErrorBody: TypeAlias = RestServiceError | RawError


@dataclass(frozen=True, slots=True)
class _GetTransactionRulesTransactionRuleIdError:
    def map(self, status_code: int, content: bytes) -> GetTransactionRulesTransactionRuleIdErrorBody:
        match status_code:
            case 400 | 401 | 403 | 422 | 500:
                return decode_json[RestServiceError](content)
            case _:
                return RawError(status_code, content)


get_transaction_rules_transaction_rule_id_error_mapper: Final[
    ErrorMapper[GetTransactionRulesTransactionRuleIdErrorBody]
] = _GetTransactionRulesTransactionRuleIdError()
