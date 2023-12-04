import React from 'react';
import Box from '@mui/material/Box';
import Collapse from '@mui/material/Collapse';
import MDBox from 'components/MDBox';
import MDTypography from 'components/MDTypography';
import MDButton from 'components/MDButton';
import { Icon, Tooltip } from '@mui/material';
import { blue } from '@mui/material/colors';

function ResComp1({
  resOpen,
  setResOpen,
  resData,
}) {
  const scrollRefs = React.useRef([]);

  const scrollToBottom = () => {
    if (resData.length > 0 && scrollRefs.current) {
      resData.map((data, idx) => {
        scrollRefs.current[idx].scrollTop = scrollRefs.current[idx].scrollHeight;
      })
    };
  };

  React.useEffect(() => {
    scrollToBottom();
    // console.log("resData: ", resData);
    // console.log("scrollRefs: ", scrollRefs.current);
  }, [resData]);

  return (
    <MDBox>
      <Box sx={{ width: '100%' }}>
        <MDBox my={2} display="flex" justifyContent="space-between" alignItems="center" >
          <MDTypography variant="h6" color="info">
            Response
          </MDTypography>
          {resData && resData.length > 0 &&
            <Tooltip title={resOpen ? "Close Response Box" : "Open Response Box"} placement="bottom" arrow>
              <MDButton variant="outlined" color="secondary" size="small" circular iconOnly onClick={() => {
                resOpen ? setResOpen({ ...resOpen, step1: false }) : setResOpen({ ...resOpen, step1: true })
              }}>
                {resOpen ? <Icon>expand_less</Icon> : <Icon>expand_more</Icon>}
              </MDButton>
            </Tooltip>
          }
        </MDBox>
        <Collapse in={resOpen}>
          {resData && resData.length > 0 ?
            resData.map((data, idx) => {
              return (
                <MDBox key={`${data}-${idx}`} sx={{ overflow: "auto" }}>
                  <MDBox>
                    <MDTypography fontSize="14px" fontWeight="medium" color="info">
                      {data.key}
                    </MDTypography>
                  </MDBox>
                  <MDBox
                    style={{
                      borderRadius: 5,
                      margin: "0 0 8px 0",
                      border: "1px solid",
                      borderColor: blue[800],
                    }}
                  >
                    <MDBox
                      py={2}
                      // bgColor={"grey-200"}
                      borderRadius="lg"
                    >
                      <MDBox
                        px={2}
                        height="185px"
                        overflow="auto"
                        ref={(el) => (scrollRefs.current[idx] = el)}
                      >
                        <MDTypography sx={{ whiteSpace: "pre-wrap" }} fontSize="14px" fontWeight="medium" color="text">
                          {data.val}
                        </MDTypography>
                      </MDBox>
                    </MDBox>
                  </MDBox>
                </MDBox>
              )
            })
            : null}
        </Collapse>
      </Box>
    </MDBox>
  );
}

export default ResComp1;