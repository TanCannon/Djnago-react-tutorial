import react from "react"
//added by me //
import {BrowserRouter, Routes, Route, Navigate} from "react-router-dom"
import Login from "./pages/Login"
import Register from "./pages/Register"
import Home from "./pages/Home"
import NotFound from "./pages/NotFound"
import  ProtectedRoute from "./components/ProtectedRoute"

//clear the current credential jwt access and refersh tokens in browser local storage 
function Logout(){
  localStorage.clear()
  return <Navigate to="/login"/>
}


//register through Register.jsx -> Form.jsx
function RegisterAndLogout(){
  localStorage.clear()
  return <Register/>
}



function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route
          path="/" 
          element ={
            <ProtectedRoute>
              <Home/>
            </ProtectedRoute>
          }
        />
        <Route path="/login" element = {<Login/>}/>
        <Route path="/logout" element = {<Logout/>}/>
        <Route path="/register" element = {<RegisterAndLogout/>}/>
        {/* for any other path we say '*' */}
        <Route path="*" element = {<NotFound/>}/>
      </Routes>
    </BrowserRouter>
  )
}

export default App
