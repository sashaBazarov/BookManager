import unittest

if __name__ == '__main__':
    # Ищет все тесты в папке `tests`
    loader = unittest.TestLoader()
    suite = loader.discover(start_dir='tests')

    runner = unittest.TextTestRunner()
    runner.run(suite)
