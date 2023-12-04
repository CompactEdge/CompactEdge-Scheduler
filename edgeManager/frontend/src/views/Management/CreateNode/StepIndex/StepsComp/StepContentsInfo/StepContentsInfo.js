import React from 'react';
import MDBox from 'components/MDBox';

const styleComp = {
  font: {
    size: "14px",
    lineSpace: 0,
  }
};

const getPassword = (infoVal) => {
  let infoValArry = [...infoVal];
  let resultPW = [];
  for (let i = 0; i < infoValArry.length; i++) {
    resultPW.push("*");
  };
  return resultPW.join("");
}

function StepContentsInfo({ infoKey, infoVal }) {
  return (
    <MDBox mb={styleComp.font.lineSpace} display="flex">
      <MDBox fontSize={styleComp.font.size} fontWeight="bold">
        {infoKey}
      </MDBox>
      {infoVal
        ?
        <MDBox ml={1} fontSize={styleComp.font.size} color="text">
          {infoKey === "password" ? getPassword(infoVal) : infoVal}
        </MDBox>
        :
        <MDBox ml={1} fontSize={styleComp.font.size} color="warning">
          Please enter data.
        </MDBox>
      }
    </MDBox>
  );
}

export default StepContentsInfo;