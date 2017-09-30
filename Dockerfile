FROM elasticsearch
# We use '-b' ('--batch') option for automatic confirmation.
RUN /usr/share/elasticsearch/bin/elasticsearch-plugin install -b discovery-ec2
