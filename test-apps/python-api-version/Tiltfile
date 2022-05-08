docker_build(
    'k3d-registry.localhost:5000/pav',
    context='.',
)

allow_k8s_contexts(k8s_context())

# Load extensions from: https://github.com/tilt-dev/tilt-extensions 
load('ext://namespace', 'namespace_create')
namespace_create('pav')


#k8s_yaml(helm('./chart'))
chart = helm(
  './chart',
  # The release name, equivalent to helm --name
  name='pav',
  # The namespace to install in, equivalent to helm --namespace
  namespace='pav',
  # Values to set from the command-line
  set=['image.repository=k3d-registry.localhost:5000/pav']
  )
k8s_yaml(chart)

k8s_resource("pav", port_forwards="5001:5000")

local_resource(
    "tests",
    cmd="echo I was too lazy to write tests for this demo",
)