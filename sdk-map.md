<!-- Generated file — do not edit; regenerated with the SDK. -->

# SDK map — Adyen (Python)

> A generated table of contents for this SDK. Consult this map and its sub-pages to learn signatures, error types, and server/auth wiring **by lookup**. Model shapes and enum values are *not* duplicated here — the map names the module declaring each type; read the shape there. Every name is the emitted spelling, so a wrong one fails at import rather than working silently.

|  |  |
| --- | --- |
| SDK display name | Adyen |
| Root package | `adyen` |
| Distribution name | `adyen` |
| Requires | Python 3.10 or later |
| API spec version | `72` |
| Generator | APIMatic |

Staleness check: the API spec version above changes when the SDK is regenerated from a new spec, and the package version is what `pip show` reports for the installed SDK. If a lookup here fails at import, re-read the module named in the row.

All `Source` paths on this map and its sub-pages are relative to the **SDK root** — the directory holding this file and `pyproject.toml` — never to the page that carries them. Open them as-is from the SDK root; if the SDK sits under a subdirectory of a larger repo, prefix that subdirectory.

---

## Getting a client

### Synchronous client

```python
from adyen import AdyenClient
from adyen.core import BasicAuthCredentials

client = AdyenClient(
    api_key_auth="YOUR_API_KEY",
    basic_auth=BasicAuthCredentials(username="YOUR_USERNAME", password="YOUR_PASSWORD"),
    client_key="YOUR_API_KEY",
)

# TODO: call endpoints here -- see api-reference.md

client.close()
```

Alternatively, scope it — `with AdyenClient(...) as client:` closes the pool on exit.

### Asynchronous client

```python
from asyncio import run

from adyen import AsyncAdyenClient
from adyen.core import BasicAuthCredentials


async def main() -> None:
    client = AsyncAdyenClient(
        api_key_auth="YOUR_API_KEY",
        basic_auth=BasicAuthCredentials(username="YOUR_USERNAME", password="YOUR_PASSWORD"),
        client_key="YOUR_API_KEY",
    )
    # TODO: call endpoints here, awaiting each -- see api-reference.md
    await client.aclose()


run(main())
```

Alternatively, scope it — `async with AsyncAdyenClient(...) as client:` closes the pool on exit.

`AsyncClient` (`adyen/async_client.py`) mirrors `Client` method for method, each endpoint method a coroutine. It takes the same keywords, except that each client accepts only its own transport and — where the **Async Type** column differs — only its own flavor.

`Client` and `AsyncClient` are aliases of `AdyenClient` and `AsyncAdyenClient` — the names tracebacks and `repr()` show; all four import from the root.

`close()` / `aclose()` closes the transport even when you supplied one via `custom_http_client=` / `custom_async_http_client=`, and a closed client cannot be reused.

Every API group is a property on the client (e.g. `client.api_credentials_company_level`). Every constructor argument is optional and keyword-only. Sources: `adyen/client.py`, `adyen/async_client.py`:

| Keyword | Sync Type | Async Type | Default |
| --- | --- | --- | --- |
| `server_config` | `ServerConfigOrDict \| None` | `ServerConfigOrDict \| None` | `None` |
| `timeout` | `float` | `float` | `30.0` seconds |
| `retry_options` | `int \| RetryOptionsOrDict \| None` | `int \| RetryOptionsOrDict \| None` | `None` |
| `custom_http_client` | `HttpClient \| None` | — | `None` |
| `custom_async_http_client` | — | `AsyncHttpClient \| None` | `None` |
| `api_key_auth` | `str \| None` | `str \| None` | `None` |
| `basic_auth` | `BasicAuthCredentialsOrDict \| None` | `BasicAuthCredentialsOrDict \| None` | `None` |
| `client_key` | `str \| None` | `str \| None` | `None` |

The types those columns name — where each imports from and, for a credentials dict, its keys:

