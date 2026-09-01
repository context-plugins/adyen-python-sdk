from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.default_error_response_entity import DefaultErrorResponseEntity

GetBalanceAccountsIdTransferLimitsErrorBody: TypeAlias = DefaultErrorResponseEntity | RawError


@dataclass(frozen=True, slots=True)
class _GetBalanceAccountsIdTransferLimitsError:
    def map(self, response: HttpResponse) -> GetBalanceAccountsIdTransferLimitsErrorBody:
        match response.status_code:
            case 404 | 422:
                return decode_json[DefaultErrorResponseEntity](response)
            case _:
                return RawError(response)


get_balance_accounts_id_transfer_limits_error_mapper: Final[
    ErrorMapper[GetBalanceAccountsIdTransferLimitsErrorBody]
] = _GetBalanceAccountsIdTransferLimitsError()
