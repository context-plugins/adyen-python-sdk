from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.service_error1 import ServiceError1

PostTestNotificationConfigurationErrorBody: TypeAlias = ServiceError1 | RawError


@dataclass(frozen=True, slots=True)
class _PostTestNotificationConfigurationError:
    def map(self, response: HttpResponse) -> PostTestNotificationConfigurationErrorBody:
        match response.status_code:
            case 400 | 401 | 403 | 422 | 500:
                return decode_json[ServiceError1](response)
            case _:
                return RawError(response)


post_test_notification_configuration_error_mapper: Final[
    ErrorMapper[PostTestNotificationConfigurationErrorBody]
] = _PostTestNotificationConfigurationError()
