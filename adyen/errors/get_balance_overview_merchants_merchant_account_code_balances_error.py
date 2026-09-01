from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.default_error_response_entity import DefaultErrorResponseEntity

GetBalanceOverviewMerchantsMerchantAccountCodeBalancesErrorBody: TypeAlias = DefaultErrorResponseEntity | RawError


@dataclass(frozen=True, slots=True)
class _GetBalanceOverviewMerchantsMerchantAccountCodeBalancesError:
    def map(self, response: HttpResponse) -> GetBalanceOverviewMerchantsMerchantAccountCodeBalancesErrorBody:
        match response.status_code:
            case 401 | 403 | 422:
                return decode_json[DefaultErrorResponseEntity](response)
            case _:
                return RawError(response)


get_balance_overview_merchants_merchant_account_code_balances_error_mapper: Final[
    ErrorMapper[GetBalanceOverviewMerchantsMerchantAccountCodeBalancesErrorBody]
] = _GetBalanceOverviewMerchantsMerchantAccountCodeBalancesError()
