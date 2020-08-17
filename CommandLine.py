import sys
# The `sys` module offers access to variables and methods closely tied to the Python interpreter.

sys.platform
sys.byteorder
sys.version_info
sys.version
sys.api_version

import os
#
os.getcwd()
os.chdir('/tmp')
os.environ.get('LOGLEVEL')
os.environ['LOGLEVEL'] = 'DEBUG'
# os.getlogin()

import subprocess
#
cp = subprocess.run(['ls', '-l'], capture_output=True, universal_newlines=True)
print(cp.stdout)

cp = subprocess.run(['ls', '/nonexist'],
                    capture_output=True,
                    universal_newlines=True)
print(cp.stderr)

cp = subprocess.run(
    ['ls', '/notexist'],
    capture_output=True,
    universal_newlines=True,
    check=True
)  # check - raises an exception if the subprocess reprots an error
print(cp)


