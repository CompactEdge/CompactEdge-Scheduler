import React from 'react';

// Material Dashboard 2 PRO React components
import MDBox from "components/MDBox";
import MDTypography from "components/MDTypography";
import MDButton from "components/MDButton";
import axios from 'axios';
import ResComp4 from './ResComp/ResComp4';
import Progress from 'views/Components/Progress/Progress';
import { CircularProgress } from '@mui/material';
import styled from "styled-components";

const CircularDiv = styled.div`
    display: flex;
    justify-content: center;
`;

const LoadStateWrap = styled.div`
    display: flex;
    flex-flow: column;
    justify-content: center;
    margin-right: 1rem;
`;

function Step4({
  title,
  getResStep4,
  isReqLoading,
  resOpen,
  setResOpen,
  reqSignal,
  resData,
  setResData,
}) {
  // state for child
  const [reqId, setReqId] = React.useState();

  const getLog = () => {
    axios('/rest/1.0/remote_control/working_progress_logs?service_type=execute_install_k8s')
      .then((res) => {
        let resObj = res.data;
        // console.log("resObj: ", resObj);
        let dataObj;
        let dataArry = [];
        let dataKeys = Object.keys(resObj);
        for (let i = 0; i < dataKeys.length; i++) {
          // console.log("???: ", resObj[dataKeys[i]]);
          dataObj = { key: dataKeys[i], val: resObj[dataKeys[i]] }
          // dataArry[i] = resObj[dataKeys[i]].service_result;
          dataArry[i] = dataObj;
        };
        // console.log("dataArry: ", dataArry);
        setResData({ ...resData, step4: dataArry });
      })
      .catch((e) => {
        console.log("error: ", e);
      });
  };

  React.useEffect(() => {
    console.log("reqSignal: ", reqSignal);
    if (reqSignal) {
      let reqIdTmp = setInterval(getLog, 3000);
      setReqId(reqIdTmp);
    } else {
      clearInterval(reqId);
    }
  }, [reqSignal]);

  return (
    <>
      <MDBox
        pb={1}
        display="flex"
        justifyContent="space-between"
      >
        <MDTypography variant="h6" fontWeight="medium" textTransform="capitalize">
          {title}
        </MDTypography>
        <MDBox display="flex" justifyContent="space-between">
          <MDButton variant="gradient" color="info" size="small" onClick={getResStep4} disabled={isReqLoading}>
            {isReqLoading ? (
              <>
                <LoadStateWrap>
                  <CircularDiv>
                    <CircularProgress color="inherit" size="16px" />
                  </CircularDiv>
                </LoadStateWrap>
                loading
              </>
            ) : (
              "execute"
            )}
          </MDButton>
        </MDBox>
      </MDBox>

      <div
        style={{
          borderRadius: 5,
          border: "1px solid lightgrey",
          padding: 8,
          height: "100%",
        }}
      >
        <MDBox mt={1} >
          {/* result area */}
          <MDBox mt={2} />
          <ResComp4 resOpen={resOpen} setResOpen={setResOpen} resData={resData.step4} />
        </MDBox>
      </div>
      {/* <Progress isLoading={isReqLoading} /> */}
    </>
  );
}

export default Step4;