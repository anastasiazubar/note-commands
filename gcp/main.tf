terraform {
  backend "local" {
  }
}

resource "google_iap_brand" "project_brand" {
  support_email     = ""
  application_title = " Search Ads 360 API"
  project           = ""
}

resource "google_iap_client" "project_client" {
  display_name = "Test"
  brand        =  google_iap_brand.project_brand.name
}