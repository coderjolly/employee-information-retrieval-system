# Information Retrieval System

A flask application that makes use of MVC architecture along with a front-end for rendering results. The application accepts various inputs from users, and returns the requested query or the information related to the query. The front-end is handlred via a html interface and the inputs from the user are converted in parameters for the query whilst maintaining the backend server to handle more queries as well. 

This project aims to use various **ETL** techniques and manipulations for *cleaning*, *indexing*, *extracting* and *loading* the dataset for running various user defined queries on the dataset.

## What is MVC ?

MVC stands for Model-View-Controller, which is a software architectural pattern commonly used in designing and developing user interfaces for web applications. It separates the application into three interconnected components:

- Model: The Model represents the data and business logic of the application. It encapsulates the data and provides methods to manipulate that data.
- View: The View is responsible for presenting the user interface to the user. It displays the data from the model to the user and sends user actions to the controller for processing.
- Controller: The Controller acts as an intermediary between the Model and the View. It receives input from the user via the View, processes that input , and updates the View accordingly.

## Installation

Whenever dealing with python based applications, it is a very good practice to make a virtual environment and then deal with the process of installing libraries and dependencies as the installation then affects one particular environment. One can use any virtual environment to inilise this project by either using `venv` or `conda`.

Next, we need to make sure that our dependies are in order, so we will use the following command to run the requirements for this project. The command is as follows:

```zsh
(nyei) ➜  information-retrieval-system pip install -r requirements.txt
```

After the successfull installation of the libraries and dependencies, we will proceed forward to run the application by running the server from `app.py`. The command is as follows:

```zsh
(nyei) ➜  information-retrieval-system python3.8 app.py
```
Following this, a prompt will be generated asking to route the attention to `locahost:5000` which is the default server address for this application rendering a front-end to interact with the user.

## Preview

The application loads at the Index page that has the options to choose from like viewing the db, finding an employee through an id or borough index and seeing the top-earners.

#### Homepage
![index](/ss/index.png)

#### Employees List
![employee-db](/ss/employee-db-list.png)

#### Find Employees through ID
![find-employee-id](/ss/find-employee-id.png)

#### Find Employees through Borough Index
![find-employee-borough](/ss/find-employee-borough.png)

#### Find the Top-Earners year-wise
![top-earners](/ss/top-earners.png)