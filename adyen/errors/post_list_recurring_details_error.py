from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.service_error import ServiceError

PostListRecurringDetailsErrorBody: TypeAlias = ServiceError | RawError


@dataclass(frozen=True, slots=True)
class _PostListRecurringDetailsError:
    def map(self, response: HttpResponse) -> PostListRecurringDetailsErrorBody:
        match response.status_code:
            case 400 | 401 | 403 | 422 | 500:
                return decode_json[ServiceError](response)
            case _:
                return RawError(response)


post_list_recurring_details_error_mapper: Final[
    ErrorMapper[PostListRecurringDetailsErrorBody]
] = _PostListRecurringDetailsError()
