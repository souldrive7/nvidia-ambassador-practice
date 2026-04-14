#!/usr/bin/env bash
docker run --rm --gpus all -it \
  -e NVIDIA_API_KEY="$NVIDIA_API_KEY" \
  -v $PWD:/workspace \
  -w /workspace \
  nvcr.io/nvidia/pytorch:26.03-py3 bash
