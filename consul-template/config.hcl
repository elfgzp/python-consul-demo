consul {
  address = "127.0.0.1:8500"

}


template {

  source = "./config.py.ctmpl"
  destination = "../python-web-service/config.py"
  command = "docker restart python-web-service_python-web-service_1"

}