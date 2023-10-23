# Abalone Project

This project consists of predicting the age of an abalone based on various physical attributes, such as their measurements and weight.

## Team

Pierre de la Belliere, Etienne du Fayet, Timothé Gypteau, Sophie Marchal, François Moreau, Mathieu Nordin

## Project Goals

The primary goals of this project are:

- Showcase best practices in MLOps, demonstrating how to structure, automate, and manage a machine learning project effectively.
- Provide a complete workflow for age prediction of abalones, covering data exploration, model development, and deployment.
- Offer a clear example of how to use Prefect for workflow orchestration and management in a data science project.
- Demonstrate the deployment of a machine learning model as a Dockerized API for real-world use.

By exploring this project, you will gain insights into how to implement MLOps practices, effectively manage data workflows, and deploy machine learning models for practical applications.

Feel free to navigate through the project's sections, including the notebooks, Prefect workflows, and Dockerized API, to understand each aspect and how they come together to accomplish the project's objectives.

## Prerequesites

Before you begin, ensure you have the following prerequisites in place:

- Python Installation: Make sure Python is installed on your computer. If you haven't installed Python, you can download it from the official website: https://python.org
- Virtual Environment Tool: You can use a virtual environment tool to manage project dependencies. We recommend either of the following options:
    * ["virtualvenv"](https://learnpython.com/blog/how-to-use-virtualenv-python/)
    * [anaconda](https://www.anaconda.com/download)

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

## Structure

The project is organized into three main sections, each serving a specific purpose in implementing MLOps practices:

1. **Notebooks**:
   - This section contains Jupyter notebooks for exploratory data analysis (EDA) and model development. You can use these notebooks to gain insights into the dataset and build, train, and evaluate machine learning models.

   - **Notebooks Included**:
     - `eda.ipynb`: An Exploratory Data Analysis notebook to examine and understand the data.
     - `modelling.ipynb`: A Model Development notebook to build and train the age prediction model.

2. **Prefect Flows**:
   - This section showcases the implementation of workflow orchestration using Prefect. Prefect is used to define, schedule, and execute workflows, providing a framework for managing the entire data pipeline, including data extraction, transformation, and loading (ETL), and model training.

   - **Flows Included**:
     - `workflow.py`: Prefect flow for data ETL processes.
     - `train_model_workflow.py`: Prefect flow for training machine learning models.

3. **App Dockerized through an API**:
   - In this section, the project's machine learning model is deployed as a Dockerized API, allowing you to interact with the model via RESTful API endpoints. The Dockerized API provides an easy way to serve the model for predictions, making it accessible for use in different applications.

   - **Components Included**:
     - `Dockerfile`: The Dockerfile for building the Docker image.
     - `app.py`: The Python script defining the API using Flask.
     - `requirements.txt`: The list of dependencies for the API.
     - `run_docker_api.sh`: A script to build and run the Docker container for the API.

By following the project's structure, you can explore EDA, model development, workflow orchestration with Prefect, and serving the model through a Dockerized API, all while implementing MLOps best practices.

## Deploying the App Using Docker

To deploy the Abalone Age Prediction app, you can use Docker to containerize the application. Follow these steps to build a Docker image and run it:

### Build a Docker Image

1. **Navigate to the App Directory**:
   Change your current working directory to the directory containing the app files. For example:

   ```bash
   cd src/web_service/
   ```

2. **Build the Docker image**:
    Use the docker build command to create a Docker image for the app.

    ```bash
    docker build -t image_name .
    ```

3. **Run the Docker Container**:
    After building the Docker image, you can run it as a container using the docker run command. Specify the port to expose on your host machine (e.g., 8501) and link it to the port exposed by the container (also 8501). Replace image_name with the name you provided when building the image.

    ```bash
    docker run -p 8501:8501 image_name
    ```

4. **Access the app**:
    Open your web browser and type either of the following URLs to start using the Abalone Age Prediction app:
        http://0.0.0.0:8000
        http://localhost:8000
    This will launch the app, allowing you to interact with it and make age predictions based on the provided data.

## Prefect integration and MLOps flows

The Abalone Age Prediction Project uses Prefect to define and orchestrate workflow processes. Prefect is a powerful tool for managing data workflows, including data extraction, transformation, and loading (ETL), and model training.

### ETL Flow

The ETL (Extract, Transform, Load) flow is defined to manage the data pipeline. This flow ensures that data is extracted, preprocessed, and made ready for model training. The key components of the ETL flow include:

- Data Extraction: Fetching the Abalone dataset from the `data` folder.
- Data Transformation: Preprocessing the data, including feature engineering and splitting it into training and testing sets.
- Data Loading: Saving the transformed data for model training.

### Execution

To run the ETL flow, execute the following command in the project directory:

```bash
python workflow.py
```
### Model training flow

The Model Training flow is designed to facilitate model development and training. This flow orchestrates the process of training machine learning models using the preprocessed data from the ETL flow.

To initiate the Model Training flow, execute the following command in the project directory:

```bash
train_model_workflow()
```

### Predict flow

Additionally, you can also run the bash_predic_work.flow function to perform predictions.

To do so, execute the following command:

```bash
bash_predict_workflow()
```






