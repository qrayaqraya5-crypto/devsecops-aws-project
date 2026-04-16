resource "aws_ecr_repository" "devsecops_app" {
  name                 = "devsecops-app"
  image_tag_mutability = "MUTABLE"

  image_scanning_configuration {
    scan_on_push = true
  }

  tags = {
    Project = "devsecops"
  }
}

output "ecr_repository_url" {
  value = aws_ecr_repository.devsecops_app.repository_url
}
