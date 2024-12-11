import unittest
from emulator import ShellEmulator

class TestShellEmulator(unittest.TestCase):
    def setUp(self):
        self.emulator = ShellEmulator('config.toml')

    def test_ls(self):
        self.emulator.ls()

    def test_cd(self):
        self.emulator.cd('some_directory')

    def test_exit(self):
        with self.assertRaises(SystemExit):
            self.emulator.exit()

    def test_chown(self):
        self.emulator.chown('new_owner', 'file.txt')

    def test_head(self):
        self.emulator.head('file.txt')

    def test_cp(self):
        self.emulator.cp('source.txt', 'destination.txt')

if __name__ == '__main__':
    unittest.main()