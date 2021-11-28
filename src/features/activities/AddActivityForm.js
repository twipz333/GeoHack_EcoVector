import React from "react";
import { Form, Input, Button, Select } from "antd";
import { MinusCircleOutlined, PlusOutlined } from "@ant-design/icons";
import { tagsData } from "../tags/tagsData";

export const AddActivityForm = () => {
  const onFinish = (values) => {
    console.log("Success:", values);
  };

  const onFinishFailed = (errorInfo) => {
    console.log("Failed:", errorInfo);
  };

  const formItemLayout = {
    labelCol: {
      span: 8,
    },
    wrapperCol: {
      span: 8,
    },
  };
  const formItemLayoutWithOutLabel = {
    wrapperCol: {
      span: 8,
      offset: 8,
    },
  };

  const options = tagsData.map((tag) => {
    return <Select.Option value={tag}>{tag}</Select.Option>;
  });

  return (
    <Form
      name="addActivity"
      labelCol={{
        span: 8,
      }}
      wrapperCol={{
        span: 16,
      }}
      onFinish={onFinish}
      onFinishFailed={onFinishFailed}
      autoComplete="off"
    >
      <Form.Item
        label="Название"
        name="title"
        rules={[
          {
            required: true,
            message: "Пожалуйста, введите название мероприятия",
          },
        ]}
      >
        <Input />
      </Form.Item>
      <Form.Item
        label="Локация"
        name="geolocation"
        rules={[
          {
            required: true,
            message: "Пожалуйста, напишите место проведения мероприятия",
          },
        ]}
      >
        <Input placeholder="Место проведения мероприятия" />
      </Form.Item>
      <Form.Item
        label="Даты проведения"
        name="date"
        rules={[
          {
            required: true,
            message: "Пожалуйста, напишите когда будет проводиться мероприятие",
          },
        ]}
      >
        <Input placeholder="Когда будет проводиться мероприятие" />
      </Form.Item>

      <Form.List name="tags">
        {(fields, { add, remove }, { errors }) => {
          return (
            <>
              {fields.map((field, index) => {
                return (
                  <Form.Item
                    {...(index === 0
                      ? formItemLayout
                      : formItemLayoutWithOutLabel)}
                    label={index === 0 ? "Теги" : ""}
                    required={false}
                    key={field.key}
                  >
                    <Form.Item
                      {...field}
                      validateTrigger={["onChange", "onBlur"]}
                      rules={[
                        {
                          required: true,
                          whitespace: true,
                          message: "Пожалуйста, добавьте теги",
                        },
                      ]}
                      noStyle
                    >
                      <Select
                        showSearch
                        style={{ width: "60%" }}
                        placeholder="Выберите тег"
                        optionFilterProp="children"
                        filterOption={(input, option) =>
                          option.children
                            .toLowerCase()
                            .indexOf(input.toLowerCase()) >= 0
                        }
                      >
                        {options}
                      </Select>
                    </Form.Item>
                    {fields.length > 1 ? (
                      <MinusCircleOutlined
                        className="dynamic-delete-button"
                        onClick={() => remove(field.name)}
                      />
                    ) : null}
                  </Form.Item>
                );
              })}
              <Form.Item
                wrapperCol={{
                  offset: 8,
                  span: 16,
                }}
              >
                <Button onClick={() => add()} icon={<PlusOutlined />}>
                  Добавить тег
                </Button>
              </Form.Item>
            </>
          );
        }}
      </Form.List>

      <Form.Item
        label="Описание"
        name="description"
        rules={[
          {
            required: true,
            message: "Пожалуйста, введите описание мероприятия",
          },
        ]}
      >
        <Input.TextArea rows={10} />
      </Form.Item>

      <Form.Item
        wrapperCol={{
          offset: 8,
          span: 16,
        }}
      >
        <Button type="primary" htmlType="submit">
          Создать
        </Button>
      </Form.Item>
    </Form>
  );
};
