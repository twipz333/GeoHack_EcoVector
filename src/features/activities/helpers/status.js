// Устанавливает статус ожидания
const setPending = (state) => {
    state.status = 'loading';
    state.error = null;
};

// Устанавливает статус ошибки
const setError = (state, error) => {
    state.status = 'idle';
    state.error = error || 'Неизвестная ошибка';
};

// Сбрасывает статус
const resetStatus = (state) => {
    state.status = 'idle';
    state.error = null;
};

export { setPending, setError, resetStatus };
