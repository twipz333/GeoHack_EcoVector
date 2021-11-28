import React from "react";
import { Typography } from "antd";
import { Page } from "./Page";
import { Signup } from "../features/user/Signup";

const { Title } = Typography;

export const SignupPage = () => {
  return (
    <Page>
      <Title>Регистрация</Title>
      <Signup />
    </Page>
  );
};
