import pkg_resources

from schwifty.bic import BIC
from schwifty.iban import IBAN
from schwifty import exceptions


__all__ = ["IBAN", "BIC"]
__version__ = pkg_resources.get_distribution(__name__).version
