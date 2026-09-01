from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.default_error_response_entity import DefaultErrorResponseEntity

PatchScaDevicesDeviceIdErrorBody: TypeAlias = DefaultErrorResponseEntity | RawError


@dataclass(frozen=True, slots=True)
class _PatchScaDevicesDeviceIdError:
    def map(self, response: HttpResponse) -> PatchScaDevicesDeviceIdErrorBody:
        match response.status_code:
            case 400 | 401 | 403 | 404 | 422 | 500:
                return decode_json[DefaultErrorResponseEntity](response)
            case _:
                return RawError(response)


patch_sca_devices_device_id_error_mapper: Final[
    ErrorMapper[PatchScaDevicesDeviceIdErrorBody]
] = _PatchScaDevicesDeviceIdError()
