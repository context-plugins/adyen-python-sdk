from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.default_error_response_entity import DefaultErrorResponseEntity

PostAuthCertificateErrorBody: TypeAlias = DefaultErrorResponseEntity | RawError


@dataclass(frozen=True, slots=True)
class _PostAuthCertificateError:
    def map(self, response: HttpResponse) -> PostAuthCertificateErrorBody:
        match response.status_code:
            case 400 | 401 | 422 | 500:
                return decode_json[DefaultErrorResponseEntity](response)
            case _:
                return RawError(response)


post_auth_certificate_error_mapper: Final[ErrorMapper[PostAuthCertificateErrorBody]] = _PostAuthCertificateError()
