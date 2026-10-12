from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.default_error_response_entity import DefaultErrorResponseEntity

DeleteScaAssociationsErrorBody: TypeAlias = DefaultErrorResponseEntity | RawError


@dataclass(frozen=True, slots=True)
class _DeleteScaAssociationsError:
    def map(self, status_code: int, content: bytes) -> DeleteScaAssociationsErrorBody:
        match status_code:
            case 401 | 403 | 500:
                return decode_json[DefaultErrorResponseEntity](content)
            case _:
                return RawError(status_code, content)


delete_sca_associations_error_mapper: Final[ErrorMapper[DeleteScaAssociationsErrorBody]] = _DeleteScaAssociationsError()
