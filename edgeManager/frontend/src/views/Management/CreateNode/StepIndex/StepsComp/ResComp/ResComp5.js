import React from 'react';
import Box from '@mui/material/Box';
import Collapse from '@mui/material/Collapse';
import MDBox from 'components/MDBox';
import MDTypography from 'components/MDTypography';
import MDButton from 'components/MDButton';
import { Icon, Tooltip } from '@mui/material';
import { blue } from '@mui/material/colors';
import MDBadge from 'components/MDBadge';

function ResComp5({
  resOpen,
  setResOpen,
  resData,
}) {

  // React.useEffect(() => {
  //   console.log("resData: ", resData);
  // }, [resData]);

  const getReqBox = (data, idx) => {
    let content;
    let color;

    if (data.val.service_code === 200 && data.val.service_validate) {
      content = "추가완료";
      color = "success"
    } else {
      content = "추가실패";
      color = "error"
    };

    return (
      <MDBox key={`${data}-${idx}`}>
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
              {data.key}
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
            Response
          </MDTypography>
          {resData && resData.length > 0 &&
            <Tooltip title={resOpen ? "Close Response Box" : "Open Response Box"} placement="bottom" arrow>
              <MDButton variant="outlined" color="secondary" size="small" circular iconOnly onClick={() => {
                resOpen ? setResOpen({ ...resOpen, step5: false }) : setResOpen({ ...resOpen, step5: true })
              }}>
                {resOpen ? <Icon>expand_less</Icon> : <Icon>expand_more</Icon>}
              </MDButton>
            </Tooltip>
          }
        </MDBox>
        <Collapse in={resOpen}>
          {resData && resData.length > 0 && resData.map((data, idx) => {
            return getReqBox(data, idx);
          })}
        </Collapse>
      </Box>
    </>
  );
}

export default ResComp5;