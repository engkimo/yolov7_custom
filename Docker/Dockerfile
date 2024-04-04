ARG CUDA=11.4.3
ARG CUDNN=8
ARG UBUNTU=20.04
FROM nvidia/cuda:${CUDA}-cudnn${CUDNN}-devel-ubuntu${UBUNTU}

ENV TZ=Asia/Tokyo
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
WORKDIR /home/app
RUN apt-get update && apt-get upgrade -y

RUN apt install -y \
    sudo tzdata vim git cmake wget unzip 
RUN apt-get update && apt install -y build-essential libssl-dev libffi-dev python3-dev libgl1 
RUN apt install -y python3-pip
# for opencv
RUN apt-get install -y libglib2.0-0

RUN pip3 install --upgrade pip
RUN pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
COPY requirements.txt /tmp/requirements.txt
RUN pip3 install -r /tmp/requirements.txt
RUN rm /tmp/requirements.txt

CMD [ "/bin/bash" ]
