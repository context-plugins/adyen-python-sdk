from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.rest_service_error import RestServiceError

PostPinsRevealErrorBody: TypeAlias = RestServiceError | RawError


@dataclass(frozen=True, slots=True)
class _PostPinsRevealError:
    def map(self, status_code: int, content: bytes) -> PostPinsRevealErrorBody:
        match status_code:
            case 401 | 403 | 422 | 500:
                return decode_json[RestServiceError](content)
            case _:
                return RawError(status_code, content)


post_pins_reveal_error_mapper: Final[ErrorMapper[PostPinsRevealErrorBody]] = _PostPinsRevealError()
