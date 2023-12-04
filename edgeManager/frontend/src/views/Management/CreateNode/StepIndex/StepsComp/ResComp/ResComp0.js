import React from 'react';
import Box from '@mui/material/Box';
import Collapse from '@mui/material/Collapse';
import MDBox from 'components/MDBox';
import MDTypography from 'components/MDTypography';
import MDButton from 'components/MDButton';
import { Divider, Icon, Tooltip } from '@mui/material';
import MDBadge from 'components/MDBadge';
import { blue } from '@mui/material/colors';
import ReqBox from './component/ReqBox';

function ResComp0({
  resOpen,
  setResOpen,
  resData,
  setFailureCondition,
}) {
  const [dataNode, setDataNode] = React.useState({});
  const [dataWorker, setDataWorker] = React.useState({});
  const [installedWorker, setInstalledWorker] = React.useState({
    state: false,
    hostName: [],
  });
  const [dataApps, setDataApps] = React.useState([]);

  React.useEffect(() => {
    if (resData) {
      setDataNode(resData.validate_node);
      setDataWorker(resData.validate_worker_node);
      setDataApps(resData.validate_installed_apps.service_result);
      if (resData.validate_worker_node.service_code === 200 && resData.validate_worker_node.service_validate) {
        setInstalledWorker({ ...installedWorker, state: false });
      } else {
        setInstalledWorker({ ...installedWorker, state: true, hostName: resData.validate_worker_node.service_result });
      };
    } else {
      setDataNode({});
      setDataWorker({});
      setInstalledWorker({
        state: false,
        hostName: [],
      });
      setDataApps([]);
    }
  }, [resData]);

  // React.useEffect(() => {
  //   console.log("dataNode: ", resData);
  //   console.log("dataWorker: ", dataWorker);
  //   console.log("installedWorker: ", installedWorker);
  //   console.log("dataApps: ", dataApps);
  // }, [dataApps]);

  return (
    <MDBox>
      <Box sx={{ width: '100%' }}>
        <MDBox borderTop={"1px solid #e0e0e0"} />
        <MDBox my={2} display="flex" justifyContent="space-between" alignItems="center" >
          <MDTypography variant="h6" color="info">
            Response
          </MDTypography>
          {resData &&
            <Tooltip title={resOpen ? "Close Response Box" : "Open Response Box"} placement="bottom" arrow>
              <MDButton variant="outlined" color="secondary" size="small" circular iconOnly onClick={() => {
                resOpen ? setResOpen({ ...resOpen, step0: false }) : setResOpen({ ...resOpen, step0: true })
              }}>
                {resOpen ? <Icon>expand_less</Icon> : <Icon>expand_more</Icon>}
              </MDButton>
            </Tooltip>
          }
        </MDBox>
        <Collapse in={resOpen}>
          <MDBox>
            <MDBox
              style={{
                borderRadius: 5,
                padding: 16,
                margin: "0 0 8px 0",
                border: "1px solid",
                borderColor: blue[800],
              }}
            >
              <MDBox
                display="flex"
                justifyContent="space-between"
                alignItems="center"
                width={{ xs: "max-content", sm: "100%" }}
              >
                <MDBox
                  fontSize="14px"
                  fontWeight="bold"
                  textTransform="capitalize"
                  style={{
                    color: blue[800],
                  }}
                >
                  노드 접속 여부
                </MDBox>
                <MDBox>
                  {
                    Object.keys(dataNode).length > 0
                      ?
                      <ReqBox
                        name={"node"}
                        data={dataNode}
                        setFailureCondition={setFailureCondition}
                      />
                      :
                      <MDBadge
                        variant="contained"
                        size="xs"
                        badgeContent={"loading..."}
                        color={"warning"}
                        container
                      />
                  }
                </MDBox>
              </MDBox>
            </MDBox>
            <MDBox
              style={{
                borderRadius: 5,
                padding: 16,
                margin: "0 0 8px 0",
                border: "1px solid",
                borderColor: blue[800],
              }}
            >
              <MDBox
                display="flex"
                justifyContent="space-between"
                alignItems="center"
                width={{ xs: "max-content", sm: "100%" }}
              >
                <MDBox
                  fontSize="14px"
                  fontWeight="bold"
                  textTransform="capitalize"
                  style={{
                    color: blue[800],
                  }}
                >
                  워커 노드 설치 여부
                </MDBox>
                {
                  Object.keys(dataWorker).length > 0
                    ?
                    <ReqBox
                      name={"worker"}
                      data={dataWorker}
                      setFailureCondition={setFailureCondition}
                    />
                    :
                    <MDBadge
                      variant="contained"
                      size="xs"
                      badgeContent={"loading..."}
                      color={"warning"}
                      container
                    />
                }
              </MDBox>
              <MDBox>
                {installedWorker.state
                  ?
                  <MDBox display="block" justifyContent="space-between" mt={2}>
                    <MDBox key={`element-1`} component="li" color="text" fontSize="1.25rem" lineHeight={1}>
                      <MDTypography variant="button" fontWeight="regular" color="text">
                        설치된 워커 노드
                      </MDTypography>
                    </MDBox>
                    <MDBox pl={3.5} mt={1}>
                      {installedWorker.hostName.length > 0
                        ?
                        installedWorker.hostName.map((data, idx) => {
                          return (
                            <MDTypography key={`worker-${idx}`} display="block" variant="button" fontWeight="regular" color="text">
                              {data}
                            </MDTypography>
                          )
                        })
                        :
                        <MDTypography variant="button" fontWeight="regular" color="text">
                          none
                        </MDTypography>
                      }
                    </MDBox>
                  </MDBox>
                  : null
                }
              </MDBox>
            </MDBox>
            <MDBox
              style={{
                borderRadius: 5,
                padding: 16,
                margin: "0 0 0px 0",
                border: "1px solid",
                borderColor: blue[800],
              }}
            >
              {dataApps.length > 0
                ?
                <MDBox>
                  <MDBox
                    fontSize="14px"
                    fontWeight="bold"
                    textTransform="capitalize"
                    style={{
                      color: blue[800],
                    }}
                  >
                    어플리케이션 설치 여부
                  </MDBox>
                  <MDBox mt={2}>
                    {dataApps.length > 0
                      ?
                      dataApps.map((app, idx) => {
                        return (
                          <MDBox key={`element-${idx}`}>
                            <MDBox display="flex" justifyContent="space-between" mt={0.5}>
                              <MDBox component="li" color="text" fontSize="1.25rem" lineHeight={1}>
                                <MDTypography variant="button" fontWeight="regular" color="text">
                                  {app.app_name}
                                </MDTypography>
                              </MDBox>
                              {
                                Object.keys(dataApps).length > 0
                                  ?
                                  <ReqBox
                                    name={"app"}
                                    data={app}
                                    setFailureCondition={setFailureCondition}
                                  />
                                  :
                                  <MDBadge
                                    variant="contained"
                                    size="xs"
                                    badgeContent={"loading..."}
                                    color={"warning"}
                                    container
                                  />
                              }
                            </MDBox>
                            {idx < dataApps.length - 1 ?
                              <Divider style={{ marginTop: 1, marginBottom: 1 }} />
                              : null}
                          </MDBox>
                        )
                      })
                      :
                      <MDTypography pl={3.5} variant="button" fontWeight="regular" color="text">
                        none
                      </MDTypography>
                    }
                  </MDBox>
                </MDBox>
                :
                <MDBox
                  display="flex"
                  justifyContent="space-between"
                  alignItems="center"
                  width={{ xs: "max-content", sm: "100%" }}
                >
                  <MDBox
                    fontSize="14px"
                    fontWeight="bold"
                    textTransform="capitalize"
                    style={{
                      color: blue[800],
                    }}
                  >
                    어플리케이션 설치 여부
                  </MDBox>
                  <MDBox>
                    <MDBadge
                      variant="contained"
                      size="xs"
                      badgeContent={"loading..."}
                      color={"warning"}
                      container
                    />
                  </MDBox>
                </MDBox>

              }
            </MDBox>
          </MDBox>
        </Collapse>
      </Box>
    </MDBox>
  );
}

export default ResComp0;