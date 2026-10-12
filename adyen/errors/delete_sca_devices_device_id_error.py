from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.default_error_response_entity import DefaultErrorResponseEntity

DeleteScaDevicesDeviceIdErrorBody: TypeAlias = DefaultErrorResponseEntity | RawError


@dataclass(frozen=True, slots=True)
class _DeleteScaDevicesDeviceIdError:
    def map(self, status_code: int, content: bytes) -> DeleteScaDevicesDeviceIdErrorBody:
        match status_code:
            case 400 | 401 | 403 | 404 | 422 | 500:
                return decode_json[DefaultErrorResponseEntity](content)
            case _:
                return RawError(status_code, content)


delete_sca_devices_device_id_error_mapper: Final[
    ErrorMapper[DeleteScaDevicesDeviceIdErrorBody]
] = _DeleteScaDevicesDeviceIdError()
