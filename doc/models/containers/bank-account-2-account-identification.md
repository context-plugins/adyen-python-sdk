
# Bank Account 2 Account Identification

## Data Type

`AULocalAccountIdentification | BRLocalAccountIdentification | CALocalAccountIdentification | CZLocalAccountIdentification | DKLocalAccountIdentification | HKLocalAccountIdentification | HULocalAccountIdentification | IbanAccountIdentification | NOLocalAccountIdentification | NZLocalAccountIdentification | NumberAndBicAccountIdentification | PLLocalAccountIdentification | SELocalAccountIdentification | SGLocalAccountIdentification | UKLocalAccountIdentification | USLocalAccountIdentification`

## Cases

| Type |
|  --- |
| [`AULocalAccountIdentification`](../../../doc/models/au-local-account-identification.md) |
| [`BRLocalAccountIdentification`](../../../doc/models/br-local-account-identification.md) |
| [`CALocalAccountIdentification`](../../../doc/models/ca-local-account-identification.md) |
| [`CZLocalAccountIdentification`](../../../doc/models/cz-local-account-identification.md) |
| [`DKLocalAccountIdentification`](../../../doc/models/dk-local-account-identification.md) |
| [`HKLocalAccountIdentification`](../../../doc/models/hk-local-account-identification.md) |
| [`HULocalAccountIdentification`](../../../doc/models/hu-local-account-identification.md) |
| [`IbanAccountIdentification`](../../../doc/models/iban-account-identification.md) |
| [`NOLocalAccountIdentification`](../../../doc/models/no-local-account-identification.md) |
| [`NZLocalAccountIdentification`](../../../doc/models/nz-local-account-identification.md) |
| [`NumberAndBicAccountIdentification`](../../../doc/models/number-and-bic-account-identification.md) |
| [`PLLocalAccountIdentification`](../../../doc/models/pl-local-account-identification.md) |
| [`SELocalAccountIdentification`](../../../doc/models/se-local-account-identification.md) |
| [`SGLocalAccountIdentification`](../../../doc/models/sg-local-account-identification.md) |
| [`UKLocalAccountIdentification`](../../../doc/models/uk-local-account-identification.md) |
| [`USLocalAccountIdentification`](../../../doc/models/us-local-account-identification.md) |

## AULocalAccountIdentification

### Initialization Code

#### Example

```python
value = AULocalAccountIdentification(
    account_number='accountNumber4',
    bsb_code='bsbCode8'
)
```

## BRLocalAccountIdentification

### Initialization Code

#### Example

```python
value = BRLocalAccountIdentification(
    account_number='accountNumber0',
    bank_code='bankCode2',
    branch_number='branchNumber2'
)
```

## CALocalAccountIdentification

### Initialization Code

#### Example

```python
value = CALocalAccountIdentification(
    account_number='accountNumber8',
    institution_number='institutionNumber2',
    transit_number='transitNumber8',
    account_type=AccountType2Enum.CHECKING
)
```

## CZLocalAccountIdentification

### Initialization Code

#### Example

```python
value = CZLocalAccountIdentification(
    account_number='accountNumber4',
    bank_code='bankCode8'
)
```

## DKLocalAccountIdentification

### Initialization Code

#### Example

```python
value = DKLocalAccountIdentification(
    account_number='accountNumber6',
    bank_code='bankCode6'
)
```

## HKLocalAccountIdentification

### Initialization Code

#### Example

```python
value = HKLocalAccountIdentification(
    account_number='accountNumber8',
    clearing_code='clearingCode2'
)
```

## HULocalAccountIdentification

### Initialization Code

#### Example

```python
value = HULocalAccountIdentification(
    account_number='accountNumber8'
)
```

## IbanAccountIdentification

### Initialization Code

#### Example

```python
value = IbanAccountIdentification(
    iban='iban6'
)
```

## NOLocalAccountIdentification

### Initialization Code

#### Example

```python
value = NOLocalAccountIdentification(
    account_number='accountNumber6'
)
```

## NZLocalAccountIdentification

### Initialization Code

#### Example

```python
value = NZLocalAccountIdentification(
    account_number='accountNumber6'
)
```

## NumberAndBicAccountIdentification

### Initialization Code

#### Example

```python
value = NumberAndBicAccountIdentification(
    account_number='accountNumber0',
    bic='bic4'
)
```

## PLLocalAccountIdentification

### Initialization Code

#### Example

```python
value = PLLocalAccountIdentification(
    account_number='accountNumber4'
)
```

## SELocalAccountIdentification

### Initialization Code

#### Example

```python
value = SELocalAccountIdentification(
    account_number='accountNumber0',
    clearing_number='clearingNumber2'
)
```

## SGLocalAccountIdentification

### Initialization Code

#### Example

```python
value = SGLocalAccountIdentification(
    account_number='accountNumber2',
    bic='bic2',
    mtype=Type82Enum.SGLOCAL
)
```

## UKLocalAccountIdentification

### Initialization Code

#### Example

```python
value = UKLocalAccountIdentification(
    account_number='accountNumber8',
    sort_code='sortCode8'
)
```

## USLocalAccountIdentification

### Initialization Code

#### Example

```python
value = USLocalAccountIdentification(
    account_number='accountNumber2',
    routing_number='routingNumber2',
    account_type=AccountType2Enum.CHECKING
)
```

