import pandas as pd
import numpy as np
from project.model import kmeans_cluster, best_k
from sklearn.preprocessing import StandardScaler


def test_kmeans_cluster_and_bestk():
    # Small fake dataset
    X = pd.DataFrame({"x": [1, 2, 3, 10, 11, 12], "y": [1, 2, 3, 10, 11, 12]})
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    results, models = kmeans_cluster(X_scaled, range(2, 5))
    assert not results.empty
    assert set(results.columns) == {"k", "inertia", "silhouette"}
    assert all(k in models for k in [2, 3, 4])

    k = best_k(results)
    assert isinstance(k, int)
    assert k in results["k"].values
