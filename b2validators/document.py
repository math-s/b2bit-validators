import re
from b2validators.exceptions import ValidationError


def validate_cnpj(value):
    cnpj = re.sub("[^0-9]", "", value)
    if len(cnpj) < 14:
        raise ValidationError("O CNPJ precisa ter 14 dígitos.")

    expected_cnpj = [int(digit) for digit in cnpj[:12] if digit.isdigit()]
    cnpj_test = [int(digit) for digit in cnpj if digit.isdigit()]
    weights = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    result = []
    for idx, w in enumerate(weights):
        x = w*expected_cnpj[idx]
        result.append(x)
    resul_sum = sum(result)
    remainder = resul_sum % 11
    if remainder < 2:
        expected_cnpj.append(0)
    else:
        expected_cnpj.append(11 - remainder)

    weights = [6] + weights
    result = []
    for idx, w in enumerate(weights):
        x = w*expected_cnpj[idx]
        result.append(x)
    resul_sum = sum(result)
    remainder = resul_sum % 11
    if remainder < 2:
        expected_cnpj.append(0)
    else:
        expected_cnpj.append(11 - remainder)

    if cnpj_test != expected_cnpj:
        raise ValidationError("CNPJ inválido")

    return value


def validate_cpf(value):
    cpf = re.sub("[^0-9]", "", value)
    if len(cpf) != 11:
        raise ValidationError("O CPF deve ter 11 dígitos.")

    expected_cpf = [int(digit) for digit in cpf][:9]
    cpf_test = [int(digit) for digit in cpf]

    weights = [10, 9, 8, 7, 6, 5, 4, 3, 2]
    result = []
    for idx, w in enumerate(weights):
        x = w*expected_cpf[idx]
        result.append(x)
    resul_sum = sum(result)
    remainder = resul_sum % 11
    if remainder < 2:
        expected_cpf.append(0)
    else:
        expected_cpf.append(11 - remainder)

    weights = [11] + weights
    result = []
    for idx, w in enumerate(weights):
        x = w*expected_cpf[idx]
        result.append(x)
    resul_sum = sum(result)
    remainder = resul_sum % 11
    if remainder < 2:
        expected_cpf.append(0)
    else:
        expected_cpf.append(11 - remainder)

    if cpf_test != expected_cpf:
        raise ValidationError("CPF inválido.")
    return value
