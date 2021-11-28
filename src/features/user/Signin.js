import { useState } from "react";
import { useFormInput } from "../../helpers/hooks/useFormInput";
import { useDispatch } from "react-redux";
import { Form, Input, Button, Checkbox } from "antd";

export const Signin = () => {
  const [username, onUsernameChange, usernameReset] = useFormInput("");
  const [password, onPasswordChange, passwordReset] = useFormInput("");
  const dispatch = useDispatch();

  const finishHandler = (event) => {
    event.preventDefault();

    usernameReset();
    passwordReset();
  };

  return (
    <Form
      name="signin"
      labelCol={{ span: 8 }}
      wrapperCol={{ span: 16 }}
      initialValues={{ remember: true }}
      onSubmit={finishHandler}
      autoComplete="off"
    >
      <Form.Item
        id="username"
        label="Имя пользователя"
        name="username"
        rules={[
          { required: true, message: "Пожалуйста, введите имя пользователя" },
        ]}
      >
        <Input onChange={onUsernameChange} value={username} />
      </Form.Item>

      <Form.Item
        id="password"
        label="Пароль"
        name="password"
        rules={[{ required: true, message: "Пожалуйста, введите пароль" }]}
      >
        <Input.Password onChange={onPasswordChange} value={password} />
      </Form.Item>

      <Form.Item wrapperCol={{ offset: 8, span: 16 }}>
        <Button type="primary" htmlType="submit">
          Войти
        </Button>
      </Form.Item>
    </Form>
  );
};
