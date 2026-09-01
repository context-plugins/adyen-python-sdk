from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.service_error import ServiceError

PostVoidTransactionErrorBody: TypeAlias = ServiceError | RawError


@dataclass(frozen=True, slots=True)
class _PostVoidTransactionError:
    def map(self, response: HttpResponse) -> PostVoidTransactionErrorBody:
        match response.status_code:
            case 400 | 401 | 403 | 500:
                return decode_json[ServiceError](response)
            case _:
                return RawError(response)


post_void_transaction_error_mapper: Final[ErrorMapper[PostVoidTransactionErrorBody]] = _PostVoidTransactionError()
