"""
Endpoint Module for handling spark triggering
Author: Po-Chun, Lu

"""
import json
import os

from flask_restful import Resource, reqparse
from flask import current_app as app

from endpoints.trigger.args import add_post_args
from endpoints.utils import log_context


def get_spark_submit_command(args):
    """ generate spark-submit command from arguments
    """
    return f"""\
        spark-submit  \
        --deploy-mode cluster \
        --files /etc/hive/conf/hive-site.xml \
        --conf spark.hadoop.mapreduce.input.fileinputformat.input.dir.recursive=true \
        --conf spark.hive.mapred.supports.subdirectories=true \
        --num-executors {args.job_resources['executors']} \
        --executor-cores {args.job_resources['cpu']} \
        --executor-memory {args.job_resources['mem']}g \
        {app.config['SPARK_SOURCE_FILE']} \
        --job_id {args.job_id} \
        --job_type {args.job_type}  \
        --job_params '{json.dumps(args.job_params)}' \
        --job_times '{json.dumps(args.job_times)}' \
        --job_resources '{json.dumps(args.job_resources)}'
    """


class SparkTrigger(Resource):
    """ /trigger/spark handler

    """

    def __init__(self):
        self.model = None
        self._set_post_parser()

    def _set_post_parser(self):
        self.post_parser = reqparse.RequestParser()
        add_post_args(self.post_parser)

    @staticmethod
    def _execute_cli(args):
        command = get_spark_submit_command(args)
        log_context("Request", {"spark_command": command})
        os.system(command)

    def _post_operate(self, args):
        self._execute_cli(args)

    def post(self):
        """ main handler of post request """
        args = self.post_parser.parse_args()
        self._post_operate(args)

        return {"info": "ok"}
