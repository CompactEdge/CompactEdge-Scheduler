import DashboardIcon from "@mui/icons-material/Dashboard";
import BigCrawlerManagement from "views/Management/BigCrawlerManagement/BigCrawlerManagement";
import CreateDeployment from "views/Management/CreateDeployment/CreateDeployment";
import CreateNode from "views/Management/CreateNode/CreateNode";
import CreatePod from "views/Management/CreatePod/CreatePod";
import CreateService from "views/Management/CreateService/CreateService";
import ClusterMonitoring from "views/Monitoring/ClusterMonitoring/ClusterMonitoring";
import ControllerMonitoring from "views/Monitoring/ControllerMonitoring/ControllerMonitoring";
import EdgeMonitoring from "views/Monitoring/EdgeMonitoring/EdgeMonitoring";
import NodeMonitoring from "views/Monitoring/NodeMonitoring/NodeMonitoring";
import PodMonitoring from "views/Monitoring/PodMonitoring/PodMonitoring";
import RabbitmqMonitoring from "views/Monitoring/RabbitmqMonitoring/RabbitmqMonitoring";
import ServiceMonitoring from "views/Monitoring/ServiceMonitoring/ServiceMonitoring";
import StorageMonitoring from "views/Monitoring/StorageMonitoring/StorageMonitoring";

const routesEdge = [
  {
    type: "collapse",
    name: "Monitoring",
    key: "monitoring",
    icon: <DashboardIcon />,
    collapse: [
      {
        name: "EdgeMonitoring",
        key: "edgeMonitoring",
        route: "/views/monitoring/edgeMonitoring",
        component: <EdgeMonitoring />,
        layout: "/admin",
      },
      {
        name: "ClusterMonitoring",
        key: "clusterMonitoring",
        route: "/views/monitoring/clusterMonitoring",
        component: <ClusterMonitoring />,
        layout: "/admin",
      },
      {
        name: "NodeMonitoring",
        key: "nodeMonitoring",
        layout: "/admin",
        route: "/views/monitoring/nodeMonitoring",
        component: <NodeMonitoring />,
      },
      {
        type: "collapse",
        name: "PodMonitoring",
        key: "podMonitoring",
        route: "/views/monitoring/podMonitoring",
        component: <PodMonitoring />,
        noCollapse: true,
        layout: "/admin",
      },
      {
        type: "collapse",
        name: "ControllerMonitoring",
        key: "controllerMonitoring",
        route: "/views/monitoring/controllerMonitoring",
        component: <ControllerMonitoring />,
        noCollapse: true,
        layout: "/admin",
      },
      {
        type: "collapse",
        name: "StorageMonitoring",
        key: "storageMonitoring",
        route: "/views/monitoring/storageMonitoring",
        component: <StorageMonitoring />,
        noCollapse: true,
        layout: "/admin",
      },
      {
        type: "collapse",
        name: "ServiceMonitoring",
        key: "serviceMonitoring",
        route: "/views/monitoring/serviceMonitoring",
        component: <ServiceMonitoring />,
        noCollapse: true,
        layout: "/admin",
      },
      {
        type: "collapse",
        name: "EdgeMQMonitoring",
        key: "EdgeMQMonitoring",
        route: "/views/monitoring/edgeMQMonitoring",
        component: <RabbitmqMonitoring />,
        noCollapse: true,
        layout: "/admin",
      },
    ],
  },
  {
    type: "collapse",
    name: "Management",
    key: "management",
    icon: <DashboardIcon />,
    collapse: [
      {
        type: "collapse",
        name: "CreatePod",
        key: "createPod",
        route: "/views/management/createPod",
        component: <CreatePod />,
        noCollapse: true,
        layout: "/admin",
      },
      {
        type: "collapse",
        name: "CreateDeployment",
        key: "createDeployment",
        route: "/views/management/createDeployment",
        component: <CreateDeployment />,
        noCollapse: true,
        layout: "/admin",
      },
      {
        type: "collapse",
        name: "CreateService",
        key: "createService",
        route: "/views/management/createService",
        component: <CreateService />,
        noCollapse: true,
        layout: "/admin",
      },
      {
        type: "collapse",
        name: "CreateNode",
        key: "createNode",
        route: "/views/management/createNode",
        component: <CreateNode />,
        noCollapse: true,
        layout: "/admin",
      },
      {
        type: "collapse",
        name: "BigCrawler",
        key: "bigCrawler",
        route: "/views/management/bigCrawler",
        component: <BigCrawlerManagement />,
        noCollapse: true,
        layout: "/admin",
      },
    ],
  },
];

export default routesEdge;
