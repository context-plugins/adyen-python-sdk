
# Three DS 2 Request Data 1

## Structure

`ThreeDS2RequestData1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `acct_info` | [`AcctInfo`](../../doc/models/acct-info.md) | Optional | Additional information about the cardholder’s account provided by the 3DS Requestor. |
| `acct_type` | [`AcctTypeEnum`](../../doc/models/acct-type-enum.md) | Optional | Indicates the type of account. For example, for a multi-account card product. Length: 2 characters. Allowed values:<br><br>* **01** — Not applicable<br>* **02** — Credit<br>* **03** — Debit<br><br>**Constraints**: *Minimum Length*: `2`, *Maximum Length*: `2` |
| `acquirer_bin` | `str` | Optional | Required for [authentication-only integration](https://docs.adyen.com/online-payments/3d-secure/other-3ds-flows/authentication-only). The acquiring BIN enrolled for 3D Secure 2. This string should match the value that you will use in the authorisation. Use 123456 on the Test platform. |
| `acquirer_merchant_id` | `str` | Optional | Required for [authentication-only integration](https://docs.adyen.com/online-payments/3d-secure/other-3ds-flows/authentication-only). The merchantId that is enrolled for 3D Secure 2 by the merchant's acquirer. This string should match the value that you will use in the authorisation. Use 123456 on the Test platform. |
| `addr_match` | [`AddrMatchEnum`](../../doc/models/addr-match-enum.md) | Optional | Indicates whether the cardholder shipping address and cardholder billing address are the same. Allowed values:<br><br>* **Y** — Shipping address matches billing address.<br>* **N** — Shipping address does not match billing address.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `1` |
| `authentication_only` | `bool` | Optional | If set to true, you will only perform the [3D Secure 2 authentication](https://docs.adyen.com/online-payments/3d-secure/other-3ds-flows/authentication-only), and not the payment authorisation.<br><br>**Default**: `False` |
| `challenge_indicator` | [`ChallengeIndicatorEnum`](../../doc/models/challenge-indicator-enum.md) | Optional | Possibility to specify a preference for receiving a challenge from the issuer.<br>Allowed values:<br><br>* `noPreference`<br>* `requestNoChallenge`<br>* `requestChallenge`<br>* `requestChallengeAsMandate` |
| `device_channel` | `str` | Required | The environment of the shopper.<br>Allowed values:<br><br>* `app`<br>* `browser` |
| `device_render_options` | [`DeviceRenderOptions`](../../doc/models/device-render-options.md) | Optional | Display options for the 3D Secure 2 SDK.<br>Optional and only for `deviceChannel` **app**. |
| `home_phone` | [`Phone`](../../doc/models/phone.md) | Optional | The home phone number provided by the cardholder. The phone number must consist of a country code, followed by the number. If the value you provide does not follow the guidelines, we do not submit it for authentication.<br><br>> Required for Visa and JCB transactions that require 3D Secure 2 authentication, if you did not include the `shopperEmail`, and did not send the shopper's phone number in `telephoneNumber`. |
| `mcc` | `str` | Optional | Required for merchants that have been enrolled for 3D Secure 2 by another party than Adyen, mostly [authentication-only integrations](https://docs.adyen.com/online-payments/3d-secure/other-3ds-flows/authentication-only). The `mcc` is a four-digit code with which the previously given `acquirerMerchantID` is registered at the scheme. |
| `merchant_name` | `str` | Optional | Required for [authentication-only integration](https://docs.adyen.com/online-payments/3d-secure/other-3ds-flows/authentication-only). The merchant name that the issuer presents to the shopper if they get a challenge. We recommend to use the same value that you will use in the authorization. Maximum length is 40 characters.<br><br>> Optional for a [full 3D Secure 2 integration](https://docs.adyen.com/online-payments/3d-secure/native-3ds2/api-integration). Use this field if you are enrolled for 3D Secure 2 with us and want to override the merchant name already configured on your account. |
| `message_version` | `str` | Optional | The `messageVersion` value indicating the 3D Secure 2 protocol version. |
| `mobile_phone` | [`Phone`](../../doc/models/phone.md) | Optional | The mobile phone number provided by the cardholder. The phone number must consist of a country code, followed by the number. If the value you provide does not follow the guidelines, we do not submit it for authentication.<br><br>> Required for Visa and JCB transactions that require 3D Secure 2 authentication, if you did not include the `shopperEmail`, and did not send the shopper's phone number in `telephoneNumber`. |
| `notification_url` | `str` | Optional | URL to where the issuer should send the `CRes`. Required if you are not using components for `channel` **Web** or if you are using classic integration `deviceChannel` **browser**. |
| `pay_token_ind` | `bool` | Optional | Value **true** indicates that the transaction was de-tokenised prior to being received by the ACS. |
| `payment_authentication_use_case` | `str` | Optional | Indicates the type of payment for which an authentication is requested (message extension) |
| `purchase_instal_data` | `str` | Optional | Indicates the maximum number of authorisations permitted for instalment payments. Length: 1–3 characters.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `3` |
| `recurring_expiry` | `str` | Optional | Date after which no further authorisations shall be performed. Format: YYYYMMDD |
| `recurring_frequency` | `str` | Optional | Indicates the minimum number of days between authorisations. Maximum length: 4 characters.<br><br>**Constraints**: *Maximum Length*: `4` |
| `sdk_app_id` | `str` | Optional | The `sdkAppID` value as received from the 3D Secure 2 SDK.<br>Required for `deviceChannel` set to **app**. |
| `sdk_enc_data` | `str` | Optional | The `sdkEncData` value as received from the 3D Secure 2 SDK.<br>Required for `deviceChannel` set to **app**. |
| `sdk_ephem_pub_key` | [`SDKEphemPubKey`](../../doc/models/sdk-ephem-pub-key.md) | Optional | The `sdkEphemPubKey` value as received from the 3D Secure 2 SDK.<br>Required for `deviceChannel` set to **app**. |
| `sdk_max_timeout` | `int` | Optional | The maximum amount of time in minutes for the 3D Secure 2 authentication process.<br>Optional and only for `deviceChannel` set to **app**. Defaults to **60** minutes.<br><br>**Default**: `60` |
| `sdk_reference_number` | `str` | Optional | The `sdkReferenceNumber` value as received from the 3D Secure 2 SDK.<br>Only for `deviceChannel` set to **app**. |
| `sdk_trans_id` | `str` | Optional | The `sdkTransID` value as received from the 3D Secure 2 SDK.<br>Only for `deviceChannel` set to **app**. |
| `sdk_version` | `str` | Optional | Version of the 3D Secure 2 mobile SDK.<br>Only for `deviceChannel` set to **app**. |
| `three_ds_comp_ind` | `str` | Optional | Completion indicator for the device fingerprinting. |
| `three_ds_requestor_authentication_ind` | `str` | Optional | Indicates the type of Authentication request. |
| `three_ds_requestor_authentication_info` | [`ThreeDSRequestorAuthenticationInfo`](../../doc/models/three-ds-requestor-authentication-info.md) | Optional | Information about how the 3DS Requestor authenticated the cardholder before or during the transaction |
| `three_ds_requestor_challenge_ind` | [`ThreeDSReqAuthMethodEnum`](../../doc/models/three-ds-req-auth-method-enum.md) | Optional | Indicates whether a challenge is requested for this transaction. Possible values:<br><br>* **01** — No preference<br>* **02** — No challenge requested<br>* **03** — Challenge requested (3DS Requestor preference)<br>* **04** — Challenge requested (Mandate)<br>* **05** — No challenge (transactional risk analysis is already performed)<br>* **06** — Data Only |
| `three_ds_requestor_id` | `str` | Optional | Required for [authentication-only integration](https://docs.adyen.com/online-payments/3d-secure/other-3ds-flows/authentication-only) for Visa. Unique 3D Secure requestor identifier assigned by the Directory Server when you enrol for 3D Secure 2. |
| `three_ds_requestor_name` | `str` | Optional | Required for [authentication-only integration](https://docs.adyen.com/online-payments/3d-secure/other-3ds-flows/authentication-only) for Visa. Unique 3D Secure requestor name assigned by the Directory Server when you enrol for 3D Secure 2. |
| `three_ds_requestor_prior_authentication_info` | [`ThreeDSRequestorPriorAuthenticationInfo`](../../doc/models/three-ds-requestor-prior-authentication-info.md) | Optional | Information about how the 3DS Requestor authenticated the cardholder as part of a previous 3DS transaction. |
| `three_ds_requestor_url` | `str` | Optional | URL of the (customer service) website that will be shown to the shopper in case of technical errors during the 3D Secure 2 process. |
| `trans_type` | [`TransTypeEnum`](../../doc/models/trans-type-enum.md) | Optional | Identifies the type of transaction being authenticated. Length: 2 characters. Allowed values:<br><br>* **01** — Goods/Service Purchase<br>* **03** — Check Acceptance<br>* **10** — Account Funding<br>* **11** — Quasi-Cash Transaction<br>* **28** — Prepaid Activation and Load<br><br>**Constraints**: *Minimum Length*: `2`, *Maximum Length*: `2` |
| `transaction_type` | [`TransactionTypeEnum`](../../doc/models/transaction-type-enum.md) | Optional | Identify the type of the transaction being authenticated. |
| `white_list_status` | `str` | Optional | The `whiteListStatus` value returned from a previous 3D Secure 2 transaction, only applicable for 3D Secure 2 protocol version 2.2.0. |
| `work_phone` | [`Phone`](../../doc/models/phone.md) | Optional | The work phone number provided by the cardholder. The phone number must consist of a country code, followed by the number. If the value you provide does not follow the guidelines, we do not submit it for authentication.<br><br>> Required for Visa and JCB transactions that require 3D Secure 2 authentication, if you did not include the `shopperEmail`, and did not send the shopper's phone number in `telephoneNumber`. |

## Example

```python
from adyen.models.acct_info import AcctInfo
from adyen.models.acct_type_enum import AcctTypeEnum
from adyen.models.addr_match_enum import AddrMatchEnum
from adyen.models.ch_acc_age_ind_enum import ChAccAgeIndEnum
from adyen.models.ch_acc_change_ind_enum import ChAccChangeIndEnum
from adyen.models.ch_acc_pw_change_ind_enum import ChAccPwChangeIndEnum
from adyen.models.three_ds_2_request_data_1 import ThreeDS2RequestData1

three_ds_2_request_data_1 = ThreeDS2RequestData1(
    device_channel='deviceChannel0',
    acct_info=AcctInfo(
        ch_acc_age_ind=ChAccAgeIndEnum.ENUM_05,
        ch_acc_change='chAccChange8',
        ch_acc_change_ind=ChAccChangeIndEnum.ENUM_01,
        ch_acc_pw_change='chAccPwChange8',
        ch_acc_pw_change_ind=ChAccPwChangeIndEnum.ENUM_03
    ),
    acct_type=AcctTypeEnum.ENUM_01,
    acquirer_bin='acquirerBIN8',
    acquirer_merchant_id='acquirerMerchantID6',
    addr_match=AddrMatchEnum.Y,
    authentication_only=False,
    sdk_max_timeout=60
)
```

