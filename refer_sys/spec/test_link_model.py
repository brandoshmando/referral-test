import pytest
from refer_sys.models import Link
from refer_sys.factories import LinkFactory
@pytest.mark.django_db
def test_valid_link_object():
  assert LinkFactory.create()
@pytest.mark.django_db
def test_add_click():
  link = LinkFactory.create()
  link.add_click()
  assert link.clicks == 1

def test_format_query():
  link = LinkFactory.create()
  assert link.format_query() == "example"

def test_format_query_with_spaces():
  link = LinkFactory.build(title="Example Title")
  assert link.format_query() == "example+title"




