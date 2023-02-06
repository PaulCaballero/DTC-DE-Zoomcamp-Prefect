import prefect
#from prefect.environments import LocalEnvironment
from prefect.filesystems import GitHub

# Connect to the GitHub API and fetch the flow file
flow_file = prefect.utilities.github.read_file_from_repo(
    repo="https://github.com/PaulCaballero/DTC-DE-Zoomcamp-Prefect",
    path="flows/02_gcp/etl_web_to_gcs.py",
    ref="master"
)

# Create a flow object from the fetched flow file
flow = prefect.Flow.from_yaml(flow_file)

# Create a GitHub storage block
github_storage = GitHub(
    repo="https://github.com/PaulCaballero/DTC-DE-Zoomcamp-Prefect",
    path="flows/02_gcp/etl_web_to_gcs.py",
    secrets=["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"],
    ref="master"
)

# Assign the GitHub storage block to the flow
flow.storage = github_storage

# Set the flow's environment to the local environment
flow.environment = LocalEnvironment()

# Deploy the flow
flow.deploy(project_name="Prefect-Zoomcamp")