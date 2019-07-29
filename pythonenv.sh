if [[ ! -d "venv" ]]; then
    #statements
    virtualenv -p python3 venv
    echo "Create an virtual environment named 'venv'"
fi
