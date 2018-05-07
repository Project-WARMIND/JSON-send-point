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
    "open_ports": [1, 2, 3],
    "windows_size": [[123,123], [123,123]],
    "other": ["some weird items"]
}
EXPECTED_SUCCESSFUL_OUTPUT = """{
  "exploit status": {
    "successful": true, 
    "exploit": "CVE-NAME"
  }, 
  {
    "detected system": {
      "windows_size": [[123, 123], [123, 123]], 
      "open_ports": [1, 2, 3], 
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
      "windows_size": [[123, 123], [123, 123]], 
      "open_ports": [1, 2, 3], 
      "other": ["some weird items"], 
      "detected OS": "Windows 7"
  }
}
"""