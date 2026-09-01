from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.rest_service_error import RestServiceError

DeleteBalanceAccountsBalanceAccountIdSweepsSweepIdErrorBody: TypeAlias = RestServiceError | RawError


@dataclass(frozen=True, slots=True)
class _DeleteBalanceAccountsBalanceAccountIdSweepsSweepIdError:
    def map(self, response: HttpResponse) -> DeleteBalanceAccountsBalanceAccountIdSweepsSweepIdErrorBody:
        match response.status_code:
            case 400 | 401 | 403 | 422 | 500:
                return decode_json[RestServiceError](response)
            case _:
                return RawError(response)


delete_balance_accounts_balance_account_id_sweeps_sweep_id_error_mapper: Final[
    ErrorMapper[DeleteBalanceAccountsBalanceAccountIdSweepsSweepIdErrorBody]
] = _DeleteBalanceAccountsBalanceAccountIdSweepsSweepIdError()
