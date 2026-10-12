from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.default_error_response_entity import DefaultErrorResponseEntity

PostAuthCertificateErrorBody: TypeAlias = DefaultErrorResponseEntity | RawError


@dataclass(frozen=True, slots=True)
class _PostAuthCertificateError:
    def map(self, status_code: int, content: bytes) -> PostAuthCertificateErrorBody:
        match status_code:
            case 400 | 401 | 422 | 500:
                return decode_json[DefaultErrorResponseEntity](content)
            case _:
                return RawError(status_code, content)


post_auth_certificate_error_mapper: Final[ErrorMapper[PostAuthCertificateErrorBody]] = _PostAuthCertificateError()
