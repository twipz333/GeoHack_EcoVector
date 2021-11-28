import React from "react";
import { Switch, Route } from "react-router-dom";
import { MainPage } from "./pages/MainPage";
import { AddActivityPage } from "./pages/AddActivityPage";
import { ActivitiesPage } from "./pages/ActivitiesPage";
import { PersonalPage } from "./pages/PersonalPage";
import { SignupPage } from "./pages/SignupPage";
import { SigninPage } from "./pages/SigninPage";

export const Routes = () => {
  return (
    <Switch>
      <Route exact path="/activities/add">
        <AddActivityPage />
      </Route>
      <Route exact path="/activities">
        <ActivitiesPage />
      </Route>
      <Route exact path="/signin">
        <SigninPage />
      </Route>
      <Route exact path="/signup">
        <SignupPage />
      </Route>
      <Route exact path="/personal">
        <PersonalPage />
      </Route>
      <Route exact path="/">
        <MainPage />
      </Route>
      <Route path="/" />
    </Switch>
  );
};
