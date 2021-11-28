import React from "react";
import { Page } from "./Page";
import { AddActivityForm } from "../features/activities/AddActivityForm";
import { Typography } from "antd";

const { Title } = Typography;

export const AddActivityPage = () => {
  return (
    <Page>
      <Title>Создание мероприятия</Title>
      <AddActivityForm />
    </Page>
  );
};
