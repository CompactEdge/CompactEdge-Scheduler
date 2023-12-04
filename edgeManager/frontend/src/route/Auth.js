/**
=========================================================
* Material Dashboard 2 PRO React - v2.1.0
=========================================================

* Product Page: https://www.creative-tim.com/product/material-dashboard-pro-react
* Copyright 2022 Creative Tim (https://www.creative-tim.com)

Coded by www.creative-tim.com

 =========================================================

* The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
*/

import { useEffect, useMemo, useState } from "react";

// react-router components
import { Navigate, Route, Routes, useLocation } from "react-router-dom";

// RTL plugins
import createCache from "@emotion/cache";
import rtlPlugin from "stylis-plugin-rtl";

// Material Dashboard 2 PRO React routes
import routes from "routes.js";

// Material Dashboard 2 PRO React contexts
import { useMaterialUIController } from "context";

export default function Auth() {
  const [controller] = useMaterialUIController();
  const {
    direction,
    layout,
  } = controller;
  const [rtlCache, setRtlCache] = useState(null);
  const { pathname } = useLocation();

  // Cache for the rtl
  useMemo(() => {
    const cacheRtl = createCache({
      key: "rtl",
      stylisPlugins: [rtlPlugin],
    });

    setRtlCache(cacheRtl);
  }, []);

  // Setting the dir attribute for the body element
  useEffect(() => {
    console.log("layout?: ", layout);
  }, []);

  useEffect(() => {
    document.body.setAttribute("dir", direction);
    console.log("direction: ", direction);
  }, [direction]);

  // Setting page scroll to 0 when changing the route
  useEffect(() => {
    document.documentElement.scrollTop = 0;
    document.scrollingElement.scrollTop = 0;
  }, [pathname]);

  const getRoutes = (routes) => {
    // console.log("routes:", routes)
    routes.map((prop, key) => {
      if (prop.layout === "/auth") {
        return (
          <Route
            path={prop.layout + prop.route}
            element={prop.component}
            key={key}
          />
        );
      }
    });
  };

  return (
    <>
      {/* <CssBaseline /> */}
      <Routes>
        {getRoutes(routes)}
        <Route path="/auth/*" element={<Navigate to="/auth/login-page" />} />
      </Routes>
    </>
  );
}
