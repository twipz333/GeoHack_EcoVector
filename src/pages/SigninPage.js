import React from "react";
import { Typography } from "antd";
import { Page } from "./Page";
import { Signin } from "../features/user/Signin";

const { Title } = Typography;

export const SigninPage = () => {
  return (
    <Page>
      <Title>Авторизация</Title>
      <Signin />
    </Page>
  );
};
