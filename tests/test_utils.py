import unittest

from eiffelactory import utils


class TestUtils(unittest.TestCase):

    def test_remove_none_from_dict(self):
        dictionary = {"test": None,
                      "test2": "not none",
                      "test3": {"nested": None, "nested2": "not none"}}

        clean = utils.remove_none_from_dict(dictionary)

        expected = {"test2": "not none", "test3": {"nested2": "not none"}}
        self.assertEqual(clean, expected)

    def test_parse_identity_purl(self):
        purl = 'pkg:job/DEPT/job/USR/job/TEST/job/FOO/job/BAR_BAR/1234/' \
               'artifacts/some_file.txt@1234'

        filename, build_url = utils.parse_purl(purl)

        self.assertEqual(filename, 'some_file.txt')
        self.assertEqual(build_url,
                'job/DEPT/job/USR/job/TEST/job/FOO/job/BAR_BAR/1234')


if __name__ == '__main__':
    unittest.main()
