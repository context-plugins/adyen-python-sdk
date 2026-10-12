from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.default_error_response_entity import DefaultErrorResponseEntity

PostScaDevicesErrorBody: TypeAlias = DefaultErrorResponseEntity | RawError


@dataclass(frozen=True, slots=True)
class _PostScaDevicesError:
    def map(self, status_code: int, content: bytes) -> PostScaDevicesErrorBody:
        match status_code:
            case 400 | 401 | 403 | 422 | 500:
                return decode_json[DefaultErrorResponseEntity](content)
            case _:
                return RawError(status_code, content)


post_sca_devices_error_mapper: Final[ErrorMapper[PostScaDevicesErrorBody]] = _PostScaDevicesError()
