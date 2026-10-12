from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.default_error_response_entity import DefaultErrorResponseEntity

GetBalanceAccountsIdTransferLimitsTransferLimitIdErrorBody: TypeAlias = DefaultErrorResponseEntity | RawError


@dataclass(frozen=True, slots=True)
class _GetBalanceAccountsIdTransferLimitsTransferLimitIdError:
    def map(self, status_code: int, content: bytes) -> GetBalanceAccountsIdTransferLimitsTransferLimitIdErrorBody:
        match status_code:
            case 404 | 422:
                return decode_json[DefaultErrorResponseEntity](content)
            case _:
                return RawError(status_code, content)


get_balance_accounts_id_transfer_limits_transfer_limit_id_error_mapper: Final[
    ErrorMapper[GetBalanceAccountsIdTransferLimitsTransferLimitIdErrorBody]
] = _GetBalanceAccountsIdTransferLimitsTransferLimitIdError()
