# Serie A Stats

This app will display results, statistics and league tables for Serie A. I’m building it to learn how to use DevOps tools in practice, whilst also combining them with my personal interests.

## Goal

The primary goal is **learning DevOps**, not building a polished frontend/backend.
The application is intentionally minimal — the value is in the tooling around it.

## Tech stack

- **Backend:** Python + FastAPI (single `/stats` endpoint fetching data from a football API)
- **Frontend:** static HTML served by the backend
- **Containerization:** Docker, docker-compose
- **Orchestration:** Kubernetes (kind/minikube locally, EKS on AWS)
- **Cloud:** AWS (EKS, ECR, IAM, VPC)
- **CI/CD:** GitHub Actions
- **Observability:** Prometheus + Grafana
- **IaC:** Terraform (later stage)

## Roadmap

- [ ] Minimal backend with `/stats` endpoint (data from football API)
- [ ] `Dockerfile` + run locally with `docker build` / `docker run`
- [ ] `docker-compose.yml` with a cache service (Redis)
- [ ] Kubernetes manifests (`Deployment`, `Service`, `ConfigMap`, `Secret`, `Ingress`)
- [ ] Run locally on kind/minikube
- [ ] Provision EKS + ECR with Terraform
- [ ] CI/CD pipeline: build → test → push to ECR → deploy to EKS
- [ ] Monitoring with Prometheus + Grafana

## Local development

_TBD — will be filled in as the project grows._
