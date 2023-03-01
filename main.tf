terraform {
  backend "remote" {
    organization = "inzynierka-agh-cyber"

    workspaces {
      name = "inzynierka-prd"
    }
  }
}

resource "null_resource" "example" {
  triggers = {
    value = "A example resource that does nothing!"
  }
}