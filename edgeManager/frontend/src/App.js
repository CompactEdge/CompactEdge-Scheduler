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

import { Fragment, useEffect, useMemo, useState } from "react";

// react-router components
import { Navigate, Route, Routes, useLocation } from "react-router-dom";

// @mui material components
import CssBaseline from "@mui/material/CssBaseline";
import { ThemeProvider } from "@mui/material/styles";

// Material Dashboard 2 PRO React examples
import Sidenav from "modules/Sidenav";

// Material Dashboard 2 PRO React themes
import theme from "assets/theme";

// RTL plugins
import createCache from "@emotion/cache";
import rtlPlugin from "stylis-plugin-rtl";

// Material Dashboard 2 PRO React routes
import routes from "routes";

// Material Dashboard 2 PRO React contexts
import { setMiniSidenav, useMaterialUIController } from "context";

// Images
import brandDark from "assets/images/logo-ct-dark.png";
import brandWhite from "assets/images/logo-ct.png";
import * as config from "config";
import DashboardLayout from "modules/LayoutContainers/DashboardLayout";
import PageLayout from "modules/LayoutContainers/PageLayout";

let sideTitle = config.sideTitle;

export default function App() {
  const [controller, dispatch] = useMaterialUIController();
  const {
    miniSidenav,
    direction,
    layout,
    sidenavColor,
    transparentSidenav,
    whiteSidenav,
    darkMode,
  } = controller;
  const [onMouseEnter, setOnMouseEnter] = useState(false);
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

  // Open sidenav when mouse enter on mini sidenav
  const handleOnMouseEnter = () => {
    if (miniSidenav && !onMouseEnter) {
      setMiniSidenav(dispatch, false);
      setOnMouseEnter(true);
    }
  };

  // Close sidenav when mouse leave mini sidenav
  const handleOnMouseLeave = () => {
    if (onMouseEnter) {
      setMiniSidenav(dispatch, true);
      setOnMouseEnter(false);
    }
  };

  // Setting the dir attribute for the body element
  useEffect(() => {
    document.body.setAttribute("dir", direction);
  }, [direction]);

  // Setting page scroll to 0 when changing the route
  useEffect(() => {
    document.documentElement.scrollTop = 0;
    document.scrollingElement.scrollTop = 0;
  }, [pathname]);

  const getRoutes = (allRoutes) =>
    allRoutes.map((route) => {
      if (route.collapse) {
        return getRoutes(route.collapse);
      }

      if (route.route) {
        return (
          <Route
            exact
            path={route.route}
            element={<DashboardLayout>{route.component}</DashboardLayout>}
            key={route.key}
          />
        );
      }

      return null;
    });

  const getPages = (allRoutes) =>
    allRoutes.map((route) => {
      if (route.collapse) {
        return getPages(route.collapse);
      }

      if (route.route) {
        return (
          <Route
            exact
            path={"/frame" + route.route.replace("/views", "")}
            element={<PageLayout>{route.component}</PageLayout>}
            key={route.key}
          />
        );
      }

      return null;
    });

  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      {layout === "dashboard" && (
        <Fragment>
          <Sidenav
            color={sidenavColor}
            brand={(transparentSidenav && !darkMode) || whiteSidenav ? brandDark : brandWhite}
            brandName={sideTitle}
            routes={routes}
            onMouseEnter={handleOnMouseEnter}
            onMouseLeave={handleOnMouseLeave}
          />
        </Fragment>
      )}

      <Routes>
        {getPages(routes)}
        {getRoutes(routes)}
        <Route path="/frame/*" element={<Navigate to="/frame/monitoring/edgeMonitoring" />} />
        <Route path="*" element={<Navigate to="/views/monitoring/edgeMonitoring" />} />
      </Routes>
    </ThemeProvider>
  );
}
