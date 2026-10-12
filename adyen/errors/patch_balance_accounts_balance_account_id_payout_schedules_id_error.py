from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.default_error_response_entity import DefaultErrorResponseEntity

PatchBalanceAccountsBalanceAccountIdPayoutSchedulesIdErrorBody: TypeAlias = DefaultErrorResponseEntity | RawError


@dataclass(frozen=True, slots=True)
class _PatchBalanceAccountsBalanceAccountIdPayoutSchedulesIdError:
    def map(self, status_code: int, content: bytes) -> PatchBalanceAccountsBalanceAccountIdPayoutSchedulesIdErrorBody:
        match status_code:
            case 401 | 403 | 404 | 422 | 500:
                return decode_json[DefaultErrorResponseEntity](content)
            case _:
                return RawError(status_code, content)


patch_balance_accounts_balance_account_id_payout_schedules_id_error_mapper: Final[
    ErrorMapper[PatchBalanceAccountsBalanceAccountIdPayoutSchedulesIdErrorBody]
] = _PatchBalanceAccountsBalanceAccountIdPayoutSchedulesIdError()
