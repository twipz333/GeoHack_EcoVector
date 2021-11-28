import React from "react";
import { List } from "antd";
import { ActivityDescription } from "./ActivityDescription";
import { Typography } from "antd";

export const ActivitiesListItem = ({
  title,
  content,
  date,
  geolocation,
  image,
  tags,
}) => {
  const { Item } = List;
  const { Paragraph } = Typography;
  return (
    <Item extra={<img width={272} alt="logo" src={image} />}>
      <Item.Meta
        title={<a href="#">{title}</a>}
        description={
          <ActivityDescription
            date={date}
            geolocation={geolocation}
            tags={tags}
          />
        }
      ></Item.Meta>
      <Paragraph style={{ textAlign: "justify" }}>{content}</Paragraph>
    </Item>
  );
};
