# Download base image
FROM nvidia/cuda:11.1.1-cudnn8-devel-ubuntu18.04
MAINTAINER Thomas Weng

#########
# Credit: https://github.com/askforalfred/alfred/blob/master/Dockerfile
#########

# Env vars for the nvidia-container-runtime.
ENV NVIDIA_VISIBLE_DEVICES all
ENV NVIDIA_DRIVER_CAPABILITIES graphics,utility,compute

# https://github.com/NVIDIA/nvidia-docker/issues/1632
RUN rm /etc/apt/sources.list.d/cuda.list

ARG USER_NAME
ARG USER_PASSWORD
ARG USER_ID
ARG USER_GID

RUN apt-get update
RUN apt install sudo
RUN useradd -ms /bin/bash $USER_NAME
RUN usermod -aG sudo $USER_NAME
RUN yes $USER_PASSWORD | passwd $USER_NAME

# set uid and gid to match those outside the container
RUN usermod -u $USER_ID $USER_NAME
RUN groupmod -g $USER_GID $USER_NAME

# work directory
WORKDIR /home/$USER_NAME/

# Dependency for EGL
# RUN apt update
# ENV DEBIAN_FRONTEND=noninteractive
# RUN apt-get -y install tzdata
# RUN apt install -y cmake build-essential libgl1-mesa-dev freeglut3-dev libglfw3-dev libgles2-mesa-dev
# RUN apt install -y libx11-dev 

# install system dependencies
COPY ./docker/install_deps.sh /tmp/install_deps.sh
RUN chmod +x /tmp/install_deps.sh
RUN yes "Y" | /tmp/install_deps.sh

# install 

# setup python environment
RUN cd $WORKDIR

# install GLX-Gears (for debugging)
RUN apt-get update && apt-get install -y \
   mesa-utils && \
   rm -rf /var/lib/apt/lists/*

# change ownership of everything to our user
RUN cd ${USER_HOME_DIR} && echo $(pwd) && chown $USER_NAME:$USER_NAME -R .

# entry point
ENTRYPOINT bash -c "/bin/bash"
# RUN mkdir /workspace/ && cd /workspace/
# WORKDIR /workspace