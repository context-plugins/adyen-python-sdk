from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.default_error_response_entity import DefaultErrorResponseEntity

PatchMandatesMandateIdErrorBody: TypeAlias = DefaultErrorResponseEntity | RawError


@dataclass(frozen=True, slots=True)
class _PatchMandatesMandateIdError:
    def map(self, response: HttpResponse) -> PatchMandatesMandateIdErrorBody:
        match response.status_code:
            case 401 | 403 | 404 | 422 | 500:
                return decode_json[DefaultErrorResponseEntity](response)
            case _:
                return RawError(response)


patch_mandates_mandate_id_error_mapper: Final[
    ErrorMapper[PatchMandatesMandateIdErrorBody]
] = _PatchMandatesMandateIdError()
