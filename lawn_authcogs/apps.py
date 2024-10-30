"""App Configuration"""

# Third Party
# AA Example App
from lawn_helpers import __version__

# Django
from django.apps import AppConfig


class ExampleConfig(AppConfig):
    """App Config"""

    name = "lawn_helpers"
    label = "lawn_helpers"
    verbose_name = f"Lawn Helpers v{__version__}"
