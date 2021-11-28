// Добавляет элемент в кеш
const addItemToCache = (state, item) => {
  const cache = state.cache || [];
  cache.push(item);
  // Кладём элемент в кеш
  state.cache = cache;
};

export { addItemToCache };
