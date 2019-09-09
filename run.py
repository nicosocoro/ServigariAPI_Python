# Initial configurations
from Configurations import SetUp

# This command must be executed BEFORE IMPORTING ANY HIGH LEVEL FILE
# Set stuff such as: Root path (to manage imports)
SetUp.Initial()

from Services import app

app.run(host='0.0.0.0', port=5000, debug=True)


