# Configure the Consul provider
provider "consul" {
  address    = "127.0.0.1:8300"
  datacenter = "dc1"
}

resource "local_file" "foo" {
    content     = "foo!va"
    filename = "${path.module}/foo.bar"
}

terraform {
  backend "http" {
    address = "http://127.0.0.1:5000/vm"
    # lock_address = "http://127.0.0.1:5000/vm/lock"
    # unlock_address = "http://127.0.0.1:5000/vm/unlock"
  }
}