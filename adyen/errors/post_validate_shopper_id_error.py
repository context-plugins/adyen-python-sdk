from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.checkout_error_response_entity import CheckoutErrorResponseEntity

PostValidateShopperIdErrorBody: TypeAlias = CheckoutErrorResponseEntity | RawError


@dataclass(frozen=True, slots=True)
class _PostValidateShopperIdError:
    def map(self, status_code: int, content: bytes) -> PostValidateShopperIdErrorBody:
        match status_code:
            case 400 | 401 | 403 | 422 | 500:
                return decode_json[CheckoutErrorResponseEntity](content)
            case _:
                return RawError(status_code, content)


post_validate_shopper_id_error_mapper: Final[
    ErrorMapper[PostValidateShopperIdErrorBody]
] = _PostValidateShopperIdError()
