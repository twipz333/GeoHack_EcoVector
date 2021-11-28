import React from "react";
import { Link } from "react-router-dom";
import { Layout, Menu } from "antd";

const { Header } = Layout;
export const AppHeader = () => {
  return (
    <Header>
      <div className="header-logo">
        <img width={50} src="/img/logo.png" alt="logo" />
      </div>
      <Menu mode="horizontal">
        <Menu.Item key="/activities">
          <Link to="/activities">Мероприятия</Link>
        </Menu.Item>
        <Menu.Item key="/activities/add">
          <Link to="/activities/add">Создать мероприятие</Link>
        </Menu.Item>
        <Menu.Item key="/personal">
          <Link to="/personal">Личный кабинет</Link>
        </Menu.Item>
        <Menu.Item key="/signup">
          <Link to="/signup">Регистрация</Link>
        </Menu.Item>
        <Menu.Item key="/signin">
          <Link to="/signin">Вход</Link>
        </Menu.Item>
      </Menu>
    </Header>
  );
};
