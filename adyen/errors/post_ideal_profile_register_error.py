from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.default_error_response_entity import DefaultErrorResponseEntity

PostIdealProfileRegisterErrorBody: TypeAlias = DefaultErrorResponseEntity | RawError


@dataclass(frozen=True, slots=True)
class _PostIdealProfileRegisterError:
    def map(self, response: HttpResponse) -> PostIdealProfileRegisterErrorBody:
        match response.status_code:
            case 400 | 422 | 500:
                return decode_json[DefaultErrorResponseEntity](response)
            case _:
                return RawError(response)


post_ideal_profile_register_error_mapper: Final[
    ErrorMapper[PostIdealProfileRegisterErrorBody]
] = _PostIdealProfileRegisterError()