| Type | Import from | Shape |
| --- | --- | --- |
| `ServerConfigOrDict` | `adyen.server` | keys as the Servers & auth tables read |
| `RetryOptionsOrDict` | `adyen.core` | a retry count, `RetryOptions`, or a dict: `max_retries: int` · `initial_delay: float` · `backoff_factor: float` · `max_delay: float` · `max_jitter: float` · `status_codes_to_retry: frozenset[int]` · `http_methods_to_retry: frozenset[HttpMethod]` |
| `HttpClient` | `adyen.core` | protocol — `send(request: HttpRequest) -> HttpResponse` · `close()`; `send` returns once the head has arrived and never reads the body, and raises `TransportError` (from `core`) when no response arrives — anything else it raises is never retried |
| `BasicAuthCredentialsOrDict` | `adyen.core` | `BasicAuthCredentials` or a dict: `username: str` · `password: str` |
| `AsyncHttpClient` | `adyen.core` | protocol — `async send(request: HttpRequest) -> AsyncHttpResponse` · `async aclose()`; the same obligation, awaited |

### Retries — on by default

`retry_options` left at `None` applies the default `RetryOptions` policy below, so an unconfigured client **retries**: a request whose method is in `http_methods_to_retry` is sent again when it gets a status in `status_codes_to_retry`, or no response at all, and the last outcome reaches you only once its retries are spent. A body that cannot be re-sent byte for byte — a streamed file upload — is never retried. `retry_options=0` (or `{"max_retries": 0}`) turns retrying off; a bare count sets `max_retries` and leaves every other field at its default.

`RetryOptions` fields (source: `adyen/core/retries.py`). Pass only the fields you change; each one left out takes its default:

| Field | Type | Default |
| --- | --- | --- |
| `max_retries` | `int` | `3` |
| `initial_delay` | `float` (seconds) | `1.0` |
| `backoff_factor` | `float` | `2.0` |
| `max_delay` | `float` (seconds) | `60.0` |
| `max_jitter` | `float` (seconds) | `0.5` |
| `status_codes_to_retry` | `frozenset[int]` | `frozenset({408, 429, 500, 502, 503, 504})` |
| `http_methods_to_retry` | `frozenset[HttpMethod]` | `frozenset({"GET", "HEAD", "PUT", "OPTIONS"})` |

The wait before retry *n* is `initial_delay × backoff_factor^(n−1)` plus up to `max_jitter` of random delay, the sum capped at `max_delay`; a `Retry-After` header replaces it, trimmed to `max_delay`.

A single call overrides two of these through `request_options` (`adyen/core/request_options.py`): `max_retries` and `status_codes_to_retry`, each merged over the client's policy field by field — `request_options={"max_retries": 0}` turns retrying off for that one call and leaves every other call alone.

---

## Error-handling model (read once — applies to every operation)

Every operation is reached in two response modes:

- **Parsed call.** Returns the decoded payload and raises `ApiError` on an error status, with the decoded body on `.error` and the status on `.status_code`.
- **Raw call.** Reached through `.with_raw_response`; returns `ApiResult` — `Success` or `Failure` — and never raises for an API error. Read `.payload` on a `Success` or `.error` on a `Failure`; both carry `.status_code` and `.headers`.

What `.error` holds is fixed per operation. There are two cases:

- **Case A — typed error.** The operation documents at least one error status, so `adyen/errors/` declares a union alias over the bodies those statuses map to — `RawError` is always its last arm, for any undocumented status — and `.error` is annotated with that alias. Narrow it with `isinstance`. The operation blocks name the alias and the status each arm maps from.
- **Case B — raw error.** The operation documents no error status; `.error` is `RawError` (`adyen/core/results.py`): `status_code: int` · `content: bytes` · `text(encoding="utf-8"): str` · `json(): Any`.

Core runtime types (`adyen/core/`) — public members with their **declared types**, verbatim from source:

