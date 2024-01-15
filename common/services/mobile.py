def serialize_mobile_api(status=True, data={}, msg=""):
    res = {}
    res["result"] = status
    res["msg"] = msg
    res["data"] = data
    return res
