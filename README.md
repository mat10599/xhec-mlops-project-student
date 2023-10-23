# Abalone Project

## Description
The goal of this repository is to implement MlOps practices.

## Prerequesites
- Install python on your computer
- ["virtualvenv"](https://learnpython.com/blog/how-to-use-virtualenv-python/) package or [anaconda](https://www.anaconda.com/download).
## Installation 

1) Clone the repository.
2) Create a `data` folder at the root of the repository and put the file `abalone.csv` in it. The `abalone.csv` file can be downloaded at this [link](https://www.kaggle.com/datasets/rodolfomendes/abalone-dataset).
3) Install requirements 
   - For anaconda users
    1) ```bash 
        conda create --name myenv python=3.8  # creates the environment
        ```
    2)  ```bash 
        conda create --name myenv python=3.8  # activates the environment
        ```
    3)  ```bash 
        conda install --file requirements.in # install the required packages
        ```
    - For virtualvenv users

    1) ```bash
        # On Windows
        python -m venv myenv
        # On macOS and Linux        # creates the environment
        python3 -m venv myenv
    2)  ```bash 
        # On Windows
        myenv\Scripts\activate
        # On macOS and Linux            # activates the environment
        source myenv/bin/activate

    3)  ```bash 
        pip install pip-tools       # pip-tools is required to run requirements.in
        ```

    4) ```bash 
        pip install pip-tools
        ```


  

  