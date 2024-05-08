
# Campus Food Menu - Backend

Welcome to the Campus Food Menu - Backend, which is the supportive project of our Campus Food Menu - Frontend Project.

---


## Contents

- [Introduction](#1-introduction)
- [Citation](#2-citation)
- [Structure of the Repository](#3-structure-of-the-repository)
- [Getting Started](#4-getting-started)
- [Launch the auto-script](#5-launch-the-auto-script)
- [Screenshots](#6-screenshots)
- [Questions](#7-questions)

---


# 1. Introduction
Welcome to the Campus Food Menu Backend, which is the supportive project of our Campus Food Menu Project.


# 2. Citation

If you use our code or datasets from `https://github.com/EnzeXu/Campus_Food_Menu_Backend` for academic research, please cite the following paper:

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
Campus Food Menu Backend
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
~ $ git clone https://github.com/EnzeXu/Campus_Food_Menu_Backend.git
```

(2) Navigate into the repository.
```shell
~ $ cd Campus_Food_Menu_Backend
~/Campus_Food_Menu_Backend $
```

(3) Create a new virtual environment and activate it. In this case we use Virtualenv environment (Here we assume you have installed the `virtualenv` package using you source python script), you can use other virtual environments instead (like conda).

For macOS or Linux operating systems:
```shell
~/Campus_Food_Menu_Backend $ python -m venv ./venv/
~/Campus_Food_Menu_Backend $ source venv/bin/activate
(venv) ~/Campus_Food_Menu_Backend $ 
```

For Windows operating systems:

```shell
~/Campus_Food_Menu_Backend $ python -m venv ./venv/
~/Campus_Food_Menu_Backend $ .\venv\Scripts\activate
(venv) ~/Campus_Food_Menu_Backend $ 
```

You can use the command deactivate to exit the virtual environment at any time.

## 4.2 Install Packages

```shell
(venv) ~/Campus_Food_Menu_Backend $ pip install -r requirements.txt
```

# 5 Launch the auto-script

```shell
(venv) ~/Campus_Food_Menu_Backend $ python clock_send.py
```

# 6. Screenshots

![23851715196380_ pic](https://github.com/EnzeXu/Campus_Food_Menu_Backend/assets/90367338/9d528c71-d590-48fb-97aa-f76874b2b6b0)
![23841715196345_ pic](https://github.com/EnzeXu/Campus_Food_Menu_Backend/assets/90367338/c6daf44f-298e-4a9b-8908-a5de4da63d8f)
![23861715196615_ pic](https://github.com/EnzeXu/Campus_Food_Menu_Backend/assets/90367338/d351947d-3c78-4ff1-858e-1c9ae4aacffa)


# 7. Questions

If you have any questions, please contact xezpku@gmail.com.