| Type | Public members | Source |
| --- | --- | --- |
| `ApiError` — raised by every parsed call; `.error` is a Case A alias from `adyen/errors/` or `RawError` | `error: E` · `status_code: int` · `headers: Mapping[str, str]` | `adyen/core/exceptions.py` |
| `ApiResult[T, E]` — returned by every raw call; the `Success[T] \| Failure[E]` union | `payload: T` (on `Success`) · `error: E` (on `Failure`) · `status_code: int` · `headers: Mapping[str, str]` (both on either) | `adyen/core/results.py` |
| `RawError` | `status_code: int` · `content: bytes` · `text(encoding="utf-8"): str` · `json(): Any` | `adyen/core/results.py` |

Typed error bodies (the arms of a Case A alias) are ordinary models — no special handling. The operation's **Type sources** table gives the module that declares each one; read field names, declared types and JSON aliases there, as for any other model.

```python
try:
    response = client.api_credentials_company_level.get_companies_company_id_api_credentials("some example string")
except ApiError as e:
    # Case A — typed error: e.error is GetCompaniesCompanyIdApiCredentialsErrorBody
    if isinstance(e.error, RestServiceError):
        # Handle 400, 401, 403, 422, 500
        print(e.error)
    if isinstance(e.error, RawError):
        # Any other error status
        print(e.status_code, e.error.text())
```

**Raw (`.with_raw_response`) variants: present on every operation** — the same call returns `ApiResult` instead of raising, with the same body on `Failure.error`. Of **449 operations**, **420 are Case A (typed)** and **29 are Case B (raw)**.

---

## Operations — by controller (93 pages, 449 operations)

Each links to a sub-page with one block per operation, headed by its full accessor path: the HTTP verb and route (for a mock, a raw request or a provider-side log — never reconstruct it from the method name), the sync parsed signature with its required positional parameters, each parameter's role and — where it differs — wire name, both return types, and its error case — **Case A** names the alias and the status each arm maps from, **Case B** names `RawError`. Every block also carries a **Type sources** table — every *generated* type it names, with the module that declares it. A runtime type — a file alias, a date/time or byte converter — is not listed there.

**Each block states what is specific to its operation. Everything below holds for every operation, and blocks never restate it — silence means the default applies.**

| Applies to every operation | Stated where |
| --- | --- |
| **Four spellings, one signature** — the same method name and parameters on `Client` and `AsyncClient`, each also reachable through `.with_raw_response`; the async twin is a coroutine to `await`, with the same return types and error case, and where the **Async Type** column differs, pass the type it names | Getting a client |
| **Parsed raises, raw returns** — `ApiError` versus `ApiResult` | Error-handling model |
| **Case B error is always `RawError`** — also the last arm of every Case A alias, where a block's **Error arms** bullet ends in it | Error-handling model |
| **A trailing `request_options`** — keyword-only and optional, for per-call overrides such as a timeout, extra headers, `max_retries` or `status_codes_to_retry`; every signature ends with it | here (`adyen/core/request_options.py`), Retries |
| **Each operation names its own server** — this SDK declares several, so every block carries a **Server** bullet with the server's key in `server_config=` | its block |
| **Parameter names are literal** — signatures are generated code verbatim, and everything behind the bare `*` must be passed by name | here |
| **A parameter's wire name is its Python name** — sent as-is on the path, query string, header or body, unless the block's **Params** bullet carries a wire name beside the role | here |

**The operation's behavioural prose lives on the operation itself**, as the method's docstring in the module named at the top of its page, and again in `api-reference.md` with a per-parameter description and a usage sample. Blocks here give you the contract — names, types, shapes, errors. Where an operation's *semantics* decide what you must pass, that is what the docstring settles; read it there rather than filling it in from memory.

Sub-pages chunk per `###` block: each block is self-contained given the table above, and assumes this page is loaded beside it.

