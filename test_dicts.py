SUCCESSFUL_EXPLOIT = {
    "exploit": "CVE-NAME",
    "successful": True
}
UNSUCCCESSFUL_EXPLOIT = {
    "exploit": "CVE-NAME",
    "successful": False
}
OS_DETECTION = {
    "detected_OS": "Windows 7",
    "open_ports": [1, 2, 3],
    "windows_size": [[123,123], [123,123]],
    "other": {"hostname": "test", "ip address": "127.0.0.1", "others": "other"}
}
EXPECTED_SUCCESSFUL_OUTPUT = """{
  "exploit_status": {
    "successful": true, 
    "exploit": "CVE-NAME"
  }, 
  {
    "detected_system": {
      "windows_size": [[123, 123], [123, 123]], 
      "open_ports": [1, 2, 3], 
      "other": ["some weird items"], 
      "detected_OS": "Windows 7"
  }
}"""
EXPECTED_FAILED_OUTPUT = """{
  "exploit_status": {
    "successful": false, 
    "exploit": "CVE-NAME"
  }, 
  {
    "detected_system": {
      "windows_size": [[123, 123], [123, 123]], 
      "open_ports": [1, 2, 3], 
      "other": ["some weird items"], 
      "detected_OS": "Windows 7"
  }
}
"""
