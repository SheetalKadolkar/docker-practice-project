# ---------- builder stage ----------
FROM python:3.11-slim AS builder
WORKDIR /app
# create a non-root user in builder to install wheel cache with proper permissions
RUN useradd -m appuser
COPY requirements.txt .
# Install build deps
RUN apt-get update && apt-get install -y build-essential && rm -rf /var/lib/apt/lists/*
RUN pip install --upgrade pip
RUN pip wheel --wheel-dir=/wheels -r requirements.txt

# ---------- final stage ----------
FROM python:3.11-slim
# create non-root user
RUN useradd -m appuser
WORKDIR /app

# copy wheels and install (faster repeated builds because of wheel cache)
COPY --from=builder /wheels /wheels
COPY requirements.txt .
RUN pip install --no-index --find-links=/wheels -r requirements.txt

# copy app code
COPY . /app

# run as non-root
USER appuser

ENV PORT=5000
EXPOSE 5000

# Healthcheck (HTTP)
HEALTHCHECK --interval=10s --timeout=3s --retries=3 \
  CMD curl -f http://localhost:5000/ || exit 1

# Use entrypoint to set executable; CMD is default args
ENTRYPOINT ["gunicorn", "--bind", "0.0.0.0:5000", "app:app", "--workers", "2"]
CMD []
