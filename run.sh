pyenv install 3.9.0
pyenv local 3.9.0
git clone https://github.com/sellisd/gitrepodb.git
cd gitrepodb
python3 -m pip install -e .
mkdir data
# Get repositories and Run analysis
gitrepodb init --name ./repositories.db --overwrite \
    && gitrepodb query --project jupyter --head 100 \
    && gitrepodb add --basepath ./data \
    && gitrepodb download --project jupyter \
    && pycodeseq --input_path ./data --output jupyter.tsv --method cells

python ./jupyter_language.py
