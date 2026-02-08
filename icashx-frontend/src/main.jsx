import { BrowserRouter, Routes, Route } from "react-router-dom";
import AppWrapper from "./App";
import Dashboard from "./pages/Dashboard";
import Leads from "./pages/Leads";
import Properties from "./pages/Properties";
import Buyers from "./pages/Buyers";
import Contracts from "./pages/Contracts";
import Settings from "./pages/Settings";
import Login from "./pages/Login";
import Register from "./pages/Register";
import PrivateRoute from "./components/PrivateRoute";
import "./styles/globals.css";

import ReactDOM from "react-dom/client";
import React from "react";

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <BrowserRouter>
      <Routes>
        <Route element={<AppWrapper />}>
          <Route
            path="/"
            element={
              <PrivateRoute>
                <Dashboard />
              </PrivateRoute>
            }
          />
          <Route
            path="/leads"
            element={
              <PrivateRoute>
                <Leads />
              </PrivateRoute>
            }
          />
          <Route
            path="/properties"
            element={
              <PrivateRoute>
                <Properties />
              </PrivateRoute>
            }
          />
          <Route
            path="/buyers"
            element={
              <PrivateRoute>
                <Buyers />
              </PrivateRoute>
            }
          />
          <Route
            path="/contracts"
            element={
              <PrivateRoute>
                <Contracts />
              </PrivateRoute>
            }
          />
          <Route
            path="/settings"
            element={
              <PrivateRoute>
                <Settings />
              </PrivateRoute>
            }
          />
          <Route path="/login" element={<Login />} />
          <Route path="/register" element={<Register />} />
        </Route>
      </Routes>
    </BrowserRouter>
  </React.StrictMode>
);