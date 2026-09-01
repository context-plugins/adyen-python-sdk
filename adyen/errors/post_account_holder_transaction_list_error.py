from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.service_error1 import ServiceError1

PostAccountHolderTransactionListErrorBody: TypeAlias = ServiceError1 | RawError


@dataclass(frozen=True, slots=True)
class _PostAccountHolderTransactionListError:
    def map(self, response: HttpResponse) -> PostAccountHolderTransactionListErrorBody:
        match response.status_code:
            case 400 | 401 | 403 | 422 | 500:
                return decode_json[ServiceError1](response)
            case _:
                return RawError(response)


post_account_holder_transaction_list_error_mapper: Final[
    ErrorMapper[PostAccountHolderTransactionListErrorBody]
] = _PostAccountHolderTransactionListError()
