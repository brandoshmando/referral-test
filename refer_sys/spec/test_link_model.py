import pytest
from refer_sys.factories import LinkFactory

def test_valid_link_object():
  assert LinkFactory.create

def test_add_click():
  link = LinkFactory.create
  link.add_click()
  assert link.clicks == 1

