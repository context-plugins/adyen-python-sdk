from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.service_error1 import ServiceError1

PostCloseAccountHolderErrorBody: TypeAlias = ServiceError1 | RawError


@dataclass(frozen=True, slots=True)
class _PostCloseAccountHolderError:
    def map(self, response: HttpResponse) -> PostCloseAccountHolderErrorBody:
        match response.status_code:
            case 400 | 401 | 403 | 422 | 500:
                return decode_json[ServiceError1](response)
            case _:
                return RawError(response)


post_close_account_holder_error_mapper: Final[
    ErrorMapper[PostCloseAccountHolderErrorBody]
] = _PostCloseAccountHolderError()
