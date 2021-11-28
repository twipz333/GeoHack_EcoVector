import React from "react";
import { Descriptions } from "antd";

export const ActivityDescription = ({ date, geolocation, tags }) => {
  return (
    <Descriptions>
      <Descriptions.Item label="Дата">{date}</Descriptions.Item>
      <Descriptions.Item label="Локация">{geolocation}</Descriptions.Item>
      <Descriptions.Item label="Теги">{tags.join(", ")}</Descriptions.Item>
    </Descriptions>
  );
};
