import React from 'react';

// Material Dashboard 2 PRO React components
import MDBox from "components/MDBox";
import MDTypography from "components/MDTypography";
import MDButton from "components/MDButton";
import ResComp2 from './ResComp/ResComp2';
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

function Step2({
  title,
  getResStep2,
  isReqLoading,
  resOpen,
  setResOpen,
  resData
}) {

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
          <MDButton variant="gradient" color="info" size="small" onClick={getResStep2} disabled={isReqLoading}>
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
          <ResComp2 resOpen={resOpen} setResOpen={setResOpen} resData={resData} />
        </MDBox>
      </div>
      {/* <Progress isLoading={isReqLoading} /> */}
    </>
  );
}

export default Step2;