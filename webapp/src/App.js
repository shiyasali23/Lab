import { BrowserRouter, Routes, Route } from "react-router-dom";

import LoginPage from "./Pages/LoginPage";
import SignUpPage from "./Pages/SignUpPage";
import HomePage from "./Pages/HomePage";
import ProfilePage from "./Pages/ProfilePage";


function App() {
  return (
    <div className="App">

            
        <BrowserRouter>
          <Routes>
            <Route path="/" element={<SignUpPage />} />
            <Route path="/login" element={<LoginPage />} />
            <Route path="/home" element={<HomePage />} />
            <Route path="/profile" element={<ProfilePage />} />

          </Routes>
        </BrowserRouter>
        

    </div>
  );
}

export default App;
