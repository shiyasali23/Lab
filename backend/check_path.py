import sys
import os

# Add the directory containing 'services' to the Python path
services_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'services'))
if services_dir not in sys.path:
    sys.path.append(services_dir)

print("Updated Python Path:")
for path in sys.path:
    print(path)
