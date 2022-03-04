master:
  resources:
    limits:
      cpu: "8"
      memory: "16Gi"
    requests:
      cpu: "4"
      memory: "4Gi"
  installPlugins:
  - docker-build-step:2.6
  - ace-editor:1.1
  - bootstrap4-api:4.6.0-2
  - git:4.7.0
  - junit:1.49
  - pipeline-milestone-step:1.3.2
  - docker-java-api:3.1.5.2
  - golang:1.4
  - pipeline-rest-api:2.19
  - git-client:3.7.0
  - google-oauth-plugin:1.0.4
  - echarts-api:5.0.1-1
  - lockable-resources:2.10
  - docker-workflow:1.26
  - checks-api:1.6.1
  - variant:1.4
  - workflow-cps:2.90
  - workflow-multibranch:2.23
  - throttle-concurrents:2.0.3
  - command-launcher:1.5
  - workflow-durable-task-step:2.38
  - credentials-binding:1.24
  - jquery-detached:1.2.1
  - jquery:1.12.4-1
  - jobConfigHistory:2.26
  - pipeline-model-definition:1.8.4
  - git-parameter:0.9.13
  - workflow-basic-steps:2.23
  - pipeline-utility-steps:2.7.0
  - http_request:1.8.27
  - structs:1.22
  - pipeline-model-extensions:1.8.4
  - docker-commons:1.17
  - pipeline-config-history:1.6
  - oauth-credentials:0.4
  - token-macro:2.15
  - ant:1.11
  - snakeyaml-api:1.27.0
  - pipeline-stage-step:2.5
  - ssh-slaves:1.31.5
  - google-login:1.6
  - jackson2-api:2.12.1
  - workflow-aggregator:2.6
  - monitoring:1.86.0
  - workflow-support:3.8
  - kubernetes-client-api:4.13.2-1
  - pipeline-model-api:1.8.4
  - role-strategy:3.1.1
  - docker-plugin:1.2.2
  - scm-api:2.6.4
  - saferestart:0.3
  - matrix-auth:2.6.7
  - script-security:1.76
  - git-server:1.9
  - pipeline-build-step:2.13
  - build-with-parameters:1.5.1
  - external-monitor-job:1.7
  - popper-api:1.16.1-2
  - credentials:2.4.1
  - mailer:1.34
  - kubernetes-credentials:0.8.0
  - display-url-api:2.3.4
  - font-awesome-api:5.15.2-2
  - antisamy-markup-formatter:2.1
  - jdk-tool:1.5
  - workflow-job:2.40
  - handlebars:3.0.8
  - pipeline-input-step:2.12
  - javadoc:1.6
  - ssh-credentials:1.18.1
  - jquery3-api:3.5.1-3
  - pipeline-stage-tags-metadata:1.8.4
  - pipeline-graph-analysis:1.10
  - jsch:0.1.55.2
  - Office-365-Connector:4.14.0
  - pipeline-multibranch-defaults:2.1
  - ldap:1.26
  - handy-uri-templates-2-api:2.1.8-1.0
  - pipeline-stage-view:2.19
  - cloudbees-bitbucket-branch-source:2.9.7
  - authentication-tokens:1.4
  - durable-task:1.35
  - apache-httpcomponents-client-4-api:4.5.13-1.0
  - momentjs:1.1.1
  - workflow-step-api:2.24
  - trilead-api:1.0.13
  - kubernetes:1.29.2
  - google-kubernetes-engine:0.8.6
  - pam-auth:1.6
  - workflow-cps-global-lib:2.18
  - windows-slaves:1.7
  - matrix-project:1.19
  - config-file-provider:3.8.0
  - workflow-api:2.42
  - cloudbees-folder:6.15
  - branch-api:2.6.3
  - hashicorp-vault-plugin:3.8.0
  - extended-choice-parameter:0.82
  - htmlpublisher:1.27
  cpu: "1"
  memory: "3500Mi"
  javaOpts: >-
   -Xms3500m -Xmx3500m -Dhudson.model.DirectoryBrowserSupport.CSP="sandbox allow-scripts; default-src 'self'; script-src 'self' 'unsafe-eval'; style-src 'unsafe-inline' 'unsafe-eval'; script-src-elem 'self' 'unsafe-inline'; img-src 'self' data:;"
  serviceType: ClusterIP
  securityRealm: |-
    <securityRealm class="org.jenkinsci.plugins.googlelogin.GoogleOAuth2SecurityRealm" plugin="google-login@1.6">
      <clientId>{JENKINS_CLIENT_ID}</clientId>
      <clientSecret>{JENKINS_CLIENT_SECRET}</clientSecret>
      <domain>gcp.lowes.com, lowes.com</domain>
      <rootURLFromRequest>true</rootURLFromRequest>
    </securityRealm>
  authorizationStrategy: |-
    <authorizationStrategy class="hudson.security.GlobalMatrixAuthorizationStrategy">
      <permission>com.cloudbees.plugins.credentials.CredentialsProvider.Create:authenticated</permission>
      <permission>com.cloudbees.plugins.credentials.CredentialsProvider.Delete:authenticated</permission>
      <permission>com.cloudbees.plugins.credentials.CredentialsProvider.ManageDomains:authenticated</permission>
      <permission>com.cloudbees.plugins.credentials.CredentialsProvider.Update:authenticated</permission>
      <permission>com.cloudbees.plugins.credentials.CredentialsProvider.View:authenticated</permission>
      <permission>hudson.model.Computer.Build:authenticated</permission>
      <permission>hudson.model.Computer.Configure:authenticated</permission>
      <permission>hudson.model.Computer.Connect:authenticated</permission>
      <permission>hudson.model.Computer.Create:authenticated</permission>
      <permission>hudson.model.Computer.Delete:authenticated</permission>
      <permission>hudson.model.Computer.Disconnect:authenticated</permission>
      <permission>hudson.model.Hudson.Administer:chris.dyer@gcp.lowes.com</permission>
      <permission>hudson.model.Hudson.Administer:james.keller@gcp.lowes.com</permission>
      <permission>hudson.model.Hudson.Administer:tamoghna.sen@gcp.lowes.com</permission>
      <permission>hudson.model.Hudson.Administer:gaurav.v@gcp.lowes.com</permission>
      <permission>hudson.model.Hudson.Administer:rajshekar.reddy@gcp.lowes.com</permission>
      <permission>hudson.model.Hudson.Administer:nithin.lakshmanan@gcp.lowes.com</permission>
      <permission>hudson.model.Hudson.Read:authenticated</permission>
      <permission>hudson.model.Item.Build:authenticated</permission>
      <permission>hudson.model.Item.Cancel:authenticated</permission>
      <permission>hudson.model.Item.Configure:authenticated</permission>
      <permission>hudson.model.Item.Create:authenticated</permission>
      <permission>hudson.model.Item.Delete:authenticated</permission>
      <permission>hudson.model.Item.Discover:authenticated</permission>
      <permission>hudson.model.Item.Move:authenticated</permission>
      <permission>hudson.model.Item.Read:authenticated</permission>
      <permission>hudson.model.Item.Workspace:authenticated</permission>
      <permission>hudson.model.Run.Delete:authenticated</permission>
      <permission>hudson.model.Run.Replay:authenticated</permission>
      <permission>hudson.model.Run.Update:authenticated</permission>
      <permission>hudson.model.View.Configure:authenticated</permission>
      <permission>hudson.model.View.Create:authenticated</permission>
      <permission>hudson.model.View.Delete:authenticated</permission>
      <permission>hudson.model.View.Read:authenticated</permission>
      <permission>hudson.scm.SCM.Tag:authenticated</permission>
      <permission>org.jenkins.plugins.lockableresources.LockableResourcesManager.Reserve:authenticated</permission>
      <permission>org.jenkins.plugins.lockableresources.LockableResourcesManager.Unlock:authenticated</permission>
    </authorizationStrategy>
