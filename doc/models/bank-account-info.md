
# Bank Account Info

## Structure

`BankAccountInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_identification` | [AULocalAccountIdentification](../../doc/models/au-local-account-identification.md) \| [CALocalAccountIdentification](../../doc/models/ca-local-account-identification.md) \| [CZLocalAccountIdentification](../../doc/models/cz-local-account-identification.md) \| [DKLocalAccountIdentification](../../doc/models/dk-local-account-identification.md) \| [HKLocalAccountIdentification](../../doc/models/hk-local-account-identification.md) \| [HULocalAccountIdentification](../../doc/models/hu-local-account-identification.md) \| [IbanAccountIdentification](../../doc/models/iban-account-identification.md) \| [NOLocalAccountIdentification](../../doc/models/no-local-account-identification.md) \| [NZLocalAccountIdentification](../../doc/models/nz-local-account-identification.md) \| [NumberAndBicAccountIdentification](../../doc/models/number-and-bic-account-identification.md) \| [PLLocalAccountIdentification](../../doc/models/pl-local-account-identification.md) \| [SELocalAccountIdentification](../../doc/models/se-local-account-identification.md) \| [SGLocalAccountIdentification](../../doc/models/sg-local-account-identification.md) \| [UKLocalAccountIdentification](../../doc/models/uk-local-account-identification.md) \| [USLocalAccountIdentification](../../doc/models/us-local-account-identification.md) \| None | Optional | This is a container for one-of cases. |
| `account_type` | `str` | Optional | The type of bank account. |
| `bank_name` | `str` | Optional | The name of the banking institution where the bank account is held. |
| `country_code` | `str` | Optional | The two-character [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code where the bank account is registered. For example, **NL**. |
| `trusted_source` | `bool` | Optional, Read-only | Identifies if the bank account was created through [instant bank verification](https://docs.adyen.com/release-notes/platforms-and-financial-products#releaseNote=2023-05-08-hosted-onboarding). |

## Example

```python
from adyen.models.au_local_account_identification import AULocalAccountIdentification
from adyen.models.bank_account_info import BankAccountInfo

bank_account_info = BankAccountInfo(
    account_identification=AULocalAccountIdentification(
        account_number='accountNumber4',
        bsb_code='bsbCode8'
    ),
    account_type='accountType6',
    bank_name='bankName2',
    country_code='countryCode2'
)
```

