FROM reg.docker.alibaba-inc.com/ecs-mysql-client:1.0

ADD install /tmp/install
ADD upgrade /tmp/upgrade
ADD rollback /tmp/rollback
ADD lib /tmp/lib
ADD run.py /tmp/run.py
ADD replace_set.sh /tmp/replace_set.sh
ADD meta /
RUN  chmod +x /tmp/run.py && chmod +x /tmp/replace_set.sh
ENTRYPOINT /tmp/run.py