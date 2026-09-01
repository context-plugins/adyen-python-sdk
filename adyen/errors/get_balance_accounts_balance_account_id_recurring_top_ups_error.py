from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.default_error_response_entity import DefaultErrorResponseEntity

GetBalanceAccountsBalanceAccountIdRecurringTopUpsErrorBody: TypeAlias = DefaultErrorResponseEntity | RawError


@dataclass(frozen=True, slots=True)
class _GetBalanceAccountsBalanceAccountIdRecurringTopUpsError:
    def map(self, response: HttpResponse) -> GetBalanceAccountsBalanceAccountIdRecurringTopUpsErrorBody:
        match response.status_code:
            case 401 | 403 | 404 | 500:
                return decode_json[DefaultErrorResponseEntity](response)
            case _:
                return RawError(response)


get_balance_accounts_balance_account_id_recurring_top_ups_error_mapper: Final[
    ErrorMapper[GetBalanceAccountsBalanceAccountIdRecurringTopUpsErrorBody]
] = _GetBalanceAccountsBalanceAccountIdRecurringTopUpsError()
