import React from "react";
import { List } from "antd";
import { ActivitiesListItem } from "./ActivitiesListItem";

export const ActivitiesList = ({ activities }) => {
  return (
    <List
      className="activities-list"
      itemLayout="vertical"
      size="large"
      dataSource={activities}
      renderItem={(item) => {
        const { id, title, description, date, geolocation, image, tags } = item;
        return (
          <ActivitiesListItem
            key={id}
            title={title}
            content={description}
            date={date}
            geolocation={geolocation}
            image={image}
            tags={tags}
          />
        );
      }}
    />
  );
};
