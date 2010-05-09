"""
Email related settings
"""
from forum.conf.settings_wrapper import settings
from livesettings import ConfigurationGroup, IntegerValue
from django.utils.translation import ugettext as _

EMAIL = ConfigurationGroup(
            'EMAIL',
            _('Email and email alert settings'), 
        )

settings.register(
    IntegerValue(
        EMAIL,
        'MAX_ALERTS_PER_EMAIL',
        default=7,
        description=_('Maximum number of news entries in an email alert')
    )
)

#todo: move email.py email_settings.py?

EMAIL_VALIDATION = 'off' #string - on|off
EMAIL_UNIQUE = False
ANONYMOUS_USER_EMAIL = 'anonymous@askbot.org'
