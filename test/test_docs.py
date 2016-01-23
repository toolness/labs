import os
import unittest
import subprocess

from .pydoctest import convert_to_pydoctest

MY_DIR = os.path.abspath(os.path.dirname(__file__))
ROOT_DIR = os.path.normpath(os.path.join(MY_DIR, '..'))
PYDOCTEST_DIR = os.path.join(MY_DIR, 'pydoctests')

if not os.path.exists(PYDOCTEST_DIR):
    os.mkdir(PYDOCTEST_DIR)

def create_doctest_method(filename):
    def test_method(self):
        self.assertDoctestWorks(filename)
    return test_method

class DoctestTestCaseMeta(type):
    def __new__(cls, name, parents, dct):
        doctest_dir = dct['DOCTEST_DIR']
        doctest_ext = dct['DOCTEST_EXT']
        doctest_filenames = [
            os.path.basename(filename)
            for filename in os.listdir(doctest_dir)
            if filename.endswith(doctest_ext)
        ]

        for filename in doctest_filenames:
            doctest_name = os.path.splitext(filename)[0]
            dct['test_%s' % doctest_name] = create_doctest_method(filename)
        return super(DoctestTestCaseMeta, cls).__new__(cls, name,
                                                       parents, dct)

class Tests(unittest.TestCase):
    __metaclass__ = DoctestTestCaseMeta

    DOCTEST_DIR = os.path.join(ROOT_DIR, 'docs')
    DOCTEST_EXT = '.md'

    def shell(self, cmdline):
        try:
            subprocess.check_output(cmdline, shell=True,
                                    stderr=subprocess.STDOUT)
        except subprocess.CalledProcessError, e:
            print "Running %s failed! Output:\n%s" % (repr(cmdline),
                                                      e.output)
            raise e

    def assertDoctestWorks(self, filename):
        pdt = '%s.pydoctest' % filename
        convert_to_pydoctest(os.path.join(self.DOCTEST_DIR, filename),
                             os.path.join(PYDOCTEST_DIR, pdt))
        self.shell('docker-compose stop && docker-compose rm -f')
        self.shell('docker-compose run home python '
                   'test_in_container.py pydoctests/%s' % pdt)

if __name__ == '__main__':
    unittest.main()
