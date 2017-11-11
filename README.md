# Goshen Trains

This project uses data collected at https://sites.google.com/site/goshentrains/ by Douglas Miller. Check out his site to see some really interesting techniques and other analysis.

## Files

### Load

This file scrapes the directory listing of the csv for a list of csvs. It then compares the list against the list of csvs already pulled, and adds any new ones to the dataframe. The dataframe is saved to `data/trains.pkl`, and can be loaded into other files.

### MakeModel

This file loads the data, preprocesses it, and uses a Random Forest Classifier to build a model. It saves the model to the models folder, with some identifiers in the name about how the model was built and the date. It also outputs some model accuracy analysis.

### Explore

Some basic data exploration

### PredictForTime

Loads the model, and predicts whether a train is present or not for a given time (default now)

### Flask app

```
$ python app.py
```

Open http://localhost:5000/prediction/

### Deploying to heroku

First, install the heroku command line tools.

Setup:

```
$ heroku login
$ heroku git:remote -a is-it-training
```

Deploying:

```
$ git push heroku master
```
