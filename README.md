
# Campus Food Menu Server

Welcome to the Campus Food Menu Server, which is the supportive project of our Campus Food Menu Project.

---


[TODO]

## Contents


- [Getting Started](#getting-started)




# 1. Introduction
Welcome to the Campus Food Menu Server, which is the supportive project of our Campus Food Menu Project.


# 2. Citation

If you use our code or datasets from `https://github.com/EnzeXu/Campus_Food_Menu_Server` for academic research, please cite the following paper:

Paper BibTeX:

```
@article{xxx2024xxxxxx,
  title        = {xxxxx},
  author       = {xxxxx},
  journal      = {arXiv preprint arXiv:xxxx.xxxx},
  year         = {2024}
}
```



# 3. Structure of the Repository

[TODO]

```
Campus Food Menu server
┌── chromedriver/
├────── darwin/
├────────── chromedriver
├────── linux/
├────────── chromedriver
├── saves/
├────── 78390/
├────────── 2024-MM-DD/
├────── 78391/
├────────── 2024-MM-DD/
├── LICENSE
├── README.md
├── requirements.txt
├── notice.py
├── get_cookie.py
├── dump.py
├── const.py
├── clock_send.py
└── utils.py
```

- `chromedriver/`: folder to save chromedriver scripts for different OS.
- `saves/`: folder to save downloaded menu info.
- `LICENSE`: license file.
- `README.md`: readme file.
- `requirements.txt`: main dependent packages (please follow section 4.2 to install all dependent packages).
- `notice.py`: settings of the auto-launcher (time of the day).
- `get_cookie.py`: use selenium package to get a valid cookie.
- `dump.py`: one-time dump the menu info down.
- `const.py`: some constant strings and settings.
- `clock_send.py`: load notice.py and deploy the auto-launcher.
- `utils.py`: some utils.


# 4. Getting Started

This project is developed using Python 3.9+ and is compatible with macOS, Linux, and Windows operating systems.

## 4.1 Preparations

(1) Clone the repository to your workspace.

```shell
~ $ git clone https://github.com/EnzeXu/Invariant_Physics.git
```

(2) Navigate into the repository.
```shell
~ $ cd Invariant_Physics
~/Invariant_Physics $
```

(3) Create a new virtual environment and activate it. In this case we use Virtualenv environment (Here we assume you have installed the `virtualenv` package using you source python script), you can use other virtual environments instead (like conda).

For macOS or Linux operating systems:
```shell
~/Invariant_Physics $ python -m venv ./venv/
~/Invariant_Physics $ source venv/bin/activate
(venv) ~/Invariant_Physics $ 
```

For Windows operating systems:

```shell
~/Invariant_Physics $ python -m venv ./venv/
~/Invariant_Physics $ .\venv\Scripts\activate
(venv) ~/Invariant_Physics $ 
```

You can use the command deactivate to exit the virtual environment at any time.

## 4.2 Install Packages

```shell
(venv) ~/Invariant_Physics $ pip install -r requirements.txt
```





# 5. Questions

If you have any questions, please contact xezpku@gmail.com.
