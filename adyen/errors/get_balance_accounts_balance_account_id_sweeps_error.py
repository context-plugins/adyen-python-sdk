from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.rest_service_error import RestServiceError

GetBalanceAccountsBalanceAccountIdSweepsErrorBody: TypeAlias = RestServiceError | RawError


@dataclass(frozen=True, slots=True)
class _GetBalanceAccountsBalanceAccountIdSweepsError:
    def map(self, status_code: int, content: bytes) -> GetBalanceAccountsBalanceAccountIdSweepsErrorBody:
        match status_code:
            case 400 | 401 | 403 | 422 | 500:
                return decode_json[RestServiceError](content)
            case _:
                return RawError(status_code, content)


get_balance_accounts_balance_account_id_sweeps_error_mapper: Final[
    ErrorMapper[GetBalanceAccountsBalanceAccountIdSweepsErrorBody]
] = _GetBalanceAccountsBalanceAccountIdSweepsError()
