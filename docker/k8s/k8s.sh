### CLUSTERS
# Launch a minikube cluster with 1 node
minikube start

# Lister les nodes
kubectl get node

# Suppression du cluster
minikube delete


### PODS
# Lancer un pod
kubectl apply -f [NOM_SPEC].yaml

# Lister les pods
kubectl get pods

# Détails du pod
kubectl describe pod [NOM_POD]

# Suppression de pods
kubectl delete po/[NOM_POD]