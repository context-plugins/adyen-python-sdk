from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.default_error_response_entity import DefaultErrorResponseEntity

GetBalancePlatformsIdTransferLimitsTransferLimitIdErrorBody: TypeAlias = DefaultErrorResponseEntity | RawError


@dataclass(frozen=True, slots=True)
class _GetBalancePlatformsIdTransferLimitsTransferLimitIdError:
    def map(self, response: HttpResponse) -> GetBalancePlatformsIdTransferLimitsTransferLimitIdErrorBody:
        match response.status_code:
            case 404 | 422:
                return decode_json[DefaultErrorResponseEntity](response)
            case _:
                return RawError(response)


get_balance_platforms_id_transfer_limits_transfer_limit_id_error_mapper: Final[
    ErrorMapper[GetBalancePlatformsIdTransferLimitsTransferLimitIdErrorBody]
] = _GetBalancePlatformsIdTransferLimitsTransferLimitIdError()
