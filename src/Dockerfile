FROM ubuntu:22.04

# install python3
RUN apt-get update && apt-get install -y python3 python3-pip \
	&& pip install pynacl

CMD ["/bin/bash"]
