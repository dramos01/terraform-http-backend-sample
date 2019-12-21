resource "local_file" "foo" {
    content     = "foo!vaa"
    filename = "${path.module}/foo.bar"
}

terraform {
  backend "http" {
    address = "http://127.0.0.1:5000/vm"
    lock_address = "http://127.0.0.1:5000/vm/lock"
    unlock_address = "http://127.0.0.1:5000/vm/unlock"
  }
}