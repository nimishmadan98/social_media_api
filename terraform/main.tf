provider "aws" {
  region = "us-east-1"  
}

# Create an ECS Cluster
resource "aws_ecs_cluster" "example" {
  name = "fargate-cluster"
}

resource "aws_ecs_task_definition" "social_media_api_task_definition" {
  family                   = "social-media-api-task-definition"
  execution_role_arn       = "arn:aws:iam::xxxxx:role/ecsTaskExecutionRole" // replace with task execution role arn
  network_mode             = "awsvpc"
  requires_compatibilities = ["FARGATE"]
  cpu                      = "512"
  memory                   = "1024"
  
  runtime_platform {
    cpu_architecture    = "ARM64"
    operating_system_family = "LINUX"
  }

  container_definitions = jsonencode([
    {
      name         = "social-media-api-image-new"
      image        = "nimishmadan/social-media-api:latest"
      cpu          = 0
      essential    = true
      portMappings = [
        {
          name        = "social-media-api-image-new-8000-tcp"
          containerPort = 8000
          hostPort     = 8000
          protocol     = "tcp"
          appProtocol  = "http"
        }
      ]
      environment = [
        {
          name  = "SMTP_SERVER"
          value = "smtp.gmail.com"
        },
        {
          name  = "SMTP_USER"
          value = "xxxxxx@gmail.com"
        },
        {
          name  = "SMTP_PASSWORD"
          value = "xxxxxx"
        },
        {
          name  = "SECRET_KEY"
          value = "your_secret_key"
        },
        {
          name  = "SMTP_PORT"
          value = "587"
        },
        {
          name  = "SENDER_EMAIL"
          value = "xxxxx@gmail.com"
        }
      ]
      log_configuration = {
        log_driver = "awslogs"
        options = {
          "awslogs-group"         = "/ecs/social-media-api-task-definition"
          "awslogs-mode"          = "non-blocking"
          "awslogs-create-group"  = "true"
          "awslogs-max-buffer-size" = "25m"
          "awslogs-region"        = "us-east-1"
          "awslogs-stream-prefix" = "ecs"
        }
      }
    }
  ])
}

# Create ECS Service to run the Task Definition
resource "aws_ecs_service" "fastapi_service" {
  name            = "social-media-service"
  cluster         = aws_ecs_cluster.example.id
  task_definition = aws_ecs_task_definition.social_media_api_task_definition.arn
  desired_count   = 1  # Number of tasks you want to run
  launch_type     = "FARGATE"
  
  network_configuration {
    subnets          = ["subnet-xxxxxxx"]  // replace with subnet id
    security_groups = ["sg-xxxxxxx"]  // replace with security group id
    assign_public_ip = true  
  }
}


