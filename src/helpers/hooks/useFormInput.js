import { useState } from "react";

/**
 *
 * @param {String} initialValue
 *
 * Возвращает три значения:
 * @return {String} Значение.
 * @return {Function} Функцию меняющую значение.
 * @return {Function} Функцию сбрасывающую значение на пустую строку.
 */
export function useFormInput(initialValue) {
  const [value, setValue] = useState(initialValue);

  const handleChange = (event) => {
    setValue(event.target.value);
  };

  const resetValue = () => {
    console.log(1);
    setValue("");
  };

  return [value, handleChange, resetValue];
}
