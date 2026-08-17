
# Schedule Terminal Actions Response Action Details

## Data Type

`ForceRebootDetails | InstallAndroidAppDetails | InstallAndroidCertificateDetails | ReleaseUpdateDetails | UninstallAndroidAppDetails | UninstallAndroidCertificateDetails`

## Cases

| Type |
|  --- |
| [`ForceRebootDetails`](../../../doc/models/force-reboot-details.md) |
| [`InstallAndroidAppDetails`](../../../doc/models/install-android-app-details.md) |
| [`InstallAndroidCertificateDetails`](../../../doc/models/install-android-certificate-details.md) |
| [`ReleaseUpdateDetails`](../../../doc/models/release-update-details.md) |
| [`UninstallAndroidAppDetails`](../../../doc/models/uninstall-android-app-details.md) |
| [`UninstallAndroidCertificateDetails`](../../../doc/models/uninstall-android-certificate-details.md) |

## ForceRebootDetails

### Initialization Code

#### Example

```python
value = ForceRebootDetails(
    mtype=Type210Enum.FORCEREBOOT
)
```

## InstallAndroidAppDetails

### Initialization Code

#### Example

```python
value = InstallAndroidAppDetails(
    mtype=Type32Enum.INSTALLANDROIDAPP
)
```

## InstallAndroidCertificateDetails

### Initialization Code

#### Example

```python
value = InstallAndroidCertificateDetails(
    mtype=Type42Enum.INSTALLANDROIDCERTIFICATE
)
```

## ReleaseUpdateDetails

### Initialization Code

#### Example

```python
value = ReleaseUpdateDetails(
    mtype=Type61Enum.RELEASEUPDATE
)
```

## UninstallAndroidAppDetails

### Initialization Code

#### Example

```python
value = UninstallAndroidAppDetails(
    mtype=Type71Enum.UNINSTALLANDROIDAPP
)
```

## UninstallAndroidCertificateDetails

### Initialization Code

#### Example

```python
value = UninstallAndroidCertificateDetails(
    mtype=Type81Enum.UNINSTALLANDROIDCERTIFICATE
)
```

