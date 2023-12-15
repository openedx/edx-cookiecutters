"""
Tests for {{cookiecutter.class_name}}
"""

from django.test import TestCase
from xblock.fields import ScopeIds
from xblock.test.toy_runtime import ToyRuntime
from my_xblock import MyXBlock


class Test{{cookiecutter.class_name}}(TestCase):
    """Tests for {{cookiecutter.class_name}}"""
    def test_my_student_view(self):
        """Test the basic view loads."""
        scope_ids = ScopeIds('1', '2', '3', '4')
        block = MyXBlock(ToyRuntime(), scope_ids=scope_ids)
        frag = block.student_view()
        as_dict = frag.to_dict()
        content = as_dict['content']
        self.assertIn('MyXBlock: count is now', content, 'XBlock did not render correct student view')
