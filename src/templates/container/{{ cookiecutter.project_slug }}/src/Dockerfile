FROM ubuntu:22.04

#
# DOCKER BUILDKIT
#

ARG BUILDARCH
ARG BUILDOS
ARG BUILDPLATFORM
ARG TARGETARCH
ARG TARGETOS
ARG TARGETPLATFORM

#
# PROJECT
#

ARG PROJECT_BUILD_DATE
ARG PROJECT_COMMIT
ARG PROJECT_VERSION

#
# IMAGE
#

ARG DEFAULT_LANG="C.UTF-8"
ARG DEFAULT_USER_PRIMARY_GROUP="dev"
ARG DEFAULT_USER_SECONDARY_GROUPS="sudo,docker"
ARG DEFAULT_USER_SHELL="/bin/bash"
ARG DEFAULT_USER="dev"

#
# LABELS
#

#
# REFERENCE
#
#   - https://github.com/opencontainers/image-spec/blob/main/annotations.md
#

LABEL org.opencontainers.image.authors="{{ cookiecutter.author }} <{{ cookiecutter.email }}>"
LABEL org.opencontainers.image.created="${PROJECT_BUILD_DATE}"
LABEL org.opencontainers.image.description="{{ cookiecutter.description }}"
LABEL org.opencontainers.image.licenses="{{ cookiecutter.license }}"
LABEL org.opencontainers.image.revision="${PROJECT_COMMIT}"
LABEL org.opencontainers.image.source="{{ cookiecutter.source_code_url }}"
LABEL org.opencontainers.image.title="{{ cookiecutter.project_name }}"
LABEL org.opencontainers.image.url="{{ cookiecutter.registry_url }}"
LABEL org.opencontainers.image.vendor="{{ cookiecutter.author }}"
LABEL org.opencontainers.image.version="${PROJECT_VERSION}"

#
# OS
#

ENV VERSION_UBUNTU="22.04"
ENV VERSION_UBUNTU_NAME="jammy"

SHELL [ "/bin/bash", "-o", "pipefail", "-c" ]

RUN export DEBIAN_FRONTEND="noninteractive" \
    && apt-get update \
    && apt-get -y install --no-install-recommends \
        build-essential \
        ca-certificates \
        curl \
        locales \
        lsb-release \
        pkg-config \
        software-properties-common \
    && apt-get autoremove -y \
    && apt-get clean autoclean -y \
    && rm -r /var/cache/* /var/lib/apt/lists/*

RUN locale-gen "${DEFAULT_LANG}" \
    && update-locale LANG="${DEFAULT_LANG}"
