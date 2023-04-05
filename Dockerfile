FROM continuumio/miniconda3

RUN conda create -n env python=3.8
RUN echo "source activate env" > ~/.bashrc
ENV PATH /opt/conda/envs/env/bin:$PATH

# Set the working directory to /app
WORKDIR /app
COPY requirements.txt /app/requirements.txt

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt --verbose

# copy source code
COPY . /app

# test the app
RUN echo "སློབ་དཔོན་བྲམ་ཟེ་རྟ་དབྱངསཀྱིཡོམཛད།" > test-bo.txt
RUN echo "Hello World" > test-en.txt

RUN chmod +x align_tib_en.sh
# RUN /app/align_tib_en.sh test-bo.txt test-en.txt
# RUN cat test-bo.txt.org
