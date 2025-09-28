import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score


def kmeans_cluster(X_scaled, values_of_k=range(2, 11)):
    inertias, silhouettes, models = [], [], {}

    # Loop through all the k_values:
    for k in values_of_k:
        km = fit_model(X_scaled, k, models)
        inertias.append(km.inertia_)
        silhouettes.append(silhouette_score(X_scaled, km.labels_))

    results = pd.DataFrame({
        "k": list(values_of_k),
        "inertia": inertias,
        "silhouette": silhouettes
    })
    return results, models


def fit_model(X_scaled, k, models):
    km = KMeans(n_clusters=k, n_init=10, random_state=42)
    km.fit(X_scaled)
    models[k] = km
    return km


def best_k(results: pd.DataFrame) -> int:
    return int(results.loc[results["silhouette"].idxmax(), "k"])
