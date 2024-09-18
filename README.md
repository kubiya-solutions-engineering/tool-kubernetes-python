# Kubernetes Command Line Interface (`kubectl`) tool

This tool definition wraps a Docker Hub container containing the Kubernetes CLI into a tool. Can be
used by Kubiya Teammates to access Kubernetes using CLI commands.

# Installation

## Pre-requisites

Nil except having a Kubernetes cluster to host your Kubiya Teammates and Tool Manager.

Note that you may need to create a ClusterRoleBinding to connect to the underlying Kubernetes
cluster. The following is an example of what that could look like, note that it does provide
elevated rights.

```bash
kubectl create clusterrolebinding kubiya-service-account-access \
  --clusterrole=cluster-admin \
  --serviceaccount=kubiya:kubiya-service-account
```

## Uploading the tool as a new Source

1. Navigate to the Kubiya Web App, [app.kubiya.ai](https://app.kubiya.ai). Login if needed.
2. Select *Resources*, *Sources*, and then *+ New Source*.
3. Copy and paste this respository's URL into the text box *Source URL* and select *Load tools &
workflows*.
4. Under *Tools & workflows discovered* you should see a list of tools associated with this
repository.
5. Optionally, name your tool.
6. Select *+ Create*.

The tool is now available for use by a Teammate.

# Usage

Depending on the roles and access assigned to the associated user, this tool can execute any command
using the Kubernetes CLI, as indicated below:

    kubectl {{.command}}

This gives the tool significant ability to affect change on your Kubernetes account. Therefore it
is highly recommended to ensure that appropriate roles are assigned.

In addition, this tool can be modified to only execute one type of command. For example:

    kubectl get {{.command}}

# Contact

Please contact the author of this tool using the email address:
[support@kubiya.ai](mailto:support@kubiya.ai).

