# ETRI k8s with a new scheduler

k8s 기반 엣지 플랫폼의 관리 기능과 RTCore를 기반으로 한 서비스의 실시간 스케줄링 설정 기능을 제공합니다. 


## Contents
- 엣지 플래폼 관리 기능 
- RT Core 관리 기능 
- 멀티 클라우드 연계 기능
- 멀티 클러스터 관리 기능 

# Features
## 엣지 플랫폼 관리 기능  

엣지 플랫폼 관리 기능은 엣지 플랫폼을 구성하는 모든 구성요소들에 대한 모니터링 기능과 엣지 플랫폼의 Pod, Deployment, Service의 배포 기능을 제공합니다. 

### Monotoring
* __EdgeMonitoring :__ 엣지 플랫폼의 전체 노드 구성 및 노드에 배표된 Pod들의 정보 모니터링
* __ClusterMonitoring :__ 클러스터 전체 대한 CPU, Memory, Disk, Network 상태 정보 모니터링 
* __NodeMonitoring :__ 하나의 노드에 대한 CPU, Memory, Disk, Network 상태 정보 모니터링 
* __PodMonitoring :__ 하나의 Namespacef를 구성하는 Pod들의 CPU, Memory, Network 상태 정보 모니터링 
* __ControllerMonitoring :__ Deployment, DaemonSet, ReplicaSet, StatefulSet, Job에 대한 모니터링 
* __StorageMonitoring :__ PersistentVolume, PersistentVolumeClaim, StorageClass에 대한 모니터링 
* __ServiceMonitoring :__ ClusterIP, LoadBalancer, NodePort에 대한 모니터링 
* __EdgeMQMonitoring :__ EdgeMQ 상태 모니터링 

### Management
* __CreatePod :__ 특정 노드에 Pod를 배포하는 기능 제공
* __CreateDeployment :__ Repository의 이미지를 Deployment로 배포하는 기능 제공
* __CreateService :__ 특정 Deployment르 Service로 배포하는 기능 제공 
* __CreateNode :__ 신규 Node를 배포하는 기능 제공

![스크린샷 2024-04-04 오후 12 55 23](https://github.com/CompactEdge/CompactEdge-Scheduler/assets/86282316/beb692ca-7726-47ce-9d35-427c0be29f39)


## RT Core 관리 기능   

엣지 플랫폼이 RealTime 서비스를 제공하기 위해 각각의 노드에 있는 RTCore의 정보를 관리하고, RTCore를 사용하는 Pod의 상태를 조회하는 기능을 제공합니다. 
* __RT Core 상태 관리:__ 클러스터에 배포된 Pod/Deployment/Service 들 중 RTCore를 사용하는 Pod/Deployment/Service에 대한 정보 표시 
* __RT Core 설정 기능:__ 클러스터를 구성하는 노드들의 Core 정보를 표시하고, 이중 RT Core의 정보 및 사용 여부 표시 
* __RT 서비스 설정 기능:__ 서비스 관리 화면을 통해 Pod/Deployment/Service가 RT Core를 사용하도록 설정하거나, 해지하는 기능 

![스크린샷 2024-04-04 오후 1 08 46](https://github.com/CompactEdge/CompactEdge-Scheduler/assets/86282316/76e79235-07de-401b-8d61-2d7074b7d82e)

# Contributors
- YeonJoong Kim (yeonjoong.kim@wizontech.com)
- Joojin Son (joosin.son@wizontech.com)

