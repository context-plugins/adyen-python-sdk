from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.default_error_response_entity import DefaultErrorResponseEntity

PostBalancePlatformsIdTransferLimitsErrorBody: TypeAlias = DefaultErrorResponseEntity | RawError


@dataclass(frozen=True, slots=True)
class _PostBalancePlatformsIdTransferLimitsError:
    def map(self, response: HttpResponse) -> PostBalancePlatformsIdTransferLimitsErrorBody:
        match response.status_code:
            case 404 | 422:
                return decode_json[DefaultErrorResponseEntity](response)
            case _:
                return RawError(response)


post_balance_platforms_id_transfer_limits_error_mapper: Final[
    ErrorMapper[PostBalancePlatformsIdTransferLimitsErrorBody]
] = _PostBalancePlatformsIdTransferLimitsError()
