import React from "react";
import { BrowserRouter } from "react-router-dom";
import { Routes } from "./Routes";
// import { useDispatch } from "react-redux";
// import { getCurrUserId } from "./features/user/helpers";
// import { loginUser } from "./features/user/userThunks";

function App() {
  // const dispatch = useDispatch();
  // const currentUserId = getCurrUserId();
  // if (currentUserId) {
  //   dispatch(loginUser(currentUserId));
  // }
  return (
    <BrowserRouter>
      <div className="App">
        <Routes />
      </div>
    </BrowserRouter>
  );
}

export default App;
