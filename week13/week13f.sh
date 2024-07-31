

# installation, creating a new environment
python3.9 -m venv [myenv]

# activate the environment
source myenv/bin/activate

# deactivate
deactivate

# install
python3.9 -m pip install pandas==2.2.2
python3.9 -m pip install redis

# Freeze, show me the packages used by my code
python3.9 -m pip freeze
python3.9 -m pip freeze > requirements.txt

# Install into another machine/computer
python3.9 -m pip install -r requirements.txt


