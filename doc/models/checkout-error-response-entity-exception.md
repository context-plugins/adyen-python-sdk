
# Checkout Error Response Entity Exception

## Structure

`CheckoutErrorResponseEntityException`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `error_code` | `str` | Required | - |
| `error_type` | `str` | Required | - |
| `message` | `str` | Required | - |
| `psp_reference` | `str` | Optional | - |
| `status` | `int` | Optional | - |

## Example

```python
try:
    # make the API call
except CheckoutErrorResponseEntityException as e:
    print(e)
except APIException as e:
    print(e)
```

