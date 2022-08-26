#!/bin/bash

set -euxo pipefail

apt-get update
DEBIAN_FRONTEND=noninteractive apt install --no-install-recommends \
  tzdata \
  curl \
  tmux \
  vim \
  libsm6 \
  libxext6 \
  libxrender-dev \
  libx11-dev \
  gedit \
  git \
  openssh-client \
  unzip \
  htop \
  libopenni-dev \
  apt-utils \
  usbutils \
  dialog \
  python3-virtualenv \
  python3-dev \
  python3-pip \
  ffmpeg \
  nvidia-settings \
  libffi-dev \
  build-essential \
  git \
  wget \
  pciutils \
  xserver-xorg \
  xserver-xorg-video-fbdev \
  xauth \
  protobuf-compiler \
  libxml2-dev \
  libxslt-dev \
  libglfw3-dev \
  libgl1-mesa-dev \
  libglu1-mesa-dev \
  libgles2-mesa-dev \
  freeglut3-dev \
  cmake \
