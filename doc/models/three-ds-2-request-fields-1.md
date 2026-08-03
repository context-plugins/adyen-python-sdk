
# Three Ds 2 Request Fields 1

Request fields for 3D Secure 2. To check if any of the following fields are required for your integration, refer to [Online payments](https://docs.adyen.com/online-payments) or [Classic integration](https://docs.adyen.com/classic-integration) documentation.

*This model accepts additional fields of type Any.*

## Structure

`ThreeDs2RequestFields1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `acct_info` | [`AcctInfo1`](../../doc/models/acct-info-1.md) | Optional | - |
| `acct_type` | [`AcctType`](../../doc/models/acct-type.md) | Optional | **Constraints**: *Minimum Length*: `2`, *Maximum Length*: `2` |
| `acquirer_bin` | `str` | Optional | Required for [authentication-only integration](https://docs.adyen.com/online-payments/3d-secure/other-3ds-flows/authentication-only). The acquiring BIN enrolled for 3D Secure 2. This string should match the value that you will use in the authorisation. Use 123456 on the Test platform. |
| `acquirer_merchant_id` | `str` | Optional | Required for [authentication-only integration](https://docs.adyen.com/online-payments/3d-secure/other-3ds-flows/authentication-only). The merchantId that is enrolled for 3D Secure 2 by the merchant's acquirer. This string should match the value that you will use in the authorisation. Use 123456 on the Test platform. |
| `addr_match` | [`AddrMatch1`](../../doc/models/addr-match-1.md) | Optional | **Constraints**: *Minimum Length*: `1`, *Maximum Length*: `1` |
| `authentication_only` | `bool` | Optional | If set to true, you will only perform the [3D Secure 2 authentication](https://docs.adyen.com/online-payments/3d-secure/other-3ds-flows/authentication-only), and not the payment authorisation.<br><br>**Default**: `False` |
| `challenge_indicator` | [`ChallengeIndicator`](../../doc/models/challenge-indicator.md) | Optional | - |
| `device_render_options` | [`DeviceRenderOptions2`](../../doc/models/device-render-options-2.md) | Optional | - |
| `home_phone` | [`HomePhone`](../../doc/models/home-phone.md) | Optional | - |
| `mcc` | `str` | Optional | Required for merchants that have been enrolled for 3D Secure 2 by another party than Adyen, mostly [authentication-only integrations](https://docs.adyen.com/online-payments/3d-secure/other-3ds-flows/authentication-only). The `mcc` is a four-digit code with which the previously given `acquirerMerchantID` is registered at the scheme. |
| `merchant_name` | `str` | Optional | Required for [authentication-only integration](https://docs.adyen.com/online-payments/3d-secure/other-3ds-flows/authentication-only). The merchant name that the issuer presents to the shopper if they get a challenge. We recommend to use the same value that you will use in the authorization. Maximum length is 40 characters.<br><br>> Optional for a [full 3D Secure 2 integration](https://docs.adyen.com/online-payments/3d-secure/native-3ds2/api-integration). Use this field if you are enrolled for 3D Secure 2 with us and want to override the merchant name already configured on your account. |
| `message_version` | `str` | Optional | The `messageVersion` value indicating the 3D Secure 2 protocol version. |
| `mobile_phone` | [`MobilePhone`](../../doc/models/mobile-phone.md) | Optional | - |
| `notification_url` | `str` | Optional | URL to where the issuer should send the `CRes`. Required if you are not using components for `channel` **Web** or if you are using classic integration `deviceChannel` **browser**. |
| `pay_token_ind` | `bool` | Optional | Value **true** indicates that the transaction was de-tokenised prior to being received by the ACS. |
| `payment_authentication_use_case` | `str` | Optional | Indicates the type of payment for which an authentication is requested (message extension) |
| `purchase_instal_data` | `str` | Optional | Indicates the maximum number of authorisations permitted for instalment payments. Length: 1–3 characters.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `3` |
| `recurring_expiry` | `str` | Optional | Date after which no further authorisations shall be performed. Format: YYYYMMDD |
| `recurring_frequency` | `str` | Optional | Indicates the minimum number of days between authorisations. Maximum length: 4 characters.<br><br>**Constraints**: *Maximum Length*: `4` |
| `sdk_app_id` | `str` | Optional | The `sdkAppID` value as received from the 3D Secure 2 SDK. |
| `sdk_ephem_pub_key` | [`SdkEphemPubKey3`](../../doc/models/sdk-ephem-pub-key-3.md) | Optional | - |
| `sdk_max_timeout` | `int` | Optional | The maximum amount of time in minutes for the 3D Secure 2 authentication process.<br>Optional and only for `deviceChannel` set to **app**. Defaults to **60** minutes.<br><br>**Default**: `60` |
| `sdk_reference_number` | `str` | Optional | The `sdkReferenceNumber` value as received from the 3D Secure 2 SDK. |
| `sdk_trans_id` | `str` | Optional | The `sdkTransID` value as received from the 3D Secure 2 SDK. |
| `three_ds_comp_ind` | `str` | Optional | Completion indicator for the device fingerprinting. |
| `three_ds_requestor_authentication_ind` | `str` | Optional | Indicates the type of Authentication request. |
| `three_ds_requestor_authentication_info` | [`ThreeDsRequestorAuthenticationInfo1`](../../doc/models/three-ds-requestor-authentication-info-1.md) | Optional | - |
| `three_ds_requestor_challenge_ind` | [`ThreeDsRequestorChallengeInd`](../../doc/models/three-ds-requestor-challenge-ind.md) | Optional | - |
| `three_ds_requestor_id` | `str` | Optional | Required for [authentication-only integration](https://docs.adyen.com/online-payments/3d-secure/other-3ds-flows/authentication-only) for Visa. Unique 3D Secure requestor identifier assigned by the Directory Server when you enrol for 3D Secure 2. |
| `three_ds_requestor_name` | `str` | Optional | Required for [authentication-only integration](https://docs.adyen.com/online-payments/3d-secure/other-3ds-flows/authentication-only) for Visa. Unique 3D Secure requestor name assigned by the Directory Server when you enrol for 3D Secure 2. |
| `three_ds_requestor_prior_authentication_info` | [`ThreeDsRequestorPriorAuthenticationInfo1`](../../doc/models/three-ds-requestor-prior-authentication-info-1.md) | Optional | - |
| `three_ds_requestor_url` | `str` | Optional | URL of the (customer service) website that will be shown to the shopper in case of technical errors during the 3D Secure 2 process. |
| `trans_type` | [`TransType`](../../doc/models/trans-type.md) | Optional | **Constraints**: *Minimum Length*: `2`, *Maximum Length*: `2` |
| `transaction_type` | [`TransactionType`](../../doc/models/transaction-type.md) | Optional | - |
| `white_list_status` | `str` | Optional | The `whiteListStatus` value returned from a previous 3D Secure 2 transaction, only applicable for 3D Secure 2 protocol version 2.2.0. |
| `work_phone` | [`WorkPhone`](../../doc/models/work-phone.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.acct_info_1 import AcctInfo1
from adyen.models.acct_type import AcctType
from adyen.models.addr_match_1 import AddrMatch1
from adyen.models.ch_acc_age_ind import ChAccAgeInd
from adyen.models.ch_acc_change_ind import ChAccChangeInd
from adyen.models.ch_acc_pw_change_ind import ChAccPwChangeInd
from adyen.models.three_ds_2_request_fields_1 import ThreeDs2RequestFields1

three_ds_2_request_fields_1 = ThreeDs2RequestFields1(
    acct_info=AcctInfo1(
        ch_acc_age_ind=ChAccAgeInd.ENUM_05,
        ch_acc_change='chAccChange8',
        ch_acc_change_ind=ChAccChangeInd.ENUM_01,
        ch_acc_pw_change='chAccPwChange8',
        ch_acc_pw_change_ind=ChAccPwChangeInd.ENUM_03,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    acct_type=AcctType.ENUM_02,
    acquirer_bin='acquirerBIN0',
    acquirer_merchant_id='acquirerMerchantID8',
    addr_match=AddrMatch1.Y,
    authentication_only=False,
    sdk_max_timeout=60,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

