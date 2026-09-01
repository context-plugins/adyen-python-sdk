from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.default_error_response_entity import DefaultErrorResponseEntity

DeleteBalanceAccountsBalanceAccountIdRecurringTopUpsTopUpIdErrorBody: TypeAlias = DefaultErrorResponseEntity | RawError


@dataclass(frozen=True, slots=True)
class _DeleteBalanceAccountsBalanceAccountIdRecurringTopUpsTopUpIdError:
    def map(self, response: HttpResponse) -> DeleteBalanceAccountsBalanceAccountIdRecurringTopUpsTopUpIdErrorBody:
        match response.status_code:
            case 400 | 401 | 403 | 404 | 422 | 500:
                return decode_json[DefaultErrorResponseEntity](response)
            case _:
                return RawError(response)


delete_balance_accounts_balance_account_id_recurring_top_ups_top_up_id_error_mapper: Final[
    ErrorMapper[DeleteBalanceAccountsBalanceAccountIdRecurringTopUpsTopUpIdErrorBody]
] = _DeleteBalanceAccountsBalanceAccountIdRecurringTopUpsTopUpIdError()
