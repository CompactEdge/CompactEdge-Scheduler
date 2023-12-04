import React from 'react';
import MDBox from 'components/MDBox';
import MDTypography from 'components/MDTypography';
import MDButton from 'components/MDButton';
import { Icon, Tooltip } from '@mui/material';
import { blue } from '@mui/material/colors';
import Box from '@mui/material/Box';
import Collapse from '@mui/material/Collapse';
import MDBadge from 'components/MDBadge';

function ResComp6({
  resOpen,
  setResOpen,
  resData
}) {

  const getReqBox = (node, idx) => {
    let content;
    let color;

    if (node.status === "Ready") {
      content = node.status;
      color = "success"
    } else {
      content = node.status;
      color = "error"
    };

    return (
      <MDBox key={`${node}-${idx}`}>
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
              {node.name}
            </MDBox>
            <MDBox>
              <MDBadge
                variant="contained"
                size="xs"
                badgeContent={content}
                color={color}
                container
              />
            </MDBox>
          </MDBox>
        </MDBox>
      </MDBox>
    );
  };

  return (
    <>
      <Box sx={{ width: '100%' }}>
        <MDBox my={2} display="flex" justifyContent="space-between" alignItems="center" >
          <MDTypography variant="h6" color="info">
            설치된 WORKER 노드
          </MDTypography>
          {resData.length > 0 &&
            <Tooltip title={resOpen ? "Close Response Box" : "Open Response Box"} placement="bottom" arrow>
              <MDButton variant="outlined" color="secondary" size="small" circular iconOnly onClick={() => {
                resOpen ? setResOpen({ ...resOpen, step6: false }) : setResOpen({ ...resOpen, step6: true })
              }}>
                {resOpen ? <Icon>expand_less</Icon> : <Icon>expand_more</Icon>}
              </MDButton>
            </Tooltip>
          }
        </MDBox>
        <Collapse in={resOpen}>
          {resData.length > 0 && resData.map((node, idx) => {
            return getReqBox(node, idx);
          })}
        </Collapse>
      </Box>
    </>
  );
}

export default ResComp6;