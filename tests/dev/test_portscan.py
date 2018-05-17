import unittest
import mock
from click.testing import CliRunner
import yoda
from modules import dev

class PortScanTest(unittest.TestCase):
    """
          Test for the following commands:

          | Module: dev
          | command: portscan
      """

    def __init__(self, methodName='runTest'):
        super(PortScanTest, self).__init__()
        self.runner = CliRunner()


    def runTest(self):
        result = self.runner.invoke(yoda.cli, ['dev','portscan'],input='github.com')
        self.assertEqual(result.exit_code, 0)