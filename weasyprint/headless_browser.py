"""
    WeasyPrint
    ==========

    WeasyPrint converts web documents to PDF.

    The public API is what is accessible from this "root" packages
    without importing sub-modules.

    :copyright: Copyright 2011-2020 Simon Sapin and contributors, see AUTHORS.
    :license: BSD, see LICENSE for details.

"""

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities


class FakeChrome(object):
    _browser = None

    def __new__(cls, executable_path="chromedriver", **kwargs):
        if cls._browser is None:
            options = kwargs.pop('options', webdriver.ChromeOptions())
            if kwargs.pop('headless', False):
                options.add_argument('headless')
            options.add_argument(f"--width={kwargs.pop('width', 2480)}")
            options.add_argument(f"--height={kwargs.pop('height', 3508)}")
            options.add_argument('--allow-file-access-from-files')

            dc = kwargs.pop('desired_capabilities', DesiredCapabilities.CHROME)
            if 'goog:loggingPrefs' not in dc:
                dc['goog:loggingPrefs'] = {'browser': 'ALL'}
            cls._browser = webdriver.Chrome(
                executable_path,
                chrome_options=options,
                desired_capabilities=dc,
                **kwargs
            )
        return cls._browser


class FakeFirefox(object):
    _browser = None

    def __new__(cls, executable_path="geckodriver", **kwargs):
        if cls._browser is None:
            options = kwargs.pop('options', webdriver.FirefoxOptions())
            if kwargs.pop('headless', False):
                options.add_argument('-headless')
            # options.add_argument(f"--width={kwargs.pop('width', 2480)}")
            # options.add_argument(f"--height={kwargs.pop('height', 3508)}")

            dc = kwargs.pop('desired_capabilities', DesiredCapabilities.FIREFOX)
            # if 'loggingPrefs' not in dc:
            #     dc['loggingPrefs'] = {'browser': 'ALL'}
            cls._browser = webdriver.Firefox(
                executable_path,
                firefox_options=options,
                desired_capabilities=dc,
                **kwargs
            )
        return cls._browser
