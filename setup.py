from setuptools import find_packages, setup

setup(
    name="mlflow-webhdfs",
    version="0.0.1",
    description="MLflow WebHDFS Plugins",
    packages=find_packages(),
    install_requires=[
        "mlflow",
        "hdfs",
    ],
    entry_points={
        "mlflow.artifact_repository": [
            "webhdfs=store.artifact.webhdfs_artifact_repo:WebHdfsArtifactRepository",
        ],
    }
)
