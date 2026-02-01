# n8n-nodes-kubernetes

This is a n8n community node. It lets you use Kubernetes in your n8n workflows.


[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

[Installation](#installation)  
[Operations](#operations)  
[Credentials](#credentials)  <!-- delete if no auth needed -->  
[Compatibility](#compatibility)  
[Usage](#usage)  <!-- delete if not using this section -->  
[Resources](#resources)  
[Version history](#version-history)  <!-- delete if not using this section -->  

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

Quick Installation

  1.  Go to Settings > Community Nodes
  2. Select Install
  3. Enter n8n-nodes-kubernetes in Enter npm package name
  4. Agree to the risks of using community nodes
  5. Select Install


## Operations

### Events

Get a list of events that have taken place on your Kubernetes Node. You can also request events from a specific Namespace

## Credentials

This N8N Node has been setup to use a [Service Account](https://kubernetes.io/docs/concepts/security/service-accounts/). Once the service account has been created you'll need to generate a Token. 


#### Create Namespace and Service Account

```
kubectl create namespace external-access
kubectl create serviceaccount event-reader -n external-access
```

#### Set Cluster Wide Role

Read More about [Role and ClusterRole](https://kubernetes.io/docs/reference/access-authn-authz/rbac/#role-and-clusterrole)

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: event-reader-clusterrole
rules:
- apiGroups: [""]
  resources: ["events"]
  verbs: ["get", "list", "watch"] # 'watch' if you want to stream events
```


#### Apply Role and bind to service account

```bash
kubectl apply -f event-reader-clusterrole.yaml 
kubectl create clusterrolebinding event-reader-binding \ --clusterrole=event-reader-clusterrole \ --serviceaccount=external-access:event-reader
```

#### Create Token

```yaml
apiVersion: v1 
kind: Secret
metadata:
  name: my-long-lived-secret
- namespace: external-access
  annotations:
    kubernetes.io/service-account-name: event-reader
type: kubernetes.io/service-account-toke
```

#### Test Your Access

```
TOKEN=$(kubectl get secret my-long-lived-secret -n external-access -o jsonpath='{.data.token}' | base64 -d)
```


```
curl -H "Authorization: Bearer $TOKEN" https://IP:PORT/api/v1/events --insecure
```


## Compatibility

This node has been tested on version 1.77.3.

## Usage


## Resources

* [n8n community nodes documentation](https://docs.n8n.io/integrations/community-nodes/)
* [kubernetes documentation](https://docs.tavily.com/welcome) 
* [kubernetes search](https://docs.tavily.com/api-reference/endpoint/search)
* [kubernetes extract](https://docs.tavily.com/api-reference/endpoint/extract)

## Version history

v0.1.5 - Updated README.md
v0.1.4 - Updated README.md and fixed issue with Extract operation and multiple URLs

