from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.service_error import ServiceError

PostDonationsErrorBody: TypeAlias = ServiceError | RawError


@dataclass(frozen=True, slots=True)
class _PostDonationsError:
    def map(self, status_code: int, content: bytes) -> PostDonationsErrorBody:
        match status_code:
            case 400 | 401 | 403 | 422 | 500:
                return decode_json[ServiceError](content)
            case _:
                return RawError(status_code, content)


post_donations_error_mapper: Final[ErrorMapper[PostDonationsErrorBody]] = _PostDonationsError()