agent:
  enabled: true
  customJenkinsLabels:
  - docker
  image: gcr.io/gcp-ushi-carbon-devops-npe/irs-image-slave
  tag: 3.10-1-B5
  imagePullSecretName: gcr
  envVars:
  - name: "DOCKER_HOST"
    value: "tcp://localhost:2375"
  - name: "JENKINS_URL"
    value: "http://jenkins.jenkins.svc.cluster.local:8080"
  resources:
    requests:
      cpu: "2"
      memory: "512Mi"
    limits:
      cpu: "4"
      memory: "2048Mi"
  yamlTemplate: |-
    apiVersion: "v1"
    kind: "Pod"
    spec:
      containers:
      - name: jnlp
        volumeMounts:
        - mountPath: /var/lib/docker/
          name: dind-storage
      - name: "dind"
        image: "docker:18.05-dind"
        imagePullPolicy: "Always"
        securityContext:
          privileged: true
        tty: true
        volumeMounts:
        - mountPath: "/var/lib/docker"
          name: "dind-storage"
      volumes:
      - emptyDir: {}
        name: "dind-storage"
persistence:
  storageClass: "standard"
  size: 200Gi
networkPolicy:
  apiVersion: networking.k8s.io/v1
rbac:
  serviceAccount:
      name: cd-jenkins
