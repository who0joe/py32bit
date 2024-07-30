# 32bit Python(3.11.3) Template

Embeded Python (for Windows) Interpreter  ***32bit***   


> ### Python 3.11.3 - April 5, 2023    
> **Note that Python 3.11.3 cannot be used on Windows 7 or earlier.**
>
> [Download Windows embeddable python-3.11.3 (32-bit)](https://www.python.org/ftp/python/3.11.3/python-3.11.3-embed-win32.zip)  
> [Find Another Version](https://www.python.org/downloads/windows/)

## How to Setup
1. Open Powershell
2. Move to working directory
3. Just run setup_python32.ps1 

```powershell
# Optionally you can change folder name by sending paramter.Default is "python32"
.\setup_python32.ps1 {FolderName}
```

### To use 32bit python interpreter

Please note that the embedded Python used here is not registered in the environment variable, so you must specify the path directly.

```powershell
> ./{FolderName}/python {command}
```

OR

```powershell
> cd {FolderName}
> ./python {command}
```

---
### Check

```powershell

# to check python interpreter version
> ./python32/python --version

# to check pip version
> ./python32/python -m pip --version

# execut check.py to check supporting archecture and 
./python32/python ./check.py

```

### Manual Setup
```ps
# download
> Invoke-WebRequest -Uri "https://www.python.org/ftp/python/3.11.3/python-3.11.3-embed-win32.zip" -OutFile "python-3.11.3-embed-win32.zip"

# unzip to ./python32
> Expand-Archive -Path "python-3.11.3-embed-win32.zip" -DestinationPath "./{python32}"

# get get-pip.py file to diectory by using curl
(PowerShell) > Invoke-WebRequest -Uri "https://bootstrap.pypa.io/get-pip.py" -OutFile ".\{python32}\get-pip.py"
(bash) > curl https://bootstrap.pypa.io/get-pip.py -o ./{python32}/get-pip.py

# setup pip correspondent to current python (32bit) interpreter
> ./{python32}/python ./{python32}/get-pip.py

# install pip pywin32 pywinauto
> ./{python32}/python - m pip install pywin32 pywinauto

# run pywin32_postinstall
> ./{python32}/python ./{python32}/Scripts/pywin32_postinstall.py -install

(IMPORTANT)
ADD path "/Lib/site-packages" 
ADD path "/Lib/site-packages/win32"
ADD path "/Lib/site-packages/pythonwin" 
=> At ./python32/python311._pth

# python package download (ex pandas)
pip download 패키지명 -d /폴더경로
ex) pip download pandas -d /path/to/download

# python package install offline
python -m pip install 파일명.whl -f ./ --no-index

```

- -f ./ 또는 --find-links ./: 이 옵션은 pip에게 패키지를 찾을 추가적인 위치를 지정합니다. 
    여기서는 현재 디렉토리를 지정하고 있습니다. 
    즉, pip는 현재 디렉토리에서 패키지를 찾으려고 시도할 것입니다.
- --no-index: 이 옵션은 pip에게 PyPI (Python Package Index)와 같은 기본 패키지 인덱스를 사용하지 않도록 지시합니다. 
    대신에 -f 옵션으로 지정된 위치에서만 패키지를 찾습니다.


