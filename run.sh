pyenv install 3.9.0
pyenv local 3.9.0
git clone https://github.com/sellisd/gitrepodb.git
cd gitrepodb
python3 -m pip install -e .
cd ..
python3 -m pip install -r requirements.txt
mkdir data
# Get repositories and Run analysis
gitrepodb init --name ./repositories.db --overwrite \
    && gitrepodb query --project jupyter --head 100 \
    && gitrepodb add --basepath ./data \
    && gitrepodb download --project jupyter

python ./jupyter_language.py ./data
