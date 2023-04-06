
![Logo](https://user-images.githubusercontent.com/59636597/230280708-7cdb4a83-495f-4296-b0a0-ce87f5685632.png)

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
# MasterPannel
Software used for remote file management using protocols SSH and SFTP. Files are securely transferred, copied, and received with all bits of sensitive information secured and encrypted. Features a LAN IP scanner so you can find your computers more easily on a LAN and a client is added for ease of setup on remote computers. You can also recursively deploy files on separate computers and upload multiple files at once. You can save computer information so you don't have to type in the IP, Username, and Password every time like in the CLI.
## Screenshots

![App Screenshot](https://user-images.githubusercontent.com/59636597/230281149-6b8b58da-1514-4a95-beca-923ed0313777.png)

## Installation

Download dependencies:

```bash
  pip install tk

  pip install paramiko

  pip install scp

  pip install subprocess.run
```
Change the directory and install:
```bash
  cd Desktop/

  git clone https://github.com/s5y-ux/MasterPannel

  cd MasterPannel/
  
  python3 main.py
```
