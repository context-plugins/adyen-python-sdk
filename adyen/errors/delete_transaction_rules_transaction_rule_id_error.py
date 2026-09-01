from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.rest_service_error import RestServiceError

DeleteTransactionRulesTransactionRuleIdErrorBody: TypeAlias = RestServiceError | RawError


@dataclass(frozen=True, slots=True)
class _DeleteTransactionRulesTransactionRuleIdError:
    def map(self, response: HttpResponse) -> DeleteTransactionRulesTransactionRuleIdErrorBody:
        match response.status_code:
            case 400 | 401 | 403 | 422 | 500:
                return decode_json[RestServiceError](response)
            case _:
                return RawError(response)


delete_transaction_rules_transaction_rule_id_error_mapper: Final[
    ErrorMapper[DeleteTransactionRulesTransactionRuleIdErrorBody]
] = _DeleteTransactionRulesTransactionRuleIdError()