| Controller | Ops | Page |
| --- | --- | --- |
| `client` (root) | 18 | [map/operations/client.md](map/operations/client.md) |
| `client.api_credentials_company_level` | 4 | [map/operations/api_credentials_company_level.md](map/operations/api_credentials_company_level.md) |
| `client.api_credentials_merchant_level` | 4 | [map/operations/api_credentials_merchant_level.md](map/operations/api_credentials_merchant_level.md) |
| `client.api_key_company_level` | 1 | [map/operations/api_key_company_level.md](map/operations/api_key_company_level.md) |
| `client.api_key_merchant_level` | 1 | [map/operations/api_key_merchant_level.md](map/operations/api_key_merchant_level.md) |
| `client.account_company_level` | 3 | [map/operations/account_company_level.md](map/operations/account_company_level.md) |
| `client.account_merchant_level` | 4 | [map/operations/account_merchant_level.md](map/operations/account_merchant_level.md) |
| `client.account_store_level` | 8 | [map/operations/account_store_level.md](map/operations/account_store_level.md) |
| `client.account_verification` | 2 | [map/operations/account_verification.md](map/operations/account_verification.md) |
| `client.account_holders` | 16 | [map/operations/account_holders.md](map/operations/account_holders.md) |
| `client.accounts` | 3 | [map/operations/accounts.md](map/operations/accounts.md) |
| `client.allowed_origins_company_level` | 4 | [map/operations/allowed_origins_company_level.md](map/operations/allowed_origins_company_level.md) |
| `client.allowed_origins_merchant_level` | 4 | [map/operations/allowed_origins_merchant_level.md](map/operations/allowed_origins_merchant_level.md) |
| `client.android_files_company_level` | 6 | [map/operations/android_files_company_level.md](map/operations/android_files_company_level.md) |
| `client.authorized_card_users` | 4 | [map/operations/authorized_card_users.md](map/operations/authorized_card_users.md) |
| `client.balance_accounts` | 5 | [map/operations/balance_accounts.md](map/operations/balance_accounts.md) |
| `client.balance_transfers` | 1 | [map/operations/balance_transfers.md](map/operations/balance_transfers.md) |
| `client.balances` | 5 | [map/operations/balances.md](map/operations/balances.md) |
| `client.balances_overview` | 2 | [map/operations/balances_overview.md](map/operations/balances_overview.md) |
| `client.bank_account_validation` | 1 | [map/operations/bank_account_validation.md](map/operations/bank_account_validation.md) |
| `client.business_lines_api` | 4 | [map/operations/business_lines_api.md](map/operations/business_lines_api.md) |
| `client.capital` | 3 | [map/operations/capital.md](map/operations/capital.md) |
| `client.card_orders` | 2 | [map/operations/card_orders.md](map/operations/card_orders.md) |
| `client.cash_out_api` | 1 | [map/operations/cash_out_api.md](map/operations/cash_out_api.md) |
| `client.client_key_company_level` | 1 | [map/operations/client_key_company_level.md](map/operations/client_key_company_level.md) |
| `client.client_key_merchant_level` | 1 | [map/operations/client_key_merchant_level.md](map/operations/client_key_merchant_level.md) |
| `client.custom_payout_schedules_sweeps` | 5 | [map/operations/custom_payout_schedules_sweeps.md](map/operations/custom_payout_schedules_sweeps.md) |
| `client.direct_debit_mandates` | 4 | [map/operations/direct_debit_mandates.md](map/operations/direct_debit_mandates.md) |
| `client.dispute_attachments` | 4 | [map/operations/dispute_attachments.md](map/operations/dispute_attachments.md) |
| `client.documents` | 4 | [map/operations/documents.md](map/operations/documents.md) |
| `client.donation_campaigns` | 6 | [map/operations/donation_campaigns.md](map/operations/donation_campaigns.md) |
| `client.donations` | 2 | [map/operations/donations.md](map/operations/donations.md) |
| `client.dynamic_offers` | 3 | [map/operations/dynamic_offers.md](map/operations/dynamic_offers.md) |
| `client.general` | 41 | [map/operations/general.md](map/operations/general.md) |
| `client.grant_accounts` | 2 | [map/operations/grant_accounts.md](map/operations/grant_accounts.md) |
| `client.grant_offers_api` | 4 | [map/operations/grant_offers_api.md](map/operations/grant_offers_api.md) |
| `client.grants_api` | 6 | [map/operations/grants_api.md](map/operations/grants_api.md) |
| `client.hosted_onboarding` | 3 | [map/operations/hosted_onboarding.md](map/operations/hosted_onboarding.md) |
| `client.hosted_onboarding_page` | 1 | [map/operations/hosted_onboarding_page.md](map/operations/hosted_onboarding_page.md) |
| `client.initialization` | 3 | [map/operations/initialization.md](map/operations/initialization.md) |
| `client.instant_payouts` | 1 | [map/operations/instant_payouts.md](map/operations/instant_payouts.md) |
| `client.legal_entities` | 7 | [map/operations/legal_entities.md](map/operations/legal_entities.md) |
| `client.manage_sca_devices` | 6 | [map/operations/manage_sca_devices.md](map/operations/manage_sca_devices.md) |
| `client.manage_card_pin` | 3 | [map/operations/manage_card_pin.md](map/operations/manage_card_pin.md) |
| `client.managed_payout_schedules` | 8 | [map/operations/managed_payout_schedules.md](map/operations/managed_payout_schedules.md) |
| `client.modifications` | 14 | [map/operations/modifications.md](map/operations/modifications.md) |
| `client.my_api_credential` | 6 | [map/operations/my_api_credential.md](map/operations/my_api_credential.md) |
| `client.network_tokens` | 2 | [map/operations/network_tokens.md](map/operations/network_tokens.md) |
| `client.orders` | 3 | [map/operations/orders.md](map/operations/orders.md) |
| `client.pci_compliance_questionnaire_page` | 1 | [map/operations/pci_compliance_questionnaire_page.md](map/operations/pci_compliance_questionnaire_page.md) |
| `client.pci_questionnaires` | 5 | [map/operations/pci_questionnaires.md](map/operations/pci_questionnaires.md) |
| `client.payment_instrument_groups` | 3 | [map/operations/payment_instrument_groups.md](map/operations/payment_instrument_groups.md) |
| `client.payment_instruments` | 9 | [map/operations/payment_instruments.md](map/operations/payment_instruments.md) |
| `client.payment_links` | 3 | [map/operations/payment_links.md](map/operations/payment_links.md) |
| `client.payment_methods_merchant_level` | 6 | [map/operations/payment_methods_merchant_level.md](map/operations/payment_methods_merchant_level.md) |
| `client.payments` | 14 | [map/operations/payments.md](map/operations/payments.md) |
| `client.payments_app` | 5 | [map/operations/payments_app.md](map/operations/payments_app.md) |
| `client.payout_settings_merchant_level` | 5 | [map/operations/payout_settings_merchant_level.md](map/operations/payout_settings_merchant_level.md) |
| `client.platform` | 3 | [map/operations/platform.md](map/operations/platform.md) |
| `client.raise_disputes` | 4 | [map/operations/raise_disputes.md](map/operations/raise_disputes.md) |
| `client.rates` | 1 | [map/operations/rates.md](map/operations/rates.md) |
| `client.recurring_api` | 4 | [map/operations/recurring_api.md](map/operations/recurring_api.md) |
| `client.recurring_top_ups` | 4 | [map/operations/recurring_top_ups.md](map/operations/recurring_top_ups.md) |
| `client.reviewing` | 2 | [map/operations/reviewing.md](map/operations/reviewing.md) |
| `client.sca_association_management` | 3 | [map/operations/sca_association_management.md](map/operations/sca_association_management.md) |
| `client.sca_device_management` | 4 | [map/operations/sca_device_management.md](map/operations/sca_device_management.md) |
| `client.session_authentication` | 2 | [map/operations/session_authentication.md](map/operations/session_authentication.md) |
| `client.split_configuration_merchant_level` | 9 | [map/operations/split_configuration_merchant_level.md](map/operations/split_configuration_merchant_level.md) |
| `client.tax_e_delivery_consent` | 2 | [map/operations/tax_e_delivery_consent.md](map/operations/tax_e_delivery_consent.md) |
| `client.terminal_actions_company_level` | 2 | [map/operations/terminal_actions_company_level.md](map/operations/terminal_actions_company_level.md) |
| `client.terminal_actions_terminal_level` | 1 | [map/operations/terminal_actions_terminal_level.md](map/operations/terminal_actions_terminal_level.md) |
| `client.terminal_orders_company_level` | 10 | [map/operations/terminal_orders_company_level.md](map/operations/terminal_orders_company_level.md) |
| `client.terminal_orders_merchant_level` | 10 | [map/operations/terminal_orders_merchant_level.md](map/operations/terminal_orders_merchant_level.md) |
| `client.terminal_settings_company_level` | 4 | [map/operations/terminal_settings_company_level.md](map/operations/terminal_settings_company_level.md) |
| `client.terminal_settings_merchant_level` | 4 | [map/operations/terminal_settings_merchant_level.md](map/operations/terminal_settings_merchant_level.md) |
| `client.terminal_settings_store_level` | 8 | [map/operations/terminal_settings_store_level.md](map/operations/terminal_settings_store_level.md) |
| `client.terminal_settings_terminal_level` | 4 | [map/operations/terminal_settings_terminal_level.md](map/operations/terminal_settings_terminal_level.md) |
| `client.terminals_terminal_level` | 2 | [map/operations/terminals_terminal_level.md](map/operations/terminals_terminal_level.md) |
| `client.terms_of_service` | 5 | [map/operations/terms_of_service.md](map/operations/terms_of_service.md) |
| `client.transaction_rules` | 4 | [map/operations/transaction_rules.md](map/operations/transaction_rules.md) |
| `client.transactions` | 2 | [map/operations/transactions.md](map/operations/transactions.md) |
| `client.transfer_instruments` | 4 | [map/operations/transfer_instruments.md](map/operations/transfer_instruments.md) |
| `client.transfer_limits_balance_account_level` | 6 | [map/operations/transfer_limits_balance_account_level.md](map/operations/transfer_limits_balance_account_level.md) |
| `client.transfer_limits_balance_platform_level` | 4 | [map/operations/transfer_limits_balance_platform_level.md](map/operations/transfer_limits_balance_platform_level.md) |
| `client.transfer_routes` | 1 | [map/operations/transfer_routes.md](map/operations/transfer_routes.md) |
| `client.transfers` | 6 | [map/operations/transfers.md](map/operations/transfers.md) |
| `client.users_company_level` | 4 | [map/operations/users_company_level.md](map/operations/users_company_level.md) |
| `client.users_merchant_level` | 4 | [map/operations/users_merchant_level.md](map/operations/users_merchant_level.md) |
| `client.utility` | 4 | [map/operations/utility.md](map/operations/utility.md) |
| `client.verification` | 8 | [map/operations/verification.md](map/operations/verification.md) |
| `client.webhooks_company_level` | 7 | [map/operations/webhooks_company_level.md](map/operations/webhooks_company_level.md) |
| `client.webhooks_merchant_level` | 7 | [map/operations/webhooks_merchant_level.md](map/operations/webhooks_merchant_level.md) |
| `client.i_deal_profiles` | 3 | [map/operations/i_deal_profiles.md](map/operations/i_deal_profiles.md) |

