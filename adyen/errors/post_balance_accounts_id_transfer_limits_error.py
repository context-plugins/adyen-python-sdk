from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.default_error_response_entity import DefaultErrorResponseEntity

PostBalanceAccountsIdTransferLimitsErrorBody: TypeAlias = DefaultErrorResponseEntity | RawError


@dataclass(frozen=True, slots=True)
class _PostBalanceAccountsIdTransferLimitsError:
    def map(self, response: HttpResponse) -> PostBalanceAccountsIdTransferLimitsErrorBody:
        match response.status_code:
            case 400 | 401 | 422:
                return decode_json[DefaultErrorResponseEntity](response)
            case _:
                return RawError(response)


post_balance_accounts_id_transfer_limits_error_mapper: Final[
    ErrorMapper[PostBalanceAccountsIdTransferLimitsErrorBody]
] = _PostBalanceAccountsIdTransferLimitsError()
