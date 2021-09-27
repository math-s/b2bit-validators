from b2validators.credit_card import (
    validate_cvv,
    validate_expiration_date,
    validate_number)
from b2validators.document import validate_cnpj, validate_cpf
from b2validators.phone import validate_phone_ddd, validate_phone_e164


validate_cpf("104.772.464-27")
validate_cnpj("446739540001-30")
validate_number("5349 9829 3187 3721")
validate_cvv("001")
validate_expiration_date("12/2021")
validate_expiration_date("12/21")
validate_phone_ddd("84")
validate_phone_e164("+5582999999999")
