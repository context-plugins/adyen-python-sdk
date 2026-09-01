from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.service_error import ServiceError

PostMergeBalanceErrorBody: TypeAlias = ServiceError | RawError


@dataclass(frozen=True, slots=True)
class _PostMergeBalanceError:
    def map(self, response: HttpResponse) -> PostMergeBalanceErrorBody:
        match response.status_code:
            case 400 | 401 | 403 | 500:
                return decode_json[ServiceError](response)
            case _:
                return RawError(response)


post_merge_balance_error_mapper: Final[ErrorMapper[PostMergeBalanceErrorBody]] = _PostMergeBalanceError()
