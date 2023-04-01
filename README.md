# Prerequisites
-  Python3
-  Pip3
-  Source code

<br />

# Setup
## Virtual Environment
Setup the virtual environment
```bash
# install virtualenv using pip3
pip3 install virtualenv

# venv folder will be created in the root directory
python3 -m venv venv

# activate the virtual env - for Unix/Linux
source ./venv/bin/activate

# (or)

# activate the virtual env - for Windows
.\venv\Scripts\activate.bat // cmd
.\venv\Scripts\activate.ps1 // Powershell
```

## Install Dependencies
```bash
pip3 install -r requirements.txt
```
<br />

# Execution

```python
python3 main.py
```
<br />

# Output

Results from both incarnations will be displayed on every run. Output will be displayed in
- Through console (textual output)
- An output.xml file

<br/>

# Testing

Execute the following command to run all unit test cases under the /tests folder.
```python
python3 -m coverage run -m unittest
```

## Coverage Report 
The following command gives an overview of the code coverage. To be run after running above command.
```python
python3 -m coverage report
```
<br />


# Pylint
Pylint enforces the best coding practices and ensures that the PEP 8 guidelines are followed. Run the command below to check for the code quality.
```bash
pylint *.py
``` 
<br />

# Pydoc
To generate html file for each python file run the following command in command prompt.
```bash
python -m pydoc -w <file address>
```
To Start a HTTP server on an arbitrary unused port and open a web browser to interactively browse documentation.
```bash
python -m pydoc -b
```

<br />

# Generate the LaTeX report

-   Install TeX Live on Windows
    https://www.tug.org/texlive/
    
    (or)
    
-   Install MacTex on macOs
    https://www.tug.org/mactex/mactex-download.html
    
 -   Install the __LaTeX Workshop__ extension ([Marketplace](https://marketplace.visualstudio.com/vscode)).
 
 -  Compile and preview.
 -  Pre-compiled report available under the /latex directory

<br />

# License

[MIT](https://choosealicense.com/licenses/mit/)
