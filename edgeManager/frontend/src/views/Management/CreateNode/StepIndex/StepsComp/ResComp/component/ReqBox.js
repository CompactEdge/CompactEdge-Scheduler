import React, { useEffect, useState } from 'react';
import MDBadge from 'components/MDBadge';

const ReqBox = ({
  name,
  data,
  setFailureCondition,
}) => {

  const [property, setProperty] = useState({
    content: "loading...",
    color: "warning"
  });

  useEffect(() => {
    if (name === "node") {
      if (data.service_code === 200 && data.service_validate) {
        setProperty(prev => ({ ...prev, content: "접속가능", color: "success" }));
        setFailureCondition(prev => [...prev, 0]);
      } else {
        setProperty(prev => ({ ...prev, content: "접속불가", color: "error" }));
        setFailureCondition(prev => [...prev, 1]);
      };
    }
    else if (name === "worker") {
      if (data.service_code === 200 && data.service_validate) {
        setProperty(prev => ({ ...prev, content: "설치가능", color: "success" }));
        setFailureCondition(prev => [...prev, 0]);
      } else {
        setProperty(prev => ({ ...prev, content: "설치불가", color: "error" }));
        setFailureCondition(prev => [...prev, 1]);
      };
    }
    else if (name === "app") {
      if (data.app_validate) {
        setProperty(prev => ({ ...prev, content: "설치가능", color: "success" }));
        setFailureCondition(prev => [...prev, 0]);
      } else {
        setProperty(prev => ({ ...prev, content: "설치불가", color: "error" }));
        setFailureCondition(prev => [...prev, 1]);
      };
    }
  }, [data]);

  return (
    <MDBadge
      variant="contained"
      size="xs"
      badgeContent={property.content}
      color={property.color}
      container
    />
  );
};

export default ReqBox;