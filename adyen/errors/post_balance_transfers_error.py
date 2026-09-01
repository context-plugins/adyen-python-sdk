from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.default_error_response_entity import DefaultErrorResponseEntity

PostBalanceTransfersErrorBody: TypeAlias = DefaultErrorResponseEntity | RawError


@dataclass(frozen=True, slots=True)
class _PostBalanceTransfersError:
    def map(self, response: HttpResponse) -> PostBalanceTransfersErrorBody:
        match response.status_code:
            case 401 | 422:
                return decode_json[DefaultErrorResponseEntity](response)
            case _:
                return RawError(response)


post_balance_transfers_error_mapper: Final[ErrorMapper[PostBalanceTransfersErrorBody]] = _PostBalanceTransfersError()
