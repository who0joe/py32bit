param(
    [parameter(Position=0)]
    [string]$directory
)

if ($directory) {
    $dir = $directory
} else {
    $dir = "python32"
}

#+-----------------------------------------------------------------------+

# download
Invoke-WebRequest -Uri "https://www.python.org/ftp/python/3.11.3/python-3.11.3-embed-win32.zip" `
-OutFile "python-3.11.3-embed-win32.zip"

# unzip to ./python32
Expand-Archive -Path "python-3.11.3-embed-win32.zip" -DestinationPath "./$dir"

# remove zip file
Remove-Item -Path "python-3.11.3-embed-win32.zip"

# check python version
$pythonExe = Join-Path -Path $dir -ChildPath 'python.exe'
$pythonFinsish = Invoke-Expression "& '$pythonExe' --version" | Out-String
Write-Host $pythonFinsish

#+-----------------------------------------------------------------------+

# get get-pip.py file to current diectory by using curl
curl https://bootstrap.pypa.io/get-pip.py -o ./$dir/get-pip.py

# setup pip correspondent to current python (32bit) interpreter
& ./$dir/python.exe ./$dir/get-pip.py --no-cache-dir --no-compile --no-warn-script-location

# add site-packages to python path
$file = "./$dir/python311._pth"
$content = Get-Content $file
$content[2] += "/Lib/site-packages`r`n"
Set-Content $file $content

# remove get-pip.py file
Remove-Item -Path "./$dir/get-pip.py"

# check pip version
$pipExe = Join-Path -Path $dir -ChildPath 'Scripts/pip.exe'
$pipFinsish = Invoke-Expression "& '$pipExe' --version" | Out-String
Write-Host $pipFinsish

Write-Host "Setup Finished."

# # to install packages
# & $pipExe install --no-warn-script-location `
# pywin32 `
