import React, { useState, useEffect } from "react";
import { Grid, Autocomplete } from "@mui/material";
import CustomComplexProjectCard from "../../Components/CustomComplexProjectCard";
import MDBox from "components/MDBox";
import MDTypography from "components/MDTypography";
import LogoKubernetes from "assets/images/logos/kubernetes_logo.png";
import { blue } from "@mui/material/colors";
import TextField from "@mui/material/TextField";
import axios from "axios";
import _ from "lodash";
import MDBadge from "components/MDBadge";
import MDButton from "components/MDButton";
import { Refresh } from "@mui/icons-material";
import Progress from "views/Components/Progress/Progress";

// const useStyles = makeStyles(styles);

function EdgeMonitoring(props) {
  // const classes = useStyles();

  const [namespaces, setNamespaces] = useState([]);
  const [selectNamespace, setSelectNamespace] = useState(
    sessionStorage.getItem("selectNamespace_edgeMonitoring")
      ? sessionStorage.getItem("selectNamespace_edgeMonitoring")
      : "all"
  );
  const [state, setState] = useState({});
  const [masterNode, setMasterNode] = useState([]);
  const [isLoading, setIsloading] = useState(false);

  useEffect(() => {
    setIsloading(true);

    let stateTmp = {};
    axios("/rest/1.0/k8s/namespace").then((res) => {
      let listNsTmp = [];
      listNsTmp.push("all");
      if (res.data.length > 0) {
        res.data.map((ns) => {
          listNsTmp.push(ns.name);
        });
      }
      setNamespaces(listNsTmp);
    });

    axios(`/rest/1.0/k8s/node`).then((res) => {
      let masterNodeTmp = [];
      let nodesTmp = [];
      if (res.data.length > 0) {
        res.data.map((node) => {
          if (node.node_role === "master") {
            masterNodeTmp.push(node.name);
          } else {
            nodesTmp.push({
              name: node.name,
              logo: "/public_assets/images/logos/" + node.node_type + "_logo.png",
            });
          }
        });
      }

      setMasterNode(masterNodeTmp);

      const selectNsTmp = selectNamespace === "all" ? "" : _.cloneDeep(selectNamespace);

      axios(`/rest/1.0/k8s/pod?namespace=${selectNsTmp}`).then((res) => {
        let podsTmp = [];
        if (res.data) {
          res.data.map((podsData, idx) => {
            podsTmp.push({
              id: `${podsData.pod_name}-${idx}`,
              content: podsData.pod_name,
              node_name: podsData.node_name,
            });
          });
          nodesTmp.map((node) => {
            stateTmp[node.name] = podsTmp.filter((pod) => {
              return pod.node_name === node.name;
            });
          });

          stateTmp["nodes"] = nodesTmp;
        }

        setState(stateTmp);
        setIsloading(false);
      });
    });
  }, []);

  useEffect(() => {
    setIsloading(true);
    sessionStorage.setItem("selectNamespace_edgeMonitoring", selectNamespace);

    let stateTmp = {};
    axios(`/rest/1.0/k8s/node`).then((res) => {
      let masterNodeTmp = [];
      let nodesTmp = [];
      if (res.data.length > 0) {
        res.data.map((node) => {
          if (node.node_role === "master") {
            masterNodeTmp.push(node.name);
          } else {
            nodesTmp.push({
              name: node.name,
              logo: "/public_assets/images/logos/" + node.node_type + "_logo.png",
            });
          }
        });
      }
      console.log("nodesTmp 확인");
      console.log(nodesTmp);
      setMasterNode(masterNodeTmp);

      const selectNsTmp = selectNamespace === "all" ? "" : _.cloneDeep(selectNamespace);

      axios(`/rest/1.0/k8s/pod?namespace=${selectNsTmp}`).then((res) => {
        let podsTmp = [];
        if (res.data) {
          res.data.map((podsData, idx) => {
            podsTmp.push({
              id: `${podsData.pod_name}-${idx}`,
              content: podsData.pod_name,
              node_name: podsData.node_name,
            });
          });
          nodesTmp.map((node) => {
            stateTmp[node.name] = podsTmp.filter((pod) => {
              return pod.node_name === node.name;
            });
          });
          stateTmp["nodes"] = nodesTmp;
        }
        setState(stateTmp);
        setIsloading(false);
      });
    });
  }, [selectNamespace]);

  useEffect(() => {
    console.log("state: ", state);
  }, [state]);

  useEffect(() => {
    console.log("selectNamespace: ", selectNamespace);
  }, [selectNamespace]);

  const handleOnReloadBtn = () => {
    setState({});
    setIsloading(true);

    let stateTmp = {};
    axios(`/rest/1.0/k8s/node`).then((res) => {
      let masterNodeTmp = [];
      let nodesTmp = [];

      if (res.data.length > 0) {
        res.data.map((node) => {
          if (node.node_role === "master") {
            masterNodeTmp.push(node.name);
          } else {
            nodesTmp.push({
              name: node.name,
              logo: "/public_assets/images/logos/" + node.node_type + "_logo.png",
            });
          }
        });
      }

      setMasterNode(masterNodeTmp);

      const selectNsTmp = selectNamespace === "all" ? "" : _.cloneDeep(selectNamespace);

      axios(`/rest/1.0/k8s/pod?namespace=${selectNsTmp}`).then((res) => {
        let podsTmp = [];
        if (res.data) {
          res.data.map((podsData, idx) => {
            podsTmp.push({
              id: `${podsData.pod_name}-${idx}`,
              content: podsData.pod_name,
              node_name: podsData.node_name,
            });
          });
          nodesTmp.map((node) => {
            stateTmp[node.name] = podsTmp.filter((pod) => {
              return pod.node_name === node.name;
            });
          });
          stateTmp["nodes"] = nodesTmp;
        }
        setState(stateTmp);
        setIsloading(false);
      });
    });
  };

  return (
    <>
      <MDBox mt={4}>
        <MDBox mt={3} display="flex" justifyContent="flex-end">
          <MDButton
            variant="gradient"
            color="info"
            size="large"
            sx={{ height: "44.125px" }}
            onClick={handleOnReloadBtn}
          >
            <Refresh sx={{ color: "#fff" }} />
          </MDButton>
        </MDBox>
      </MDBox>
      <MDBox mt={8} />
      <MDBox>
        <CustomComplexProjectCard title={"KUBERNETES"} image={LogoKubernetes}>
          <MDBox mt={5}>
            <Grid
              container
              display="flex"
              justifyContent="space-between"
              alignItems="center"
              spacing={5}
            >
              <Grid item>
                <MDBox mb={1}>
                  <MDTypography variant="h6" fontWeight="medium" textTransform="capitalize">
                    Master Node
                  </MDTypography>
                </MDBox>
                {masterNode.length > 0
                  ? masterNode.map((msNode, idx) => {
                      return (
                        <div
                          key={`${msNode}-${idx}`}
                          style={{
                            borderRadius: 5,
                            border: "1px solid lightgrey",
                            padding: 8,
                            width: "350px",
                          }}
                        >
                          <MDBox>
                            <MDBadge
                              size="xs"
                              color="success"
                              badgeContent={"Node Name"}
                              container
                              sx={{ height: "100%" }}
                            />
                            <MDBox mt={-0.5} ml={0.5} fontSize="20px" fontWeight="100">
                              {msNode}
                            </MDBox>
                          </MDBox>
                        </div>
                      );
                    })
                  : null}
              </Grid>
              <Grid item>
                <MDBox mb={1}>
                  <MDTypography variant="h6" fontWeight="medium" textTransform="capitalize">
                    Namespace
                  </MDTypography>
                </MDBox>
                <Autocomplete
                  size="medium"
                  disableClearable
                  disablePortal
                  value={selectNamespace}
                  options={namespaces}
                  onInputChange={(e) => {
                    if (e) {
                      const nameSpaceTmp = e.target.innerText;
                      setSelectNamespace(nameSpaceTmp);
                    }
                  }}
                  renderInput={(params) => <TextField {...params} sx={{ width: "350px" }} />} //label="Namespace"
                />
              </Grid>
            </Grid>
          </MDBox>

          <MDBox mt={5}>
            <MDBox mb={1}>
              <MDTypography variant="h6" fontWeight="medium" textTransform="capitalize">
                Worker Nodes
              </MDTypography>
            </MDBox>
            <Grid container spacing={5}>
              {state["nodes"]
                ? state["nodes"].map((node, idx) => {
                    return (
                      <Grid item key={`${node.name}-${idx}`}>
                        <div
                          style={{
                            borderRadius: 5,
                            border: "1px solid lightgrey",
                            padding: 8,
                            width: "350px",
                            height: "380px",
                          }}
                        >
                          <MDBox mb={1}>
                            <MDBox mt={-1}>
                              <MDBadge
                                size="xs"
                                color="success"
                                badgeContent={"Node Name"}
                                container
                              />
                              {node.logo === "/public_assets/images/logos/onpremise_logo.png" ? (
                                ""
                              ) : (
                                <img
                                  src={node.logo}
                                  alt=""
                                  width="60px"
                                  height="40px"
                                  align="right"
                                  style={{ marginTop: "5.6px" }}
                                />
                              )}
                            </MDBox>
                            <MDBox mt={-0.5} ml={0.5} fontSize="20px" fontWeight="100">
                              {node.name}
                            </MDBox>
                          </MDBox>

                          {/* <Divider /> */}
                          <MDBox mb={0.1}>
                            <MDBadge size="xs" color="info" badgeContent={"Pod List"} container />
                            <div style={{ overflowY: "auto", height: "255px" }}>
                              {state[node.name]
                                ? state[node.name].map((item, index) => (
                                    <div key={`${item.id}-${index}`}>
                                      <MDBox
                                        style={{
                                          borderRadius: 5,
                                          padding: 16,
                                          margin: `0 0 8px 0`,
                                          borderColor: blue[200],
                                          border: `1px solid ${blue[800]}`,
                                        }}
                                      >
                                        <MDBox
                                          fontSize="14px"
                                          fontWeight=""
                                          textTransform="lowercase"
                                          sx={{ color: blue[800] }}
                                        >
                                          {item.content}
                                        </MDBox>
                                      </MDBox>
                                    </div>
                                  ))
                                : null}
                            </div>
                          </MDBox>
                        </div>
                      </Grid>
                    );
                  })
                : null}
            </Grid>
          </MDBox>
        </CustomComplexProjectCard>
      </MDBox>
      <Progress isLoading={isLoading} />
    </>
  );
}

export default EdgeMonitoring;
