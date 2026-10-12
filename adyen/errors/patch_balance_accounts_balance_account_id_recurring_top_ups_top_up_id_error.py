from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.default_error_response_entity import DefaultErrorResponseEntity

PatchBalanceAccountsBalanceAccountIdRecurringTopUpsTopUpIdErrorBody: TypeAlias = DefaultErrorResponseEntity | RawError


@dataclass(frozen=True, slots=True)
class _PatchBalanceAccountsBalanceAccountIdRecurringTopUpsTopUpIdError:
    def map(
        self, status_code: int, content: bytes
    ) -> PatchBalanceAccountsBalanceAccountIdRecurringTopUpsTopUpIdErrorBody:
        match status_code:
            case 400 | 401 | 403 | 422:
                return decode_json[DefaultErrorResponseEntity](content)
            case _:
                return RawError(status_code, content)


patch_balance_accounts_balance_account_id_recurring_top_ups_top_up_id_error_mapper: Final[
    ErrorMapper[PatchBalanceAccountsBalanceAccountIdRecurringTopUpsTopUpIdErrorBody]
] = _PatchBalanceAccountsBalanceAccountIdRecurringTopUpsTopUpIdError()
