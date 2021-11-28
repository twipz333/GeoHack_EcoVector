import React from "react";
import { Link } from "react-router-dom";
import { Menu, Typography } from "antd";
import { tagsData } from "./tagsData";

export const TagsMenu = () => {
  const tagsMenuItems = tagsData.map((tag) => {
    return (
      <Menu.Item key={tag}>
        <Link to="#">{tag}</Link>
      </Menu.Item>
    );
  });
  return (
    <>
      <Typography.Title className="tags-title" level={2}>
        Теги
      </Typography.Title>
      <Menu className="tags-menu" mode="vertical">
        {tagsMenuItems}
      </Menu>
    </>
  );
};
