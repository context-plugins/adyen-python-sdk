from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.service_error import ServiceError

GetPaymentLinksLinkIdErrorBody: TypeAlias = ServiceError | RawError


@dataclass(frozen=True, slots=True)
class _GetPaymentLinksLinkIdError:
    def map(self, status_code: int, content: bytes) -> GetPaymentLinksLinkIdErrorBody:
        match status_code:
            case 400 | 401 | 403 | 422 | 500:
                return decode_json[ServiceError](content)
            case _:
                return RawError(status_code, content)


get_payment_links_link_id_error_mapper: Final[
    ErrorMapper[GetPaymentLinksLinkIdErrorBody]
] = _GetPaymentLinksLinkIdError()
