import unittest
import pycodestyle
import os

excludeDirs = ['node_modules', '__pycache__', '.serverless']


def discover_all_python_files():
    matches = []
    for root, dirnames, filenames in os.walk('.'):
        dirnames[:] = [
            dirname for dirname in dirnames if dirname not in excludeDirs]
        for filename in filenames:
            if filename.endswith(('.py')):
                matches.append(os.path.join(root, filename))
    return matches


class CodeStyleTest(unittest.TestCase):
    def test_pep8_conformance(self):
        """Test that we conform to PEP-8."""
        style_guide = pycodestyle.StyleGuide()
        style_check_report = style_guide.check_files(
            discover_all_python_files())
        self.assertEqual(style_check_report.total_errors, 0,
                         "Found code style errors (and warnings).")
