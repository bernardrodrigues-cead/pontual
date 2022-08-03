from time import timezone
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_month(value):
    if int(value) < 1 or int(value) > 12:
        raise ValidationError(
            _('Favor utilizar um mês no formato mm')
        )

def validate_year(value):
    if int(value) < 1000 or int(value) > 9999:
        raise ValidationError(
            _('Favor utilizar um ano no formato yyyy')
        )