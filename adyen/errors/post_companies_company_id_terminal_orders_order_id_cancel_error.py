from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.rest_service_error import RestServiceError

PostCompaniesCompanyIdTerminalOrdersOrderIdCancelErrorBody: TypeAlias = RestServiceError | RawError


@dataclass(frozen=True, slots=True)
class _PostCompaniesCompanyIdTerminalOrdersOrderIdCancelError:
    def map(self, response: HttpResponse) -> PostCompaniesCompanyIdTerminalOrdersOrderIdCancelErrorBody:
        match response.status_code:
            case 400 | 401 | 403 | 422 | 500:
                return decode_json[RestServiceError](response)
            case _:
                return RawError(response)


post_companies_company_id_terminal_orders_order_id_cancel_error_mapper: Final[
    ErrorMapper[PostCompaniesCompanyIdTerminalOrdersOrderIdCancelErrorBody]
] = _PostCompaniesCompanyIdTerminalOrdersOrderIdCancelError()
