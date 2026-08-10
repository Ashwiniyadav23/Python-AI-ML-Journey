#pip — Python's package installer
#pip installs third-party packages from PyPI (Python Package Index), the official repository of Python packages.

pip install pandas              # install a package
pip install pandas==1.5.3       # install a specific version
pip install pandas numpy scipy  # install multiple at once
pip uninstall pandas            # remove a package
pip list                        # see everything installed
pip show pandas                 # see details about one package


# Creating a virtual environment with venv (built into Python)

python -m venv myenv          # creates a folder called "myenv" — your isolated environment

# Activate it:
# On Mac/Linux:
source myenv/bin/activate



(myenv) $ pip install pandas    # installed only inside myenv

deactivate                       # exit the environment when done