
# Bank Account Info Account Identification

## Data Type

`AuLocalAccountIdentification | CaLocalAccountIdentification | CzLocalAccountIdentification | DkLocalAccountIdentification | HkLocalAccountIdentification | HuLocalAccountIdentification | IbanAccountIdentification1 | NoLocalAccountIdentification | NzLocalAccountIdentification | NumberAndBicAccountIdentification | PlLocalAccountIdentification | SeLocalAccountIdentification | SgLocalAccountIdentification | UkLocalAccountIdentification | UsLocalAccountIdentification`

## Cases

| Type |
|  --- |
| [`AuLocalAccountIdentification`](../../../doc/models/au-local-account-identification.md) |
| [`CaLocalAccountIdentification`](../../../doc/models/ca-local-account-identification.md) |
| [`CzLocalAccountIdentification`](../../../doc/models/cz-local-account-identification.md) |
| [`DkLocalAccountIdentification`](../../../doc/models/dk-local-account-identification.md) |
| [`HkLocalAccountIdentification`](../../../doc/models/hk-local-account-identification.md) |
| [`HuLocalAccountIdentification`](../../../doc/models/hu-local-account-identification.md) |
| [`IbanAccountIdentification1`](../../../doc/models/iban-account-identification-1.md) |
| [`NoLocalAccountIdentification`](../../../doc/models/no-local-account-identification.md) |
| [`NzLocalAccountIdentification`](../../../doc/models/nz-local-account-identification.md) |
| [`NumberAndBicAccountIdentification`](../../../doc/models/number-and-bic-account-identification.md) |
| [`PlLocalAccountIdentification`](../../../doc/models/pl-local-account-identification.md) |
| [`SeLocalAccountIdentification`](../../../doc/models/se-local-account-identification.md) |
| [`SgLocalAccountIdentification`](../../../doc/models/sg-local-account-identification.md) |
| [`UkLocalAccountIdentification`](../../../doc/models/uk-local-account-identification.md) |
| [`UsLocalAccountIdentification`](../../../doc/models/us-local-account-identification.md) |

## AuLocalAccountIdentification

### Initialization Code

#### Example

```python
value = AuLocalAccountIdentification(
    account_number='accountNumber4',
    bsb_code='bsbCode8',
    mtype=Type413.AULOCAL
)
```

## CaLocalAccountIdentification

### Initialization Code

#### Example

```python
value = CaLocalAccountIdentification(
    account_number='accountNumber8',
    institution_number='institutionNumber2',
    transit_number='transitNumber8',
    mtype=Type153.CALOCAL
)
```

## CzLocalAccountIdentification

### Initialization Code

#### Example

```python
value = CzLocalAccountIdentification(
    account_number='accountNumber4',
    bank_code='bankCode8',
    mtype=Type163.CZLOCAL
)
```

## DkLocalAccountIdentification

### Initialization Code

#### Example

```python
value = DkLocalAccountIdentification(
    account_number='accountNumber6',
    bank_code='bankCode6',
    mtype=Type173.DKLOCAL
)
```

## HkLocalAccountIdentification

### Initialization Code

#### Example

```python
value = HkLocalAccountIdentification(
    account_number='accountNumber8',
    clearing_code='clearingCode2',
    mtype=Type1810.HKLOCAL
)
```

## HuLocalAccountIdentification

### Initialization Code

#### Example

```python
value = HuLocalAccountIdentification(
    account_number='accountNumber8',
    mtype=Type193.HULOCAL
)
```

## IbanAccountIdentification1

### Initialization Code

#### Example

```python
value = IbanAccountIdentification1(
    iban='iban4',
    mtype=Type203.IBAN
)
```

## NoLocalAccountIdentification

### Initialization Code

#### Example

```python
value = NoLocalAccountIdentification(
    account_number='accountNumber6',
    mtype=Type223.NOLOCAL
)
```

## NzLocalAccountIdentification

### Initialization Code

#### Example

```python
value = NzLocalAccountIdentification(
    account_number='accountNumber6',
    mtype=Type233.NZLOCAL
)
```

## NumberAndBicAccountIdentification

### Initialization Code

#### Example

```python
value = NumberAndBicAccountIdentification(
    account_number='accountNumber0',
    bic='bic4',
    mtype=Type244.NUMBERANDBIC
)
```

## PlLocalAccountIdentification

### Initialization Code

#### Example

```python
value = PlLocalAccountIdentification(
    account_number='accountNumber4',
    mtype=Type256.PLLOCAL
)
```

## SeLocalAccountIdentification

### Initialization Code

#### Example

```python
value = SeLocalAccountIdentification(
    account_number='accountNumber0',
    clearing_number='clearingNumber2',
    mtype=Type264.SELOCAL
)
```

## SgLocalAccountIdentification

### Initialization Code

#### Example

```python
value = SgLocalAccountIdentification(
    account_number='accountNumber2',
    bic='bic2'
)
```

## UkLocalAccountIdentification

### Initialization Code

#### Example

```python
value = UkLocalAccountIdentification(
    account_number='accountNumber8',
    sort_code='sortCode8',
    mtype=Type273.UKLOCAL
)
```

## UsLocalAccountIdentification

### Initialization Code

#### Example

```python
value = UsLocalAccountIdentification(
    account_number='accountNumber2',
    routing_number='routingNumber2',
    mtype=Type283.USLOCAL
)
```

