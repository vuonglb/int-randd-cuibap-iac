from abc import get_cache_token
from constructs import Construct
from cdktf import App

from cloud_function_stack import CloudFunctionStack

GCP_PROJECT_NAME = "gcp-project-name"

app = App()
t =CloudFunctionStack(app, "vuonglb", GCP_PROJECT_NAME)

app.synth()