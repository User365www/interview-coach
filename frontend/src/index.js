import React from "react";
import { createRoot } from "react-dom/client";
import App from "./App";

const appDiv = document.getElementById("app");
if (!appDiv) throw new Error("Root element 'app' not found");

const root = createRoot(appDiv);
root.render(<App />);