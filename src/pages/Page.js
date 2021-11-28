import React from "react";
import { Layout } from "antd";
import { AppHeader } from "../layout/AppHeader";

const { Footer, Content, Sider } = Layout;

export const Page = ({ sidebar, children }) => {
  const content = <Content className="app-content">{children}</Content>;
  let siderLayout = null;
  if (sidebar) {
    siderLayout = (
      <Layout>
        {content}
        <Sider>{sidebar}</Sider>
      </Layout>
    );
  }
  return (
    <Layout>
      <AppHeader></AppHeader>
      {siderLayout || content}
      <Footer></Footer>
    </Layout>
  );
};
