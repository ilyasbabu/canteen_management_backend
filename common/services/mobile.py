import sys
import traceback
import cloudinary.uploader

from django.core.exceptions import ValidationError
from ..constants import ERROR_MSG


def serialize_mobile_api(status=True, data={}, msg=""):
    res = {}
    res["result"] = status
    res["msg"] = msg
    res["data"] = data
    return res


def handle_error(e):
    msg = ERROR_MSG
    error_info = "\n".join(traceback.format_exception(*sys.exc_info()))
    print(error_info)
    if isinstance(e, ValidationError):
        error_info = "\n".join(e.messages)
        msg = e.messages
    return msg


def upload_image(image):
    result = cloudinary.uploader.upload(image, folder="/canteen_management")
    return result["secure_url"]
