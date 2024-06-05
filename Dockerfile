# Use an official Python 3.9 slim image as the base
FROM python:3.9-slim

# Install PostgreSQL 14 dependencies (adjust for your package manager)
RUN apt update && apt upgrade -y
RUN apt install -y  postgresql # For Debian/Ubuntu

# Alternatively, for RHEL/CentOS-based systems
# RUN yum install -y postgresql-devel postgresql-server-postgresql14

RUN apt install -y build-essential python3-dev  # Installs gcc and other build tools

ENV PGDATA=/app/database

# Install your project dependencies
COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

# Copy your project codebase
COPY . .

# Default command to run your Python application
CMD ["python", "main.py"]
