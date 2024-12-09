provider "google" {
  project = "your-project-id"
  region  = "us-central1"
}

resource "google_compute_firewall_policy" "test_policy" {
  name = "test-firewall-policy"
  description = "A test firewall policy"

  # The default rule that applies to all traffic
  rule {
    action = "allow"
    direction = "INGRESS"
    priority = 1000
    source_ranges = ["0.0.0.0/0"]
    target_tags = ["test-tag"]

    match {
      versioned_expr = "SRC_IPS_V4"
      config {
        src_ip_ranges = ["0.0.0.0/0"]
      }
    }
  }
}

# This will create a firewall rule that uses the firewall policy
resource "google_compute_firewall" "apply_firewall_policy" {
  name    = "apply-firewall-policy"
  network = "projects/your-project-id/global/networks/your-network-name"

  firewall_policy = google_compute_firewall_policy.test_policy.id
}
