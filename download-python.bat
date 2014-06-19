@echo off
if defined ProgramFiles(x86) (
	https://www.python.org/ftp/python/2.7.7/python-2.7.7.amd64.msi
) else (
    explorer https://www.python.org/ftp/python/2.7.7/python-2.7.7.msi
)