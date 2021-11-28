import { useDispatch } from "react-redux";
import { Form, Input, Button, Checkbox, Typography } from "antd";
import { createUser } from "./userThunks";

export const Signup = () => {
  const dispatch = useDispatch();

  const finishHandler = (evt) => {
    const userData = new FormData(evt.target);
    console.log(evt);
    console.log(userData);
    dispatch(createUser(JSON.stringify(evt)));
  };

  return (
    <Form
      name="signup"
      labelCol={{ span: 8 }}
      wrapperCol={{ span: 16 }}
      initialValues={{ remember: true }}
      onFinish={finishHandler}
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
        <Input />
      </Form.Item>

      <Form.Item
        id="email"
        label="E-mail"
        name="email"
        rules={[{ required: true, message: "Пожалуйста, введите e-mail" }]}
      >
        <Input />
      </Form.Item>

      <Form.Item
        id="phone"
        label="Телефон"
        name="phone"
        rules={[{ required: true, message: "Пожалуйста, введите телефон" }]}
      >
        <Input />
      </Form.Item>

      <Form.Item
        id="password"
        label="Пароль"
        name="password"
        rules={[{ required: true, message: "Пожалуйста, введите пароль" }]}
      >
        <Input.Password />
      </Form.Item>

      <Form.Item
        name="remember"
        valuePropName="checked"
        wrapperCol={{ offset: 8, span: 16 }}
      >
        <Checkbox defaultChecked={true}>Запомнить меня</Checkbox>
      </Form.Item>

      <Form.Item
        name="personalInfo"
        valuePropName="checked"
        wrapperCol={{ offset: 8, span: 16 }}
        rules={[
          {
            required: true,
            message: "Требуется согласие на обработку персональных данных",
          },
        ]}
      >
        <Checkbox>
          Даю{" "}
          <Typography.Link href="#">
            согласие на обработку персональных данных
          </Typography.Link>
        </Checkbox>
      </Form.Item>

      <Form.Item wrapperCol={{ offset: 8, span: 16 }}>
        <Button type="primary" htmlType="submit">
          Зарегистрироваться
        </Button>
      </Form.Item>
    </Form>
  );
};
