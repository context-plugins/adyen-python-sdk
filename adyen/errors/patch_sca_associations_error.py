from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.default_error_response_entity import DefaultErrorResponseEntity

PatchScaAssociationsErrorBody: TypeAlias = DefaultErrorResponseEntity | RawError


@dataclass(frozen=True, slots=True)
class _PatchScaAssociationsError:
    def map(self, response: HttpResponse) -> PatchScaAssociationsErrorBody:
        match response.status_code:
            case 401 | 403 | 500:
                return decode_json[DefaultErrorResponseEntity](response)
            case _:
                return RawError(response)


patch_sca_associations_error_mapper: Final[ErrorMapper[PatchScaAssociationsErrorBody]] = _PatchScaAssociationsError()
