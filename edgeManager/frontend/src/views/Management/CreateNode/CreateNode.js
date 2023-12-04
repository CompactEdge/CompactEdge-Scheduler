import React, { useState, useEffect } from "react";

// @mui material components
import Grid from "@mui/material/Grid";
import Stepper from "@mui/material/Stepper";
import Step from "@mui/material/Step";
import StepLabel from "@mui/material/StepLabel";
import Card from "@mui/material/Card";

// Material Dashboard 2 PRO React components
import MDBox from "components/MDBox";
import StepIndex from "./StepIndex/StepIndex";

import {
  Icon,
} from "@mui/material";

// NewProduct page components
const rootData =
  [
    {
      step: "서버 확인",
      content: [
        {
          title: "1. 서버 확인",
          field:
          {
            server: "",   // 10.7.20.104
            port: "",     // 22
            username: "", // wiz
            password: "", // qwe123
          },
        },
      ]
    },
    {
      step: "OS 업데이트",
      content: [
        {
          title: "2. OS 업데이트",
        },
      ]
    },
    {
      step: "OS 설정",
      content: [
        {
          title: "3. OS 설정",
        }
      ]
    },
    {
      step: "DOKER 설치",
      content: [
        {
          title: "4. DOKER 설치",
        }
      ]
    },
    {
      step: "K8S 설치",
      content: [
        {
          title: "5. K8S 설치",
        },
      ]
    },
    {
      step: "WORKER 노드 추가",
      content: [
        {
          title: "6. WORKER 노드 추가",
        },
      ]
    },
    {
      step: "WORKER 노드 확인",
      content: [
        {
          title: "7. WORKER 노드 확인",
        },
      ]
    },
  ];

function CreateNode() {
  const [stepIndex, setStepIndex] = useState(0);
  const [resetModalOpen, setResetModalOpen] = useState(false);
  const [isLastStep, setIsLastStep] = useState(false);

  const resetBtn = () => {
    setResetModalOpen(true)
  };

  const resetButton = (
    <MDBox
      display="flex"
      justifyContent="center"
      alignItems="center"
      width="3.25rem"
      height="3.25rem"
      bgColor="white"
      shadow="sm"
      borderRadius="50%"
      position="fixed"
      right="2rem"
      bottom="2rem"
      zIndex={99}
      color="dark"
      sx={{ cursor: "pointer" }}
      onClick={resetBtn}
    >
      <Icon fontSize="medium" color="inherit">
        replayout
      </Icon>
    </MDBox>
  );

  function getSteps() {
    let result = [];
    rootData.map(data => {
      result.push(data.step);
    });
    return result;
  };

  const steps = getSteps();
  // const isLastStep = activeStep === steps.length - 1;

  const handleNext = () => setStepIndex(stepIndex + 1);
  const handleBack = () => setStepIndex(stepIndex - 1);

  return (
    <>
      <MDBox mt={8} mb={9}>
        <Grid container justifyContent="center">
          <Grid item xs={12} lg={12}>
            <Card>
              <MDBox mt={-3} mb={3} mx={2}>
                <Stepper activeStep={stepIndex} alternativeLabel>
                  {steps.map((label) => (
                    <Step key={label}>
                      <StepLabel>{label}</StepLabel>
                    </Step>
                  ))}
                </Stepper>
              </MDBox>
              <MDBox p={4}>
                <MDBox mt={3}>
                  <StepIndex
                    rootData={rootData}
                    resetModalOpen={resetModalOpen}
                    setResetModalOpen={setResetModalOpen}
                    steps={steps}
                    stepIndex={stepIndex}
                    setStepIndex={setStepIndex}
                    isLastStep={isLastStep}
                    setIsLastStep={setIsLastStep}
                    handleNext={handleNext}
                    handleBack={handleBack}
                  />
                </MDBox>
              </MDBox>
            </Card>
          </Grid>
        </Grid>
        {resetButton}
      </MDBox>
    </>
  );
}

export default CreateNode;
