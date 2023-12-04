import React from 'react';
import {
  Dialog,
  DialogTitle,
  DialogContent,
  DialogContentText,
  TextField,
  DialogActions,
  IconButton,
} from "@mui/material";
import CloseIcon from '@mui/icons-material/Close';
import MDBox from 'components/MDBox';
import MDButton from 'components/MDButton';

function DialogComp({
  dialogOpen,
  setDialogOpen,
  handleOnClose,
  fieldData,
  setFieldData
}) {

  const handleOnChange = (e) => {
    let infoKey = e.target.name;
    setFieldData({ ...fieldData, [infoKey]: e.target.value });
  };

  return (
    <>
      <Dialog
        fullWidth
        open={dialogOpen}
        onClose={handleOnClose}
        aria-labelledby="alert-dialog-title"
        aria-describedby="alert-dialog-description"
      >
        <MDBox display="flex" justifyContent="space-between" alignItems="center">
          <DialogTitle id="alert-dialog-title">Edit</DialogTitle>
          <IconButton
            style={{ marginRight: "7px" }}
            aria-label="close"
            color="inherit"
            onClick={() => {
              setDialogOpen(false);
            }}
          >
            <CloseIcon />
          </IconButton>
        </MDBox>
        <DialogContent dividers>
          {fieldData && Object.keys(fieldData).map((infoKey, idx) => {
            return (
              <MDBox key={`${infoKey}_${idx}`} mb={2}>
                <DialogContentText id="alert-dialog-description">
                  {infoKey}
                </DialogContentText>
                <TextField
                  type={infoKey === "password" ? "password" : null}
                  fullWidth
                  name={infoKey}
                  value={fieldData[infoKey]}
                  id={`${infoKey}_${idx}`}
                  variant="outlined"
                  onChange={handleOnChange}
                >
                </TextField>
              </MDBox>
            )
          })}
        </DialogContent>

        <DialogActions>
          <MDButton variant="gradient" color="info" onClick={handleOnClose}>Save</MDButton>
        </DialogActions>
      </Dialog>
    </>
  );
}

export default DialogComp;