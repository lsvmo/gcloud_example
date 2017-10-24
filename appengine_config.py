import os
import sys

if os.environ.get('SERVER_SOFTWARE', '').startswith('Google App Engine'):
    pass
else:
    if os.name == 'nt':
        os.name = None
        sys.platform = ''