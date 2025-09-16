import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score


def kmeans_cluster(X_scaled, k_values=range(2, 11)):
    inertias, silhouettes, models = [], [], {}

    for k in k_values:
        km = KMeans(n_clusters=k, n_init=10, random_state=42)
        km.fit(X_scaled)
        models[k] = km
        inertias.append(km.inertia_)
        silhouettes.append(silhouette_score(X_scaled, km.labels_))

    results = pd.DataFrame({
        "k": list(k_values),
        "inertia": inertias,
        "silhouette": silhouettes
    })
    return results, models


def best_k(results: pd.DataFrame) -> int:
    return int(results.loc[results["silhouette"].idxmax(), "k"])
