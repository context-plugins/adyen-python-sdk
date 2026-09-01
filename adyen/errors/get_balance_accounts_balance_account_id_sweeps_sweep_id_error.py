from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.rest_service_error import RestServiceError

GetBalanceAccountsBalanceAccountIdSweepsSweepIdErrorBody: TypeAlias = RestServiceError | RawError


@dataclass(frozen=True, slots=True)
class _GetBalanceAccountsBalanceAccountIdSweepsSweepIdError:
    def map(self, response: HttpResponse) -> GetBalanceAccountsBalanceAccountIdSweepsSweepIdErrorBody:
        match response.status_code:
            case 400 | 401 | 403 | 422 | 500:
                return decode_json[RestServiceError](response)
            case _:
                return RawError(response)


get_balance_accounts_balance_account_id_sweeps_sweep_id_error_mapper: Final[
    ErrorMapper[GetBalanceAccountsBalanceAccountIdSweepsSweepIdErrorBody]
] = _GetBalanceAccountsBalanceAccountIdSweepsSweepIdError()