---

## Models — where they live, how to build them

**Shapes live only in the source.** Every module under `adyen/models/` declares one type plus its input companion, and every module under `adyen/errors/` one alias plus the mapper that builds it; no two share a name. Take a type's module from the operation's **Type sources** table. When no retrieved chunk names it, the module is the type name in snake_case under the kind's directory below (`AchDirectDebit` ↔ `ach_direct_debit.py`; an error alias drops its `Body` suffix: `DeleteBalanceAccountsBalanceAccountIdPayoutSchedulesIdErrorBody` ↔ `delete_balance_accounts_balance_account_id_payout_schedules_id_error.py`). Never grep for a type.

| Group | Count | Directory (module = `<type_name>.py`) |
| --- | --- | --- |
| Models (`SdkBaseModel` pydantic classes) | 2046 | `adyen/models/` |
| Enums (`Enum` over `str`) — Python member names + wire values | 522 | `adyen/models/enums/` |
| Unions (discriminated) — `TypeAlias` over the arms, tagged via `WireDiscriminator(…)` | 20 | `adyen/models/unions/` |
| Unions (plain) — `TypeAlias` over the arms | 1 | `adyen/models/unions/` |
| Error aliases (one per Case A operation) | 420 | `adyen/errors/` |

Conventions: a model is a `SdkBaseModel` (pydantic) class; a field whose wire name differs from its Python name carries it as `Field(alias=…)` (`account_holder_type` ↔ `"accountHolderType"`) — read the alias off the field rather than deriving it. An omittable field is annotated `Optional[T]` and defaults to `UNSET`, and one that may also be explicitly null is `OptionalNullable[T]`; both come from `core` and neither is `typing.Optional` — there is no `None` arm unless the spec declared the property nullable, so passing `None` to the first is a type error rather than a value that serializes.

