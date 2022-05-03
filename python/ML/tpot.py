import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from tpot import TPOTClassifier

tpot_config_dict = {
    # Classifiers
    # "sklearn.naive_bayes.GaussianNB": {}, 
    # "sklearn.naive_bayes.BernoulliNB": {
    #     "alpha": [1e-3, 1e-2, 1e-1, 1.0, 10.0, 100.0],
    #     "fit_prior": [True, False],
    # },
    # "sklearn.naive_bayes.MultinomialNB": {
    #     "alpha": [1e-3, 1e-2, 1e-1, 1.0, 10.0, 100.0],
    #     "fit_prior": [True, False],
    # },
    "sklearn.tree.DecisionTreeClassifier": {
        "criterion": ["gini", "entropy"],
        "max_depth": range(1, 11),
        "min_samples_split": range(2, 21),
        "min_samples_leaf": range(1, 21),
    },
    "sklearn.ensemble.ExtraTreesClassifier": {
        "n_estimators": [100],
        "criterion": ["gini", "entropy"],
        "max_features": np.arange(0.05, 1.01, 0.05),
        "min_samples_split": range(2, 21),
        "min_samples_leaf": range(1, 21),
        "bootstrap": [True, False],
    },
    "sklearn.ensemble.RandomForestClassifier": {
        "n_estimators": [100],
        "criterion": ["gini", "entropy"],
        "max_features": np.arange(0.05, 1.01, 0.05),
        "min_samples_split": range(2, 21),
        "min_samples_leaf": range(1, 21),
        "bootstrap": [True, False],
    },
    "sklearn.ensemble.GradientBoostingClassifier": {
        "n_estimators": [100],
        "learning_rate": [1e-3, 1e-2, 1e-1, 0.5, 1.0],
        "max_depth": range(1, 11),
        "min_samples_split": range(2, 21),
        "min_samples_leaf": range(1, 21),
        "subsample": np.arange(0.05, 1.01, 0.05),
        "max_features": np.arange(0.05, 1.01, 0.05),
    },
    # "sklearn.neighbors.KNeighborsClassifier": {
    #     "n_neighbors": range(3, 101),
    #     "weights": ["uniform", "distance"],
    #     "p": [1, 2],
    # },
    # "sklearn.svm.LinearSVC": {
    #     "penalty": ["l1", "l2"],
    #     "loss": ["hinge", "squared_hinge"],
    #     "dual": [True, False],
    #     "tol": [1e-5, 1e-4, 1e-3, 1e-2, 1e-1],
    #     "C": [1e-4, 1e-3, 1e-2, 1e-1, 0.5, 1.0, 5.0, 10.0, 15.0, 20.0, 25.0],
    # },
    # "sklearn.linear_model.LogisticRegression": {
    #     "penalty": ["l1", "l2"],
    #     "C": [1e-4, 1e-3, 1e-2, 3e-2, 1e-1, 0.3, 0.5, 1.0, 5.0, 10.0, 15.0, 20.0, 25.0],
    #     "dual": [False],
    #     "solver": ["liblinear"],
    # },
    "xgboost.XGBClassifier": {
        "n_estimators": [100],
        "max_depth": range(1, 11),
        "learning_rate": [1e-3, 1e-2, 1e-1, 0.5, 1.0],
        "subsample": np.arange(0.05, 1.01, 0.05),
        "min_child_weight": range(1, 21),
        "reg_alpha": [0, 1e-4, 1e-3, 1e-2, 1e-1, 1, 10, 100],
        "reg_lambda": [0, 1e-4, 1e-3, 1e-2, 1e-1, 1, 10, 100],
        "eval_metric": ["logloss"],
    },
    "lightgbm.LGBMClassifier": {
        "learning_rate": [1e-3, 1e-2, 1e-1, 0.5, 1.0],
        "n_estimators": [100],
        "subsample": np.arange(0.05, 1.01, 0.05),
        "reg_alpha": [0, 1e-4, 1e-3, 1e-2, 1e-1, 1, 10, 100],
        "reg_lambda": [0, 1e-4, 1e-3, 1e-2, 1e-1, 1, 10, 100],
    },
    "sklearn.linear_model.SGDClassifier": {
        "loss": ["log", "hinge", "modified_huber", "squared_hinge", "perceptron"],
        "penalty": ["elasticnet"],
        "alpha": [0.0, 0.01, 0.001],
        "learning_rate": ["invscaling", "constant"],
        "fit_intercept": [True, False],
        "l1_ratio": [0.25, 0.0, 1.0, 0.75, 0.5],
        "eta0": [0.1, 1.0, 0.01],
        "power_t": [0.5, 0.0, 1.0, 0.1, 100.0, 10.0, 50.0],
    },
}


X_train, X_test, y_train, y_test = train_test_split(
            X,
            y,
            random_state=42,
            stratify=y,
        )

pipeline_optimizer = TPOTClassifier(
        generations=2,
        population_size=100,
        verbosity=2,
        config_dict=tpot_config_dict,
        template="Classifier",
        scoring="f1_weighted",
        n_jobs=-1,
        use_dask=True,
    )

pipeline_optimizer.fit(X_train, y_train)

# creating the csv containing the cv scores of the tested models
my_dict = list(pipeline_optimizer.evaluated_individuals_.items())
model_scores = pd.DataFrame()
for model in my_dict:
    model_name = model[0]
    model_info = model[1]
    cv_score = model[1].get(
        "internal_cv_score"
    )  # Pull out cv_score as a column (i.e., sortable)
    model_scores = model_scores.append(
        {"model": model_name, "cv_score": cv_score, "model_info": model_info},
        ignore_index=True,
    )

model_name_ext = model_scores["model"].str.extract("(^.*?)\(")
model_scores.insert(0, "model_ext", model_name_ext)
model_scores = model_scores.sort_values("cv_score", ascending=False)
model_scores.to_csv(output_csv_path)

with open(output_path, "wb") as f:
    pickle.dump(pipeline_optimizer.fitted_pipeline_, f)