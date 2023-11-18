# Titanic deploy example

This is a repo containing a deployment example of
a model trained to predict the probability of person's
survival on the Titanic ship.

The data used can be found at [Kaggle](https://www.kaggle.com/competitions/titanic/data).

## Code overview

The `main.ipynb` notebook file contains the original
solution for the model alongside with the sample to test
the model's server API (at the very bottom of the file).
The basic catboost model with simple preprocessing steps
was used to shortcut all the actual ML nuances.

The original `main.ipynb` was then refactored into the
`train_model.py` file. All the classes were put in the
`src` folder.

The `models` folder contains the pickled instances
of the trained and fitted models and preprocessors.

The `servers` folder has two servers in it: the frontend
server with the basic `streamlit` frontend and the `fastapi`
model API server run with `uvicorn`. Both have the `Dockerfile`-s
in them. The frontend's server also includes a small
`frontend_src` folder for the UI.

The `data` folder includes the data from [Kaggle](https://www.kaggle.com/competitions/titanic/data).


## Running the servers

The expected way to run is to make use of the `docker compose` from the
repository's root:

```bash
docker compose up --build
```

**Note** that in this `docker-compose` the `model`'s server is also available
from the "outside" on port `8000`. The change that and make it unavailable
while being available for the `frontend` server, remove the ports of the
`model_server` from the `docker-compose.yaml` file.

You can also run the servers in separate:

### Model server

```bash
docker build -f servers/model_server/Dockerfile -t model_server . 
docker run -p 8000:8000 model_server
```

### Frontend server

```bash
docker build -f servers/frontend_server/Dockerfile -t frontend_server .
docker run -p 80:8501 frontend_server
```