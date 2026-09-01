from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.service_error import ServiceError

PatchPaymentLinksLinkIdErrorBody: TypeAlias = ServiceError | RawError


@dataclass(frozen=True, slots=True)
class _PatchPaymentLinksLinkIdError:
    def map(self, response: HttpResponse) -> PatchPaymentLinksLinkIdErrorBody:
        match response.status_code:
            case 400 | 401 | 403 | 422 | 500:
                return decode_json[ServiceError](response)
            case _:
                return RawError(response)


patch_payment_links_link_id_error_mapper: Final[
    ErrorMapper[PatchPaymentLinksLinkIdErrorBody]
] = _PatchPaymentLinksLinkIdError()
