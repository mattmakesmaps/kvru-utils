# REF: https://docs.python-guide.org/writing/structure/#test-suite
import os
import sys

package_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, package_path)

import mp3convertpackage