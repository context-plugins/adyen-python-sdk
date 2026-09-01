from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.rest_service_error import RestServiceError

PostRegisteredDevicesDeviceIdAssociationsErrorBody: TypeAlias = RestServiceError | RawError


@dataclass(frozen=True, slots=True)
class _PostRegisteredDevicesDeviceIdAssociationsError:
    def map(self, response: HttpResponse) -> PostRegisteredDevicesDeviceIdAssociationsErrorBody:
        match response.status_code:
            case 400 | 401 | 403 | 422 | 500:
                return decode_json[RestServiceError](response)
            case _:
                return RawError(response)


post_registered_devices_device_id_associations_error_mapper: Final[
    ErrorMapper[PostRegisteredDevicesDeviceIdAssociationsErrorBody]
] = _PostRegisteredDevicesDeviceIdAssociationsError()
