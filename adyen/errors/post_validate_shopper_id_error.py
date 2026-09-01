from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.checkout_error_response_entity import CheckoutErrorResponseEntity

PostValidateShopperIdErrorBody: TypeAlias = CheckoutErrorResponseEntity | RawError


@dataclass(frozen=True, slots=True)
class _PostValidateShopperIdError:
    def map(self, response: HttpResponse) -> PostValidateShopperIdErrorBody:
        match response.status_code:
            case 400 | 401 | 403 | 422 | 500:
                return decode_json[CheckoutErrorResponseEntity](response)
            case _:
                return RawError(response)


post_validate_shopper_id_error_mapper: Final[
    ErrorMapper[PostValidateShopperIdErrorBody]
] = _PostValidateShopperIdError()
