import { HashRouter, Routes, Route } from "react-router-dom";

import LoginPage from "./Pages/LoginPage";
import SignUpPage from "./Pages/SignUpPage";
import ProfilePage from "./Pages/ProfilePage";
import AlertComponent from "./Components/AlertComponent";
import MainPage from "./Pages/MainPage";


function App() {
  return (
    <div className="App">

      <AlertComponent/>    
        <HashRouter>
          <Routes>
          <Route path="/" element={<MainPage />} />
          <Route path="/profile" element={<ProfilePage />} />
          <Route path="/login" element={<LoginPage />} />
          <Route path="/signup" element={<SignUpPage />}/>
          </Routes>
        </HashRouter>
        

    </div>
  );
}

export default App;