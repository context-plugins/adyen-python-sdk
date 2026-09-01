from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.service_error import ServiceError

PostStoreDetailErrorBody: TypeAlias = ServiceError | RawError


@dataclass(frozen=True, slots=True)
class _PostStoreDetailError:
    def map(self, response: HttpResponse) -> PostStoreDetailErrorBody:
        match response.status_code:
            case 400 | 401 | 403 | 422 | 500:
                return decode_json[ServiceError](response)
            case _:
                return RawError(response)


post_store_detail_error_mapper: Final[ErrorMapper[PostStoreDetailErrorBody]] = _PostStoreDetailError()
