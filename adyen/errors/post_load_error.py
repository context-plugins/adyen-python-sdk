from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.service_error import ServiceError

PostLoadErrorBody: TypeAlias = ServiceError | RawError


@dataclass(frozen=True, slots=True)
class _PostLoadError:
    def map(self, response: HttpResponse) -> PostLoadErrorBody:
        match response.status_code:
            case 400 | 401 | 403 | 500:
                return decode_json[ServiceError](response)
            case _:
                return RawError(response)


post_load_error_mapper: Final[ErrorMapper[PostLoadErrorBody]] = _PostLoadError()
