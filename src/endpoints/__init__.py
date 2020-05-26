"""
Organize all API entrypoints
Author: Po-Chun, Lu

"""
from endpoints.trigger.resource import SparkTrigger

RESOURCES = {"/trigger/spark": SparkTrigger}
