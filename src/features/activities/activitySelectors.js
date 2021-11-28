// Получает списочные элементы каталога определённой категории
const selectCatalogListItems = (state, type) =>
    state.catalog.cache.listItems[type];

// Получает элемент каталога
const selectCatalogItem = (state, type, { id, url }) => {
    return state.catalog.cache.items[type]?.find((item) => {
        const res = id ? Number(item.id) === Number(id) : item.url === url;
        return res;
    });
};

// Получает статус запроса
const selectCatalogStatus = (state) => {
    return [state.catalog.status, state.catalog.error];
};

export { selectCatalogListItems, selectCatalogItem, selectCatalogStatus };
