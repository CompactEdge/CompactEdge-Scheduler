import React from 'react';
import axios from 'axios';
import Step0 from './StepsComp/Step0';
import Step1 from './StepsComp/Step1';
import Step2 from './StepsComp/Step2';
import Step3 from './StepsComp/Step3';
import Step4 from './StepsComp/Step4';
import Step5 from './StepsComp/Step5';
import Step6 from './StepsComp/Step6';
import StepContents from './StepsComp/StepContents';
import {
  Dialog,
  DialogTitle,
  DialogContent,
  DialogContentText,
  DialogActions,
} from "@mui/material";
import MDButton from 'components/MDButton';
import MDBox from 'components/MDBox';

const initData = {
  step0: null,
  step1: [],
  step2: {},
  step3: [],
  step4: [],
  step5: [],
  step6: [],
}

function StepIndex({
  rootData,
  resetModalOpen,
  setResetModalOpen,
  steps,
  stepIndex,
  setStepIndex,
  isLastStep,
  setIsLastStep,
  handleNext,
  handleBack
}) {
  const [nextBtn, setNextBtn] = React.useState(false);
  const [stepData, setStepData] = React.useState(rootData[0].content);
  const [fieldData, setFieldData] = React.useState(rootData[0].content[0].field);
  const [isReqLoading, setIsReqLoading] = React.useState({
    step0: false,
    step1: false,
    step2: false,
    step3: false,
    step4: false,
    step5: false,
    step6: false
  });
  const [resData, setResData] = React.useState(initData);
  const [resOpen, setResOpen] = React.useState({
    step0: false,
    step1: false,
    step2: false,
    step3: false,
    step4: false,
    step5: false,
    step6: true
  });
  // log
  const [reqSignal, setReqSignal] = React.useState({
    step1: false,
    step3: false,
    step4: false,
  });
  const [stepCompletion, setStepCompletion] = React.useState([
    false,
    false,
    false,
    false,
    false,
    false,
    false
  ]);
  const [failureCondition, setFailureCondition] = React.useState([]);
  const [finishModalOpen, setFinishModalOpen] = React.useState(false);

  React.useEffect(() => {
    // console.log("failureCondition: ", failureCondition);
    if (failureCondition.length === 4) {
      let count = 0;
      failureCondition.map(data => {
        count = count + data;
      });
      // console.log("count: ",count);
      if (count > 0) {
        setNextBtn(false);
      } else {
        setNextBtn(true);
      };
    };
  }, [failureCondition])

  React.useEffect(() => {
    // console.log("step: ", stepIndex);
    setStepData(rootData[stepIndex].content);
    if (stepIndex === steps.length - 1) {
      setIsLastStep(true);
    } else {
      setIsLastStep(false);
    };
    if (stepCompletion[stepIndex]) {
      setNextBtn(true);
    } else {
      setNextBtn(false);
    };
  }, [stepIndex])

  React.useEffect(() => {
    // console.log("stepCompletion: ", stepCompletion);
    if (stepCompletion[stepIndex]) {
      if (stepIndex !== 0) {
        setNextBtn(true);
      };
    }
  }, [stepCompletion]);

  // React.useEffect(() => {
  //   console.log("resData: ", resData);
  // }, [resData]);

  // React.useEffect(() => {
  //   console.log("nextBtn: ", nextBtn);
  // }, [nextBtn]);

  // get res functions ------------------------------------------------------------------------------ start
  const getResStep0 = () => {
    setFailureCondition([]);
    setResData(prev => ({ ...prev, step0: null }));
    if (fieldData.server && fieldData.port && fieldData.username && fieldData.password) {
      setResOpen(prev => ({ ...prev, step0: true }));
      setIsReqLoading(prev => ({ ...prev, step0: true }));
      // console.log(fieldData.server, fieldData.port, fieldData.username, fieldData.password);
      let reqUrl = `/rest/1.0/remote_control/validate_node_health_management?server=${fieldData.server}&port=${fieldData.port}&username=${fieldData.username}&password=${fieldData.password}`;
      axios(reqUrl)
        .then((res) => {
          setIsReqLoading(prev => ({ ...prev, step0: false }));
          setResData(prev => ({ ...prev, step0: res.data }));
          //
          let newArr = [...stepCompletion];
          newArr[stepIndex] = true;
          setStepCompletion(newArr);
        })
        .catch((e) => {
          console.log("error: ", e);
          alert("데이터 조회에 실패했습니다.");
          setIsReqLoading(prev => ({ ...prev, step0: false }));
          setResOpen(prev => ({ ...prev, step0: false }));
          setResData(prev => ({ ...prev, step0: null }));
        });
    } else {
      setIsReqLoading(prev => ({ ...prev, step0: false }));
      alert("데이터를 입력해 주세요!");
    };
  };
  const getResStep1 = () => {
    setResData(prev => ({ ...prev, step1: [] }));
    setResOpen(prev => ({ ...prev, step1: true }));
    setIsReqLoading(prev => ({ ...prev, step1: true }));
    let reqUrl = `/rest/1.0/remote_control/execute_default_package_management`;
    setReqSignal(prev => ({ ...prev, step1: true }));
    axios(reqUrl)
      .then((res) => {
        setReqSignal(prev => ({ ...prev, step1: false }));
        setIsReqLoading(prev => ({ ...prev, step1: false }));
        let resObj = res.data;
        let dataObj;
        let dataArry = [];
        let dataKeys = Object.keys(resObj);
        for (let i = 0; i < dataKeys.length; i++) {
          dataObj = { key: dataKeys[i], val: resObj[dataKeys[i]].service_result }
          dataArry[i] = dataObj;
        };
        console.log("dataArry 2: ", dataArry);
        setResData(prev => ({ ...prev, step1: dataArry }));
        //
        let newArr = [...stepCompletion];
        newArr[stepIndex] = true;
        setStepCompletion(newArr);
      })
      .catch((e) => {
        console.log("error: ", e);
        alert("데이터 조회에 실패했습니다.");
        setReqSignal(prev => ({ ...prev, step1: false }));
        setIsReqLoading(prev => ({ ...prev, step1: false }));
      });
  };
  const getResStep2 = () => {
    setResData(prev => ({ ...prev, step2: {} }));
    setResOpen(prev => ({ ...prev, step2: true }));
    setIsReqLoading(prev => ({ ...prev, step2: true }));
    let reqUrl = `/rest/1.0/remote_control/execute_default_preferences_management`;
    axios(reqUrl)
      .then((res) => {
        setIsReqLoading(prev => ({ ...prev, step2: false }));
        setResData(prev => ({ ...prev, step2: res.data }));
        //
        let newArr = [...stepCompletion];
        newArr[stepIndex] = true;
        setStepCompletion(newArr);
      })
      .catch((e) => {
        console.log("error: ", e);
        alert("데이터 조회에 실패했습니다.");
        setIsReqLoading(prev => ({ ...prev, step2: false }));
      });
  };
  const getResStep3 = () => {
    setReqSignal(prev => ({ ...prev, step3: true }));
    setResData(prev => ({ ...prev, step3: [] }));
    setResOpen(prev => ({ ...prev, step3: true }));
    setIsReqLoading(prev => ({ ...prev, step3: true }));
    let reqUrl = `/rest/1.0/remote_control/execute_install_docker`;
    axios(reqUrl)
      .then((res) => {
        setReqSignal(prev => ({ ...prev, step3: false }));
        setIsReqLoading(prev => ({ ...prev, step3: false }));
        let resObj = res.data;
        let dataObj;
        let dataArry = [];
        let dataKeys = Object.keys(resObj);
        for (let i = 0; i < dataKeys.length; i++) {
          dataObj = { key: dataKeys[i], val: resObj[dataKeys[i]] }
          dataArry[i] = dataObj;
        };
        console.log("dataArry 2: ", dataArry);
        setResData(prev => ({ ...prev, step3: dataArry }));
        //
        let newArr = [...stepCompletion];
        newArr[stepIndex] = true;
        setStepCompletion(newArr);
      })
      .catch((e) => {
        console.log("error: ", e);
        alert("데이터 조회에 실패했습니다.");
        setReqSignal(prev => ({ ...prev, step3: false }));
        setIsReqLoading(prev => ({ ...prev, step3: false }));
      });
  };
  const getResStep4 = () => {
    setReqSignal(prev => ({ ...prev, step4: true }));
    setResData(prev => ({ ...prev, step4: [] }));
    setResOpen(prev => ({ ...prev, step4: true }));
    setIsReqLoading(prev => ({ ...prev, step4: true }));
    let reqUrl = `/rest/1.0/remote_control/execute_install_k8s`;
    axios(reqUrl)
      .then((res) => {
        setReqSignal(prev => ({ ...prev, step4: false }));
        setIsReqLoading(prev => ({ ...prev, step4: false }));
        let resObj = res.data;
        let dataObj;
        let dataArry = [];
        let dataKeys = Object.keys(resObj);
        for (let i = 0; i < dataKeys.length; i++) {
          dataObj = { key: dataKeys[i], val: resObj[dataKeys[i]] }
          dataArry[i] = dataObj;
        };
        console.log("dataArry 2: ", dataArry);
        setResData(prev => ({ ...prev, step4: dataArry }));
        //
        let newArr = [...stepCompletion];
        newArr[stepIndex] = true;
        setStepCompletion(newArr);
      })
      .catch((e) => {
        console.log("error: ", e);
        alert("데이터 조회에 실패했습니다.");
        setReqSignal(prev => ({ ...prev, step4: false }));
        setIsReqLoading(prev => ({ ...prev, step4: false }));
      });
  };
  const getResStep5 = () => {
    setResData(prev => ({ ...prev, step5: [] }));
    setResOpen(prev => ({ ...prev, step5: true }));
    setIsReqLoading(prev => ({ ...prev, step5: true }));
    let reqUrl = `/rest/1.0/remote_control/execute_join_k8s_worker_node`;
    axios(reqUrl)
      .then((res) => {
        setIsReqLoading(prev => ({ ...prev, step5: false }));
        let resObj = res.data;
        let dataObj;
        let dataArry = [];
        let dataKeys = Object.keys(resObj);
        for (let i = 0; i < dataKeys.length; i++) {
          dataObj = { key: dataKeys[i], val: resObj[dataKeys[i]] }
          dataArry[i] = dataObj;
        };
        console.log("dataArry : ", dataArry);
        setResData(prev => ({ ...prev, step5: dataArry }));
        //
        let newArr = [...stepCompletion];
        newArr[stepIndex] = true;
        setStepCompletion(newArr);
      })
      .catch((e) => {
        console.log("error: ", e);
        alert("데이터 조회에 실패했습니다.");
        setIsReqLoading(prev => ({ ...prev, step5: false }));
      });
  };
  const getResStep6 = () => {
    setResData(prev => ({ ...prev, step6: [] }));
    setIsReqLoading(prev => ({ ...prev, step6: true }));
    let reqUrl = `/rest/1.0/k8s/node_status`;
    axios(reqUrl)
      .then((res) => {
        setIsReqLoading(prev => ({ ...prev, step6: false }));
        setResData(prev => ({ ...prev, step6: res.data }));
      })
      .catch((e) => {
        console.log("error: ", e);
        alert("데이터 조회에 실패했습니다.");
        setIsReqLoading(prev => ({ ...prev, step6: false }));
      });
  };
  // get res functions ------------------------------------------------------------------------------ end

  const getContent = (data, idx) => {
    if (stepIndex === 0) {
      return (
        <div key={`${data.title}_${idx}`}>
          <Step0
            title={data.title}
            getResStep0={getResStep0}
            fieldData={fieldData}
            setFieldData={setFieldData}
            isReqLoading={isReqLoading.step0}
            resOpen={resOpen.step0}
            setResOpen={setResOpen}
            resData={resData.step0}
            setFailureCondition={setFailureCondition}
          />
        </div>
      );
    } else if (stepIndex === 1) {
      return (
        <div key={`${data.title}_${idx}`}>
          <Step1
            title={data.title}
            getResStep1={getResStep1}
            isReqLoading={isReqLoading.step1}
            resOpen={resOpen.step1}
            setResOpen={setResOpen}
            reqSignal={reqSignal.step1}
            setReqSignal={setReqSignal}
            resData={resData}
            setResData={setResData}
          />
        </div>
      )
    } else if (stepIndex === 2) {
      return (
        <div key={`${data.title}_${idx}`}>
          <Step2
            title={data.title}
            getResStep2={getResStep2}
            isReqLoading={isReqLoading.step2}
            resOpen={resOpen.step2}
            setResOpen={setResOpen}
            resData={resData.step2}
            setResData={setResData}
          />
        </div>
      )
    } else if (stepIndex === 3) {
      return (
        <div key={`${data.title}_${idx}`}>
          <Step3
            title={data.title}
            getResStep3={getResStep3}
            isReqLoading={isReqLoading.step3}
            resOpen={resOpen.step3}
            setResOpen={setResOpen}
            reqSignal={reqSignal.step3}
            setReqSignal={setReqSignal}
            resData={resData}
            setResData={setResData}
          />
        </div>
      )
    } else if (stepIndex === 4) {
      return (
        <div key={`${data.title}_${idx}`}>
          <Step4
            title={data.title}
            getResStep4={getResStep4}
            isReqLoading={isReqLoading.step4}
            resOpen={resOpen.step4}
            setResOpen={setResOpen}
            reqSignal={reqSignal.step4}
            resData={resData}
            setResData={setResData}
          />
        </div>
      )
    } else if (stepIndex === 5) {
      return (
        <div key={`${data.title}_${idx}`}>
          <Step5
            title={data.title}
            getResStep5={getResStep5}
            isReqLoading={isReqLoading.step5}
            resOpen={resOpen.step5}
            setResOpen={setResOpen}
            resData={resData}
          />
        </div>
      )
    } else if (stepIndex === 6) {
      return (
        <div key={`${data.title}_${idx}`}>
          <Step6
            title={data.title}
            getResStep6={getResStep6}
            isReqLoading={isReqLoading.step6}
            resOpen={resOpen.step6}
            setResOpen={setResOpen}
            resData={resData.step6}
            setResData={setResData}
          />
        </div>
      )
    }
    return (
      <div key={`${data.title}_${idx}`}>
        <StepContents title={data.title} stepContentData={data.content} />
      </div>
    );
  };

  const handleResetBtn = () => {
    let reqUrl = `/rest/1.0/remote_control/init_sessions`;
    axios(reqUrl)
      .then((res) => {
        // console.log("res: ", res.data);
        setStepIndex(0);
        setResData(prev => ({ ...prev, ...initData }));
        setResOpen(prev =>  ({ ...prev, step0: false, step1: false, step2: false, step3: false, step4: false }));
        setFieldData(rootData[0].content[0].field);
        resetModalOpen && setResetModalOpen(false);
        finishModalOpen && setFinishModalOpen(false);
        setNextBtn(false);
      })
      .catch((e) => {
        console.log("error: ", e);
      });
  };

  const getStepLoad = () => {
    let result;
    Object.keys(isReqLoading).map((key, idx) => {
      if (idx === stepIndex) {
        result = isReqLoading[key];
      };
    });
    return result;
  };

  return (
    <>
      {stepData && stepData.map((data, idx) => {
        return getContent(data, idx);
      })}

      <MDBox mt={3} width="100%" display="flex" justifyContent="space-between">
        {stepIndex === 0 ? (
          <MDBox />
        ) : (
          <MDButton
            variant="gradient"
            color="light"
            onClick={handleBack}
            disabled={getStepLoad()}
          >
            back
          </MDButton>
        )}
        {isLastStep ? (
          <MDButton
            variant="gradient"
            color="dark"
            onClick={() => {setFinishModalOpen(true)}}
          >
            finish
          </MDButton>
        ) : (
          <MDButton
            variant="gradient"
            color="dark"
            disabled={!nextBtn || getStepLoad()}
            onClick={handleNext}
          >
            next
          </MDButton>
        )}
      </MDBox>

      <Dialog
        fullWidth
        open={resetModalOpen}
        onClose={() => { setResetModalOpen(false) }}
        aria-labelledby="alert-dialog-title"
        aria-describedby="alert-dialog-description"
      >
        <DialogTitle id="alert-dialog-title">reset</DialogTitle>
        <DialogContent>
          <DialogContentText id="alert-dialog-description">
            초기화 하시겠습니까?
          </DialogContentText>
        </DialogContent>
        <DialogActions>
          <MDButton variant="contained" onClick={handleResetBtn} color="info">
            확인
          </MDButton>
          <MDButton variant="contained" onClick={() => { setResetModalOpen(false) }} color="dark">
            취소
          </MDButton>
        </DialogActions>
      </Dialog>

      <Dialog
        fullWidth
        open={finishModalOpen}
        onClose={() => { setFinishModalOpen(false) }}
        aria-labelledby="alert-dialog-title"
        aria-describedby="alert-dialog-description"
      >
        <DialogTitle id="alert-dialog-title">Node creation completed!</DialogTitle>
        <DialogContent>
          <DialogContentText id="alert-dialog-description">
            노드 생성이 완료됐습니다.
          </DialogContentText>
        </DialogContent>
        <DialogActions>
          <MDButton variant="contained" onClick={handleResetBtn} color="info">
            확인
          </MDButton>
        </DialogActions>
      </Dialog>
    </>
  );
}

export default StepIndex;