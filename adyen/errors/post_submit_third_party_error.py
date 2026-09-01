from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.service_error import ServiceError

PostSubmitThirdPartyErrorBody: TypeAlias = ServiceError | RawError


@dataclass(frozen=True, slots=True)
class _PostSubmitThirdPartyError:
    def map(self, response: HttpResponse) -> PostSubmitThirdPartyErrorBody:
        match response.status_code:
            case 400 | 401 | 403 | 422 | 500:
                return decode_json[ServiceError](response)
            case _:
                return RawError(response)


post_submit_third_party_error_mapper: Final[ErrorMapper[PostSubmitThirdPartyErrorBody]] = _PostSubmitThirdPartyError()
