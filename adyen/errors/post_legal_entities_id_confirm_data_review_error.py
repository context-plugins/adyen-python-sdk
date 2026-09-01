from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.service_error1 import ServiceError1

PostLegalEntitiesIdConfirmDataReviewErrorBody: TypeAlias = ServiceError1 | RawError


@dataclass(frozen=True, slots=True)
class _PostLegalEntitiesIdConfirmDataReviewError:
    def map(self, response: HttpResponse) -> PostLegalEntitiesIdConfirmDataReviewErrorBody:
        match response.status_code:
            case 400 | 401 | 403 | 422 | 500:
                return decode_json[ServiceError1](response)
            case _:
                return RawError(response)


post_legal_entities_id_confirm_data_review_error_mapper: Final[
    ErrorMapper[PostLegalEntitiesIdConfirmDataReviewErrorBody]
] = _PostLegalEntitiesIdConfirmDataReviewError()