Every model, enum and union also has an **input companion**, exported beside it from the same package (`AchDirectDebit` ↔ `AchDirectDebitDict`). Wherever a signature names the companion you may pass either the model instance or a plain dict with the same keys, whichever reads better at the call site. An enum is a real `Enum` subclass over `str`; its companion is spelled `<Name>OrStr` or `<Name>OrInt` (`AccountAgeIndicator` ↔ `AccountAgeIndicatorOrStr`) and additionally accepts a wire value this SDK version does not know. A union is a `TypeAlias` over its arms — a discriminated one names the wire key its arms are told apart by, so build the arm you mean and the union supplies the tag for any arm whose own schema does not declare it.

Import paths by content type (`from <package> import <Name>`):

| Contents | Import from |
| --- | --- |
| Client (root) | `adyen` |
| Operation controllers | `adyen.apis` |
| Models | `adyen.models` |
| Enums | `adyen.models.enums` |
| Unions | `adyen.models.unions`, `adyen.models` |
| Error aliases | `adyen.errors` |
| Core runtime (`ApiError`, `ApiResult`, `RawError`, …) | `adyen.core` |

---

## Servers & auth

**API key (header `X-API-Key`).** Pass `api_key_auth="<api_key>"`; sent as the `X-API-Key` request header.

