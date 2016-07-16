import sys
from os.path import dirname, abspath, join, exists

PROJECT_DIR = dirname(dirname(abspath(__file__)))
SITEPACKAGES_DIR = join(PROJECT_DIR, "sitepackages")
APPENGINE_DIR = join(SITEPACKAGES_DIR, "google_appengine")


def fix_path():
    if exists(APPENGINE_DIR) and APPENGINE_DIR not in sys.path:
        sys.path.insert(1, APPENGINE_DIR)

    if SITEPACKAGES_DIR not in sys.path:
        sys.path.insert(1, SITEPACKAGES_DIR)


def get_app_config():
    """Returns the application configuration, creating it if necessary."""
    from django.utils.crypto import get_random_string
    from google.appengine.ext import ndb

    class Config(ndb.Model):
        """A simple key-value store for application configuration settings."""
        secret_key = ndb.StringProperty()

    # Create a random SECRET_KEY
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'

    @ndb.transactional()
    def txn():
        # Get or create the Config in a transaction, so that if it doesn't exist we don't get 2
        # threads creating a Config object and one overwriting the other
        key = ndb.Key(Config, 'config')
        entity = key.get()
        if not entity:
            entity = Config(key=key)
            entity.secret_key = get_random_string(50, chars)
            entity.put()
        return entity
    return txn()

