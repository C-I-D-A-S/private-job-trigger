"""
Module for API arguments config
Author: Po-Chun, Lu

"""


def add_post_args(post_parser):
    """ defining post arguments
    """
    post_parser.add_argument(
        "job_id",
        type=str,
        required=True,
        location="json",
        help="job_id parameter should be list",
    )

    post_parser.add_argument(
        "job_type",
        type=str,
        required=True,
        location="json",
        help="job_type parameter should be list",
    )

    post_parser.add_argument(
        "job_params",
        type=dict,
        required=True,
        location="json",
        help="job_params parameter should be list",
    )

    post_parser.add_argument(
        "job_times",
        type=dict,
        required=True,
        location="json",
        help="job_time parameter should be list",
    )

    post_parser.add_argument(
        "job_resources",
        type=dict,
        required=True,
        location="json",
        help="job_resources parameter should be list",
    )
