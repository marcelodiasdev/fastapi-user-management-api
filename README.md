# FastAPI User Management API

<div align="center">

![FastAPI](https://img.shields.io/badge/FastAPI-0.110%2B-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.11%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-Async-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white)
![Ruff](https://img.shields.io/badge/Ruff-261230?style=for-the-badge&logo=ruff&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)

A high-performance, asynchronous user management and authentication API built with modern Python standards, featuring robust database migrations, containerized workflows, and a comprehensive automated test suite.

</div>

---

## 🚀 About the Project

This project is a production-ready RESTful API designed for scalable user management operations. It follows clean architecture principles, leveraging **FastAPI** for blazing-fast asynchronous request handling and **SQLAlchemy (Async)** paired with **Alembic** for reliable database management. 

Designed with developer experience (DX) and code quality in mind, it incorporates strict linting rules via **Ruff**, task automation with **Taskipy**, and container orchestration using **Docker Compose**.

---

## 🛠️ Tech Stack & Architecture

* **Framework:** [FastAPI](https://fastapi.tiangolo.com/) (Async web framework)
* **Server:** [Uvicorn](https://www.uvicorn.org/) (ASGI server)
* **Database & ORM:** [PostgreSQL](https://www.postgresql.org/) / [SQLite](https://www.sqlite.org/) via **SQLAlchemy** (AsyncIO)
* **Migrations:** [Alembic](https://alembic.sqlalchemy.org/)
* **Validation & Settings:** [Pydantic v2](https://pydantic-docs.helpmanual.io/)
* **Code Quality & Linter:** [Ruff](https://github.com/astral-sh/ruff)
* **Task Runner:** [Taskipy](https://github.com/illBeRoy/taskipy)
* **Testing:** [Pytest](https://docs.pytest.org/) (Async test suite)
* **Containerization:** [Docker](https://www.docker.com/) & Docker Compose

---

## 📂 Project Structure

```text
car_api/
├── alembic/              # Database migration scripts
├── car_api/              # Main application package
│   ├── api/              # API routers and endpoints
│   ├── core/             # Security, config, and database sessions
│   ├── models/           # SQLAlchemy models
│   ├── schemas/          # Pydantic data validation schemas
│   └── main.py           # Application entrypoint
├── tests/                # Automated tests (Pytest)
├── Dockerfile            # Container image configuration
├── docker-compose.yml    # Multi-container orchestration
├── pyproject.toml        # Project metadata, dependencies, and task shortcuts
└── README.md