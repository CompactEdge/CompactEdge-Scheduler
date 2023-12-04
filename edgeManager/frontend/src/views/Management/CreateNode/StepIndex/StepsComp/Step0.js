import React from 'react';
import MDBox from "components/MDBox";
import MDTypography from "components/MDTypography";
import MDButton from "components/MDButton";
import StepContentsInfo from './StepContentsInfo/StepContentsInfo';
import DialogComp from './DialogComp/DialogComp';
import ResComp0 from './ResComp/ResComp0';
import styled from "styled-components";
import { CircularProgress } from '@mui/material';

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

function Step0({
  title,
  getResStep0,
  fieldData,
  setFieldData,
  isReqLoading,
  resOpen,
  setResOpen,
  resData,
  setFailureCondition,
}) {
  const [dialogOpen, setDialogOpen] = React.useState(false);

  const onEditBTN = () => {
    setDialogOpen(true);
  };
  const handleOnClose = () => {
    setDialogOpen(false);
  };

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
        <MDBox
          display="flex"
          justifyContent="flex-end"
          width="155px"
        >
          <MDButton
            sx={{ px: 7 }}
            variant="gradient"
            color="secondary"
            size="small"
            onClick={onEditBTN}
            disabled={isReqLoading}
          >
            edit
          </MDButton>
          <MDButton
            sx={{ ml: 1, px: 7 }}
            variant="gradient"
            color="info"
            size="small"
            onClick={getResStep0}
            disabled={isReqLoading}>
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
        {/* info box */}
        <MDBox mt={1} >
          {fieldData && Object.keys(fieldData).map((infoKey, idx) => {
            return <StepContentsInfo key={`${infoKey}_${idx}`} infoKey={infoKey} infoVal={fieldData[infoKey]} />
          })}
          {/* result area */}
          <MDBox mt={2} />
          <ResComp0
            resOpen={resOpen}
            setResOpen={setResOpen}
            resData={resData}
            setFailureCondition={setFailureCondition}
          />
        </MDBox>
      </div>
      <DialogComp
        dialogOpen={dialogOpen}
        setDialogOpen={setDialogOpen}
        handleOnClose={handleOnClose}
        fieldData={fieldData}
        setFieldData={setFieldData}
      />
    </>
  );
}

export default Step0;