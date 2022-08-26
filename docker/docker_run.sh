xhost +local:*
docker run \
  -v /home/$USER/projects/neural-grasp-fields/:/home/$USER \
  -v /tmp/.X11-unix:/tmp/.X11-unix \
  --gpus all \
  -e DISPLAY=$DISPLAY \
  -e QT_X11_NO_MITSHM=1 \
  -it thomasweng-ngf bash
  # -v /home/$USER/miniconda3/:/home/$USER/miniconda3/ \
  # -e PATH="/home/$USER/miniconda3/envs/gm1/bin:$PATH" \
