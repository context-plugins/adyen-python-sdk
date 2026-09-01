from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.default_error_response_entity import DefaultErrorResponseEntity

DeleteScaDevicesDeviceIdErrorBody: TypeAlias = DefaultErrorResponseEntity | RawError


@dataclass(frozen=True, slots=True)
class _DeleteScaDevicesDeviceIdError:
    def map(self, response: HttpResponse) -> DeleteScaDevicesDeviceIdErrorBody:
        match response.status_code:
            case 400 | 401 | 403 | 404 | 422 | 500:
                return decode_json[DefaultErrorResponseEntity](response)
            case _:
                return RawError(response)


delete_sca_devices_device_id_error_mapper: Final[
    ErrorMapper[DeleteScaDevicesDeviceIdErrorBody]
] = _DeleteScaDevicesDeviceIdError()
