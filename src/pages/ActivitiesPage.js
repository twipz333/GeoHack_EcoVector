import React from "react";
import { Typography } from "antd";
import { Page } from "./Page";
import { Activities } from "../features/activities/Activities";
import { TagsMenu } from "../features/tags/TagsMenu";

const { Title } = Typography;

export const ActivitiesPage = () => {
  return (
    <Page sidebar={<TagsMenu />}>
      <Title>Список мероприятий</Title>
      <Activities />
    </Page>
  );
};
