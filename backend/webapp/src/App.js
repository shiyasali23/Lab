import { HashRouter, Routes, Route } from "react-router-dom";

import ProfilePage from "./Pages/ProfilePage";
import AlertComponent from "./Components/AlertComponent";
import MainPage from "./Pages/MainPage";
import ConsultPage from "./Pages/ConsultPage";
import LandingPage from "./Pages/LandingPage";


function App() {
  return (
    <div className="App">

      <AlertComponent/>    
        <HashRouter>
          <Routes>
          <Route path="/" element={<LandingPage />} />
          <Route path="/main" element={<MainPage />} />
          <Route path="/profile" element={<ProfilePage />} />
          <Route path="/consult" element={<ConsultPage />} />
          </Routes>
        </HashRouter>
        

    </div>
  );
}

export default App;
