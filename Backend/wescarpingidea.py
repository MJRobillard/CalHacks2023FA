from utilities import print_emotions

from hume import HumeBatchClient
from hume.models.config import NerConfig

client = HumeBatchClient("<your-api-key>")

# Submit the obama.txt file from the local disk
files = ["obama.txt"]
config = NerConfig()
job = client.submit_job([], [config], files=files)

print("Running...", job)
job.await_complete()
print("Job completed with status: ", job.get_status())