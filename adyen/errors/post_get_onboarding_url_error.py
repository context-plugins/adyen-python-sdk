from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.service_error1 import ServiceError1

PostGetOnboardingUrlErrorBody: TypeAlias = ServiceError1 | RawError


@dataclass(frozen=True, slots=True)
class _PostGetOnboardingUrlError:
    def map(self, status_code: int, content: bytes) -> PostGetOnboardingUrlErrorBody:
        match status_code:
            case 400 | 401 | 403 | 422 | 500:
                return decode_json[ServiceError1](content)
            case _:
                return RawError(status_code, content)


post_get_onboarding_url_error_mapper: Final[ErrorMapper[PostGetOnboardingUrlErrorBody]] = _PostGetOnboardingUrlError()
