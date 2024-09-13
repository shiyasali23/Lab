import { BrowserRouter, Routes, Route } from "react-router-dom";

import LoginPage from "./Pages/LoginPage";
import SignUpPage from "./Pages/SignUpPage";
import HomePage from "./Pages/HomePage";
import ProfilePage from "./Pages/ProfilePage";
import AlertComponent from "./Components/AlertComponent";
import CameraPage from "./Pages/CameraPage";
import MainPage from "./Pages/MainPage";


function App() {
  return (
    <div className="App">

      <AlertComponent/>    
        <BrowserRouter>
          <Routes>
          <Route path="/home" element={<MainPage />} />
          <Route path="/profile" element={<ProfilePage />} />


            {/* <Route path="/" element={<SignUpPage />} />
            <Route path="/login" element={<LoginPage />} />
            <Route path="/home" element={<HomePage />} />
            <Route path="/profile" element={<ProfilePage />} />
            <Route path="/camera" element={<CameraPage />} /> */}

          </Routes>
        </BrowserRouter>
        

    </div>
  );
}

export default App;
