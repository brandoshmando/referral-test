import factory
from refer_sys.models import Link

class LinkFactory(factory.Factory):
  FACTORY_FOR = Link
  title = "This is an example title."
