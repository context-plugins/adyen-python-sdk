from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.default_error_response_entity import DefaultErrorResponseEntity

GetBalanceAccountsBalanceAccountIdPayoutSchedulesIdExecutionsErrorBody: TypeAlias = (
    DefaultErrorResponseEntity | RawError
)


@dataclass(frozen=True, slots=True)
class _GetBalanceAccountsBalanceAccountIdPayoutSchedulesIdExecutionsError:
    def map(self, response: HttpResponse) -> GetBalanceAccountsBalanceAccountIdPayoutSchedulesIdExecutionsErrorBody:
        match response.status_code:
            case 401 | 403 | 404 | 422 | 500:
                return decode_json[DefaultErrorResponseEntity](response)
            case _:
                return RawError(response)


get_balance_accounts_balance_account_id_payout_schedules_id_executions_error_mapper: Final[
    ErrorMapper[GetBalanceAccountsBalanceAccountIdPayoutSchedulesIdExecutionsErrorBody]
] = _GetBalanceAccountsBalanceAccountIdPayoutSchedulesIdExecutionsError()