**Basic auth.** Pass `basic_auth={"username": …, "password": …}`, or a `BasicAuthCredentials`.

**API key (query `clientKey`).** Pass `client_key="<api_key>"`; sent as the `clientKey` query parameter.

Operation blocks name their scheme in an **Auth** bullet; an operation whose spec declares no scheme carries no such bullet.

- `AND` — every scheme listed must be configured for the call to succeed.
- `OR` — any one of the schemes listed can be used; the first one you configured is the one sent, in the order listed.

A scheme you did not configure is skipped silently rather than raising, and the request is sent anyway — so an authentication failure can mean no credential was sent rather than a bad one.

**One environment.** The spec declares a single environment, so no `environment` keyword exists and there is nothing to select.

**29 servers.** Base-URL templates and override points (`adyen/server/server_config.py`):

| Server | Base URL | Override point |
| --- | --- | --- |
| `default` | `https://checkout-test.adyen.com/v72` | `{"default": {"base_url": …}}` |
| `default1` | `https://pal-test.adyen.com/pal/servlet/Payment/v68` | `{"default1": {"base_url": …}}` |
| `default2` | `https://pal-test.adyen.com/pal/servlet/Recurring/v68` | `{"default2": {"base_url": …}}` |
| `default3` | `https://pal-test.adyen.com/pal/servlet/Payout/v68` | `{"default3": {"base_url": …}}` |
| `default4` | `https://pal-test.adyen.com/pal/servlet/BinLookup/v54` | `{"default4": {"base_url": …}}` |
| `default5` | `https://pal-test.adyen.com/pal/servlet/StoredValue/v46` | `{"default5": {"base_url": …}}` |
| `default6` | `https://ca-test.adyen.com/ca/services/DataProtectionService/v1` | `{"default6": {"base_url": …}}` |
| `default7` | `https://balanceplatform-api-test.adyen.com/fx/api/v1` | `{"default7": {"base_url": …}}` |
| `default8` | `https://pal-test.adyen.com/pal/services/TestCard/v1` | `{"default8": {"base_url": …}}` |
| `default9` | `https://management-test.adyen.com/v3` | `{"default9": {"base_url": …}}` |
| `default10` | `https://cal-test.adyen.com/cal/services/Account/v6` | `{"default10": {"base_url": …}}` |
| `default11` | `https://balance-control-test.adyen.com/balance-control/api/v2` | `{"default11": {"base_url": …}}` |
| `default12` | `https://cal-test.adyen.com/cal/services/Notification/v6` | `{"default12": {"base_url": …}}` |
| `default13` | `https://balanceplatform-api-test.adyen.com/bcl/v2` | `{"default13": {"base_url": …}}` |
| `default14` | `https://balanceplatform-api-test.adyen.com/btl/v4` | `{"default14": {"base_url": …}}` |
| `default15` | `https://balanceplatform-api-test.adyen.com/capital/v1` | `{"default15": {"base_url": …}}` |
| `default16` | `https://cal-test.adyen.com/cal/services/Fund/v6` | `{"default16": {"base_url": …}}` |
| `default17` | `https://test.adyen.com/authe/api/v1` | `{"default17": {"base_url": …}}` |
| `default18` | `https://kyc-test.adyen.com/lem/v4` | `{"default18": {"base_url": …}}` |
| `default19` | `https://cal-test.adyen.com/cal/services/Hop/v6` | `{"default19": {"base_url": …}}` |
| `default20` | `https://balanceplatform-api-test.adyen.com/a2aissuer-api/v1` | `{"default20": {"base_url": …}}` |
| `default21` | `https://obgateway-test.adyen.com/obgateway/v1` | `{"default21": {"base_url": …}}` |
| `default22` | `https://ca-test.adyen.com/ca/services/DisputeService/v30` | `{"default22": {"base_url": …}}` |
| `default23` | `https://balanceplatform-api-test.adyen.com/btl/api/v4` | `{"default23": {"base_url": …}}` |
| `default24` | `https://device-api-test.adyen.com/v1` | `{"default24": {"base_url": …}}` |
| `default25` | `https://softposconfig-test.adyen.com/softposconfig/v3` | `{"default25": {"base_url": …}}` |
| `default26` | `https://management-test.adyen.com/v1` | `{"default26": {"base_url": …}}` |
| `default27` | `https://checkout-test.adyen.com/checkout/possdk/v68` | `{"default27": {"base_url": …}}` |
| `default28` | `https://postfmapi-test.adyen.com/postfmapi/terminal/v1` | `{"default28": {"base_url": …}}` |

Override any of these by passing `server_config=` a dict nested exactly as the columns above read — `{"default": {"base_url": …}}` — with each row's variables sitting beside its `base_url`.

