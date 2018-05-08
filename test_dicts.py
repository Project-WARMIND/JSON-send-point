SUCCESSFUL_EXPLOIT = {
    "exploit": "CVE-NAME",
    "successful": True
}
UNSUCCCESSFUL_EXPLOIT = {
    "exploit": "CVE-NAME",
    "successful": False
}
OS_DETECTION = {
    "detected OS": "Windows 7",
    "open ports": [1, 2, 3],
    "windows size": [[123,123], [123,123]],
    "other": {"hostname": "test", "ip_address": "127.0.0.1", "others": "other"}
}
EXPECTED_SUCCESSFUL_OUTPUT = """{
  "exploit status": {
    "successful": true, 
    "exploit": "CVE-NAME"
  }, 
  {
    "detected system": {
      "windows size": [[123, 123], [123, 123]], 
      "open ports": [1, 2, 3], 
      "other": ["some weird items"], 
      "detected OS": "Windows 7"
  }
}"""
EXPECTED_FAILED_OUTPUT = """{
  "exploit status": {
    "successful": false, 
    "exploit": "CVE-NAME"
  }, 
  {
    "detected system": {
      "windows size": [[123, 123], [123, 123]], 
      "open ports": [1, 2, 3], 
      "other": ["some weird items"], 
      "detected OS": "Windows 7"
  }
}
"""