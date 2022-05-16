apiVersion: v1
kind: Config

clusters:
- cluster:
    certificate-authority-data: ${CLUSTER_CA}
    server: ${CLUSTER_API}
  name: ${CLUSTER_NAME}

users:
- name: ${USER_NAME}
  user:
    client-certificate-data: ${USER_CRT}
    client-key-data: ${USER_KEY}

contexts:
- context:
    cluster: ${CLUSTER_NAME}
    user: ${USER_NAME}
