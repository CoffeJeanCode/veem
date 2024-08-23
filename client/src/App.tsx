import { Route, Redirect, Router } from "wouter"
import RegisterPage from "./pages/Register";
import LogInPage from "./pages/LogIn";

function App() {


  return (
    <>
      <Router>
        <Route path="/register" component={RegisterPage} />
        <Route path="/login" component={LogInPage} />
        <Route> 404 No se encotron</Route>
      </Router>
    </>
  );
}

export default App;
