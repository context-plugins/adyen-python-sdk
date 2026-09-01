from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.default_error_response_entity import DefaultErrorResponseEntity

GetMerchantsMerchantAccountConnectedDevicesErrorBody: TypeAlias = DefaultErrorResponseEntity | RawError


@dataclass(frozen=True, slots=True)
class _GetMerchantsMerchantAccountConnectedDevicesError:
    def map(self, response: HttpResponse) -> GetMerchantsMerchantAccountConnectedDevicesErrorBody:
        match response.status_code:
            case 401 | 403:
                return decode_json[DefaultErrorResponseEntity](response)
            case _:
                return RawError(response)


get_merchants_merchant_account_connected_devices_error_mapper: Final[
    ErrorMapper[GetMerchantsMerchantAccountConnectedDevicesErrorBody]
] = _GetMerchantsMerchantAccountConnectedDevicesError()
